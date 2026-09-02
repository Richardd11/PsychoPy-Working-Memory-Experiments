# 🧠 PsychoPy Working Memory Experiments

**Full Array Test Design - Working Memory with Cognitive Load and Mind Wandering**

[![PsychoPy](https://img.shields.io/badge/PsychoPy-3.x-blue.svg)](https://www.psychopy.org/)
[![Python](https://img.shields.io/badge/Python-3.8+-green.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Based on research: [Robison & Unsworth (2023)](https://econtent.hogrefe.com/doi/10.1027/1618-3169/a000599)

---

## 📋 Overview

This repository contains **two PsychoPy experiments** investigating working memory capacity under different presentation conditions:

- **Experiment 1**: Simultaneous presentation (all 4 colored squares shown at once)
- **Experiment 2**: Sequential presentation (4 colored squares shown one at a time)

### 🎯 Key Feature: Full Array Test Design

Unlike traditional change detection paradigms that test single items, this implementation uses a **full array comparison** where participants see all 4 colors again and judge if the entire array is identical or if at least one item changed.

---

## 🚀 Quick Start

### Prerequisites

```bash
# Install Python 3.8 or higher
# Install PsychoPy
pip install psychopy
```

### Running the Experiments

**Windows:**
```bash
RUN_EXPERIMENT1.bat  # Experiment 1 - Simultaneous
RUN_EXPERIMENT2.bat  # Experiment 2 - Sequential
```

**Manual:**
```bash
python experiment1_simultaneous.py
python experiment2_sequential.py
```

---

## 🎮 Experiment Design

### Trial Structure

```
1. FIXATION (+)               → 500ms
2. MEMORY ARRAY (4 colors)    → 500ms
3. ISI (blank)                → 200ms
4. PARITY TASK (0/2/4 digits) → 3.0s per digit
5. MEMORY TEST (all 4 colors) → 5.0s max
6. THOUGHT PROBE              → No time limit
```

### Memory Test Phase

**Participant sees:**
```
🟦 🟥 🟩 🟨  (all 4 squares shown together)
```

**Question:**
```
Are all 4 colors the SAME as before?

S = SAME (all identical)
D = DIFFERENT (at least one changed)
```

### Conditions

- **Load**: 0, 2, or 4 digits (cognitive load manipulation)
- **Change**: 50% same, 50% one color changes
- **Trials**: 144 total (breaks every 36 trials)
- **Practice**: 6 trials before main experiment

---

## 📊 Data Output

All data saved to `data/` folder as CSV files.

### Key Variables

| Variable | Description |
|----------|-------------|
| `load_condition` | 0, 2, or 4 (number of parity digits) |
| `change_condition` | 'change' or 'no_change' |
| `changed_position` | Which position changed (0-3, or 'NA') |
| `original_color_1-4` | Colors shown in memory phase |
| `test_color_1-4` | Colors shown in test phase |
| `memory_response` | 's' (same) or 'd' (different) |
| `memory_correct` | 1 (correct) or 0 (incorrect) |
| `parity_digit_1-4` | Digits shown in parity task |
| `parity_correct_1-4` | Accuracy on each digit |
| `thought_probe_response` | 1-8 (thought category) |

See [DATA_DICTIONARY.md](DATA_DICTIONARY.md) for complete variable descriptions.

---

## 📂 Repository Structure

```
PsychoPy-Working-Memory-Experiments/
├── experiment1_simultaneous.py      # Exp 1: All 4 colors at once
├── experiment2_sequential.py        # Exp 2: Colors one by one
├── RUN_EXPERIMENT1.bat              # Windows launcher
├── RUN_EXPERIMENT2.bat              # Windows launcher
├── conditions/                      # Trial condition files
│   ├── practice_conditions.csv
│   ├── experiment1_conditions.csv
│   └── experiment2_conditions.csv
├── data/                            # Output folder (auto-created)
├── analyze_data.py                  # Basic data analysis
├── enhance_data.py                  # Advanced analysis with outliers
├── ENHANCE_DATA.bat                 # Analysis launcher
├── COMPLETE_GUIDE.html              # Interactive documentation
├── VISUAL_EXPLANATION.html          # Why full array test?
├── CLIENT_README.md                 # Client-friendly guide
├── DATA_DICTIONARY.md               # Variable descriptions
└── README.md                        # This file
```

---

## 🔬 Research Background

This implementation is based on:

**Robison, M. K., & Unsworth, N. (2023).**  
*Mind wandering and working memory capacity: A sequential working memory task.*  
Experimental Psychology, 70(4), 219-229.  
DOI: [10.1027/1618-3169/a000599](https://econtent.hogrefe.com/doi/10.1027/1618-3169/a000599)

### Key Modification

**Original Paper**: Single item test (show 1 square, ask if it changed)  
**This Implementation**: Full array test (show all 4 squares, ask if all are same)

**Rationale**: More intuitive for participants, tests whole-array comparison rather than individual item memory.

---

## 📈 Data Analysis

### Basic Analysis
```bash
python analyze_data.py
# Or double-click: ENHANCE_DATA.bat
```

**Outputs:**
- Accuracy by load condition
- Reaction time statistics
- Thought probe distribution
- Participant summaries

### Advanced Analysis (with Outlier Detection)
```bash
python enhance_data.py
```

**Additional features:**
- Outlier detection (RT > 3 SD)
- Trial-level flagging
- Enhanced visualizations

---

## ⚙️ Timing Parameters

All timing constants (in seconds):

```python
FIXATION_DURATION = 0.5        # Fixation cross
MEMORY_DISPLAY_DURATION = 0.5  # Each memory item
ISI_DURATION = 0.2             # Inter-stimulus interval
PARITY_TIMEOUT = 3.0           # Max time per digit
MEMORY_TEST_TIMEOUT = 5.0      # Max time for response
LOAD_0_BLANK_DURATION = 6.0    # Blank screen for load 0
```

---

## 🎨 Stimulus Details

### Colors
8 possible colors: Red, Green, Blue, Yellow, Magenta, Cyan, White, Orange

### Positions
```
[1] [2]    Top-left, Top-right
[3] [4]    Bottom-left, Bottom-right
```

### Parity Digits
Digits: 1, 2, 3, 4, 6, 7, 8, 9 (excludes 5 for ambiguity)

---

## 📚 Documentation

- **[COMPLETE_GUIDE.html](COMPLETE_GUIDE.html)** - Interactive setup and usage guide
- **[VISUAL_EXPLANATION.html](VISUAL_EXPLANATION.html)** - Why full array test design?
- **[CLIENT_README.md](CLIENT_README.md)** - Client-friendly instructions
- **[DATA_DICTIONARY.md](DATA_DICTIONARY.md)** - Complete variable descriptions
- **[SIMPLE_EXPLANATION_TAGALOG.txt](SIMPLE_EXPLANATION_TAGALOG.txt)** - Tagalog explanation

---

## 🐛 Troubleshooting

**Problem: Experiment won't start**
- Ensure PsychoPy is installed: `pip install psychopy`
- Check Python version: `python --version` (need 3.8+)

**Problem: Data not saving**
- `data/` folder is created automatically
- Check file permissions in experiment directory

**Problem: Timing issues**
- Check monitor refresh rate (60Hz recommended)
- Close other applications during experiment

**Problem: Conditions file not found**
- Ensure `conditions/` folder exists with CSV files
- Download from repository if missing

---

## 📝 Citation

If you use this code in your research, please cite:

```bibtex
@software{psychopy_working_memory_2024,
  title = {PsychoPy Working Memory Experiments - Full Array Test Design},
  author = {Your Name},
  year = {2024},
  url = {https://github.com/Richardd11/PsychoPy-Working-Memory-Experiments}
}
```

And the original research:

```bibtex
@article{robison2023mind,
  title={Mind wandering and working memory capacity: A sequential working memory task},
  author={Robison, Matthew K and Unsworth, Nash},
  journal={Experimental Psychology},
  volume={70},
  number={4},
  pages={219--229},
  year={2023},
  publisher={Hogrefe Publishing}
}
```

---

## 📧 Contact

For questions or issues, please open an issue on GitHub.

---

## 📄 License

MIT License - feel free to use and modify for research purposes.

---

**✅ Ready to use!** Clone, run, and start collecting data. 🚀
