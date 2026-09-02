"""Shared runtime helpers for the two PsychoPy experiments."""

import math
import re


def sanitize_participant_id(value):
    """Return a Windows-safe participant ID for use in data filenames."""
    cleaned = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", str(value).strip())
    cleaned = cleaned.rstrip(". ")[:80]
    return cleaned or "participant"


def _close_window(win):
    if win is not None:
        try:
            win.close()
        except Exception:
            pass


def create_compatible_window(visual, core):
    """Create and render-test a window, falling back for older graphics cards."""
    profiles = [
        (
            "fullscreen compatibility mode",
            dict(
                size=[1920, 1080],
                fullscr=True,
                units="height",
                color=[0, 0, 0],
                allowGUI=False,
                useFBO=False,
                allowStencil=False,
                multiSample=False,
                checkTiming=False,
                gammaErrorPolicy="warn",
                autoLog=False,
            ),
        ),
        (
            "windowed compatibility mode",
            dict(
                size=[1280, 720],
                fullscr=False,
                units="height",
                color=[0, 0, 0],
                allowGUI=True,
                useFBO=False,
                useRetina=False,
                allowStencil=False,
                multiSample=False,
                checkTiming=False,
                gammaErrorPolicy="warn",
                autoLog=False,
            ),
        ),
        (
            "basic windowed mode",
            dict(
                size=[800, 600],
                fullscr=False,
                units="height",
                color=[0, 0, 0],
                allowGUI=True,
                useFBO=False,
                useRetina=False,
                allowStencil=False,
                multiSample=False,
                checkTiming=False,
                winType="pyglet",
                gammaErrorPolicy="warn",
                autoLog=False,
            ),
        ),
        (
            "legacy low-end windowed mode",
            dict(
                size=[800, 600],
                fullscr=False,
                units="height",
                color=[0, 0, 0],
                allowGUI=True,
                useFBO=False,
                useRetina=False,
                allowStencil=False,
                multiSample=False,
                checkTiming=False,
                winType="pygame",
                gammaErrorPolicy="warn",
                autoLog=False,
            ),
        ),
    ]

    failures = []
    for description, options in profiles:
        win = None
        print(f"Trying {description}...")
        try:
            win = visual.Window(**options)

            # Window construction alone is not enough. Some driver/shader errors
            # appear only on the first TextStim draw or buffer flip.
            measuring_text = visual.TextStim(
                win,
                text="Checking display compatibility...\nPlease wait...",
                height=0.05,
                color="white",
            )
            measuring_text.draw()
            win.flip()

            frame_rate = win.getActualFrameRate(
                nIdentical=5,
                nMaxFrames=60,
                nWarmUpFrames=5,
            )
            if not frame_rate or not math.isfinite(frame_rate) or frame_rate < 20:
                print("Stable frame rate was not detected; using a safe 60 Hz timing fallback.")
                frame_rate = 60.0

            ready_text = visual.TextStim(
                win,
                text="Ready!\n\nStarting experiment...",
                height=0.05,
                color="white",
            )
            ready_text.draw()
            win.flip()
            core.wait(1.0)

            frame_duration = 1.0 / max(1, round(frame_rate))
            print(f"Display ready using {description} ({frame_rate:.2f} Hz).")
            return win, frame_rate, frame_duration
        except Exception as exc:
            failures.append(f"{description}: {type(exc).__name__}: {exc}")
            print(f"Display test failed in {description}: {exc}")
            _close_window(win)

    details = "\n".join(failures)
    raise RuntimeError(
        "PsychoPy could not create a working display using any compatibility mode.\n"
        + details
    )
