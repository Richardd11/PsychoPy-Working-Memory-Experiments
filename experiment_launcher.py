#!/usr/bin/env python
"""Run an experiment with persistent logging and a user-friendly error dialog."""

import faulthandler
import os
from pathlib import Path
import runpy
import sys
import traceback


class Tee:
    def __init__(self, *streams):
        self.streams = streams

    def write(self, value):
        for stream in self.streams:
            stream.write(value)
            stream.flush()
        return len(value)

    def flush(self):
        for stream in self.streams:
            stream.flush()

    def isatty(self):
        return any(getattr(stream, "isatty", lambda: False)() for stream in self.streams)


def show_error(message):
    try:
        import tkinter as tk
        from tkinter import messagebox

        root = tk.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        messagebox.showerror("Experiment could not start", message, parent=root)
        root.destroy()
    except Exception:
        pass


def close_psychopy_windows():
    try:
        from psychopy.visual import window as window_module

        for window_ref in list(window_module.openWindows):
            window = window_ref() if callable(window_ref) else window_ref
            if window is not None:
                try:
                    window.close()
                except Exception:
                    pass
    except Exception:
        pass


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: experiment_launcher.py <experiment.py>")

    project_dir = Path(__file__).resolve().parent
    requested = Path(sys.argv[1]).resolve()
    allowed = {
        (project_dir / "experiment1_simultaneous.py").resolve(),
        (project_dir / "experiment2_sequential.py").resolve(),
    }
    if requested not in allowed or not requested.is_file():
        raise SystemExit("The requested experiment file is missing or invalid.")

    log_dir = project_dir / "logs"
    log_dir.mkdir(exist_ok=True)
    log_path = log_dir / f"{requested.stem}_latest.log"

    os.chdir(project_dir)
    with log_path.open("w", encoding="utf-8", buffering=1) as log_file:
        original_stdout, original_stderr = sys.stdout, sys.stderr
        sys.stdout = Tee(original_stdout, log_file)
        sys.stderr = Tee(original_stderr, log_file)
        faulthandler.enable(file=log_file, all_threads=True)
        try:
            print(f"Starting {requested.name}")
            print(f"Python: {sys.executable}")
            import psychopy

            print(f"PsychoPy: {psychopy.__version__}")
            runpy.run_path(str(requested), run_name="__main__")
            return 0
        except SystemExit as exc:
            code = exc.code if isinstance(exc.code, int) else 0
            return code
        except BaseException:
            print("\nUNHANDLED EXPERIMENT ERROR")
            traceback.print_exc()
            close_psychopy_windows()
            show_error(
                "The experiment encountered an unexpected problem.\n\n"
                f"A diagnostic log was saved here:\n{log_path}\n\n"
                "Please send that log file to the researcher."
            )
            return 1
        finally:
            faulthandler.disable()
            sys.stdout = original_stdout
            sys.stderr = original_stderr


if __name__ == "__main__":
    raise SystemExit(main())
