# Working Memory Experiments - Client Package

**Two separate experiments studying working memory under cognitive load**

Version: 2.0.0  
Delivered: 2026-09-02

---

## 📦 What's Included

### Main Experiment Files:
- **`experiment1_simultaneous.py`** - Experiment 1 (all 4 squares shown together)
- **`experiment2_sequential.py`** - Experiment 2 (4 squares shown one at a time)

### Launch Files (Windows):
- **`RUN_EXPERIMENT1.bat`** - Double-click to run Experiment 1
- **`RUN_EXPERIMENT2.bat`** - Double-click to run Experiment 2

### Condition Files:
- **`conditions/practice_conditions.csv`** - 6 practice trials
- **`conditions/experiment1_conditions.csv`** - 144 main trials
- **`conditions/experiment2_conditions.csv`** - 144 main trials

### Data Enhancement:
- **`enhance_data.py`** - Convert CSV to formatted Excel with colors
- **`ENHANCE_DATA.bat`** - Windows launcher for enhancement tool

### Documentation:
- **`DATA_DICTIONARY.md`** - Complete description of all data variables
- **`CLIENT_README.md`** - This file

---

## 🚀 Quick Start

### 1. Install PsychoPy

**Download PsychoPy Standalone:**
https://www.psychopy.org/download.html

(This is recommended - works on all systems)

### 2. Run an Experiment

**Option A: Using Double-Click (Easiest)**
- Double-click **`RUN_EXPERIMENT1.bat`** for Experiment 1
- Double-click **`RUN_EXPERIMENT2.bat`** for Experiment 2

**Option B: Using PsychoPy App**
1. Open PsychoPy application
2. File → Open → Select `experiment1_simultaneous.py` or `experiment2_sequential.py`
3. Click the green Run button (▶️)

**Option C: Using Command Line**
```bash
python experiment1_simultaneous.py
# or
python experiment2_sequential.py
```

### 3. Collect Data

- Participant enters their information
- Completes 6 practice trials
- Completes 144 main trials (~45 minutes)
- Data automatically saved to `data/` folder

### 4. (Optional) Enhance Data

- Double-click **`ENHANCE_DATA.bat`**
- Select your CSV file
- Get beautiful Excel file with color-coding!

---

## 📊 The Two Experiments

### Experiment 1: Simultaneous Presentation
- **What:** All 4 colored squares shown **at the same time**
- **Duration:** ~40-50 minutes
- **File:** `experiment1_simultaneous.py`

### Experiment 2: Sequential Presentation  
- **What:** 4 colored squares shown **one at a time**
- **Duration:** ~45-55 minutes
- **File:** `experiment2_sequential.py`

### Both Include:
- Practice trials (6)
- Main trials (144)
- Cognitive load manipulation (0, 2, or 4 digits)
- Memory test (same/different?)
- Thought probe (8 categories)

---

## 📁 Data Output

### File Location:
`data/` folder

### File Names:
```
{ParticipantID}_Experiment1_Simultaneous_{Date}_data.csv
{ParticipantID}_Experiment2_Sequential_{Date}_data.csv
```

### Example:
```
P001_Experiment1_Simultaneous_2026_Sep02_1430_data.csv
P001_Experiment2_Sequential_2026_Sep02_1500_data.csv
```

### What's Logged:
- Participant information
- Trial conditions
- Memory stimuli (colors, positions)
- Parity task responses and accuracy
- Memory test responses and accuracy
- Thought probe responses
- Reaction times
- Timestamps

**See `DATA_DICTIONARY.md` for complete variable descriptions.**

---

## 🎮 Response Keys

| Task | Key | Action |
|------|-----|--------|
| **Parity** | F | Odd number |
| | J | Even number |
| **Memory** | S | Same color |
| | D | Different color |
| **Thought** | 1-8 | Category number |
| **Control** | SPACE | Continue |
| | ESC | Quit experiment |

---

## ⚙️ System Requirements

### Minimum:
- Windows 10 or later (Mac/Linux compatible too)
- Python 3.8+ (if not using PsychoPy Standalone)
- 1920×1080 display
- 60Hz refresh rate
- Keyboard

### Recommended:
- PsychoPy Standalone installed
- 1920×1080 or higher display
- Quiet testing environment
- Approximately 1 hour per participant

---

## 📖 Documentation

### Full Variable Documentation:
**`DATA_DICTIONARY.md`** - Describes all 35 output variables

### Quick Reference:
- **participant** - Participant ID
- **load_condition** - Cognitive load (0, 2, or 4 digits)
- **change_condition** - Whether test color changed
- **memory_correct** - Memory accuracy (1=correct, 0=wrong)
- **memory_rt** - Memory reaction time (seconds)
- **parity_correct_1-4** - Parity accuracy for each digit
- **thought_probe_label** - What participant was thinking

---

## 🎨 Data Enhancement Feature

Convert plain CSV to beautiful formatted Excel:

### How to Use:
1. Run experiment and get CSV file
2. Double-click **`ENHANCE_DATA.bat`**
3. Select CSV file
4. Get formatted Excel with:
   - Color-coded headers (blue)
   - Alternating row colors
   - **Green** for correct answers
   - **Red** for incorrect answers
   - Summary statistics

---

## ⚠️ Troubleshooting

### "Shader compilation failed" Error
**Solution:** Use PsychoPy Standalone instead of pip-installed version

### Window doesn't go fullscreen
**Solution:** Experiment will show warning and continue in windowed mode (still works fine)

### "Participant ID cannot be empty"
**Solution:** Restart and enter a valid participant ID

### "File already exists" Dialog
**Options:**
- **Cancel** - Stop without overwriting
- **Overwrite** - Replace old file (⚠️ data loss!)
- **New Session** - Create new file with timestamp

### Python not found
**Solution:** Install PsychoPy Standalone (doesn't require separate Python)

---

## 📞 Support

### For Technical Issues:
- PsychoPy Forum: https://discourse.psychopy.org/
- PsychoPy Docs: https://www.psychopy.org/documentation.html

### For Study Design Questions:
- Original Paper: https://econtent.hogrefe.com/doi/10.1027/1618-3169/a000599

---

## 📂 Project Structure

```
Working Memory Experiments/
│
├── experiment1_simultaneous.py      ← Experiment 1 script
├── experiment2_sequential.py        ← Experiment 2 script
│
├── RUN_EXPERIMENT1.bat              ← Launch Experiment 1
├── RUN_EXPERIMENT2.bat              ← Launch Experiment 2
│
├── conditions/                      ← Trial configurations
│   ├── practice_conditions.csv
│   ├── experiment1_conditions.csv
│   └── experiment2_conditions.csv
│
├── data/                            ← Data output (created automatically)
│   └── [participant data files]
│
├── enhance_data.py                  ← Excel formatter
├── ENHANCE_DATA.bat                 ← Excel formatter launcher
│
├── DATA_DICTIONARY.md               ← Variable documentation
└── CLIENT_README.md                 ← This file
```

---

## ✅ Quality Assurance

### Before Data Collection:
- ✅ PsychoPy installed
- ✅ Monitor at least 60Hz
- ✅ Quiet environment
- ✅ Keyboard working
- ✅ Instructions prepared

### After Data Collection:
- ✅ CSV file in `data/` folder
- ✅ 144 trials present (check row count)
- ✅ All responses recorded
- ✅ No excessive missing data

---

## 📊 Expected Output

### Per Experiment:
- **Trials:** 144 main + 6 practice = 150 rows
- **Columns:** 35 variables
- **Duration:** 40-55 minutes
- **File size:** ~50-100 KB (CSV)

### Both Experiments:
- **Total time:** ~90-120 minutes (with break between)
- **Total trials:** 288 main trials (144 × 2)
- **2 CSV files** (one per experiment)

---

## 🎯 Key Features

✅ **Separate experiments** - Run independently or together  
✅ **Automatic data saving** - No data loss  
✅ **Duplicate protection** - Warns before overwriting  
✅ **Frame-based timing** - Precise stimulus presentation  
✅ **Randomization** - Proper trial randomization  
✅ **Comprehensive logging** - 35 variables per trial  
✅ **Excel enhancement** - Beautiful formatted output  
✅ **Complete documentation** - Data dictionary included  

---

## 📝 Citation

If using these experiments in research:

**Original Study:**
```
Holmqvist, K., & Sohlberg, R. (2024). 
[Full citation from paper]
https://econtent.hogrefe.com/doi/10.1027/1618-3169/a000599
```

**This Implementation:**
```
Working Memory Experiments v2.0
Based on Holmqvist & Sohlberg (2024)
Delivered: 2026-09-02
```

---

## 🎉 You're Ready!

**To run Experiment 1:**
→ Double-click `RUN_EXPERIMENT1.bat`

**To run Experiment 2:**
→ Double-click `RUN_EXPERIMENT2.bat`

**To enhance data:**
→ Double-click `ENHANCE_DATA.bat`

**For help:**
→ Read `DATA_DICTIONARY.md`

---

**Good luck with your data collection!** 🚀

*Delivered by: [Your Name]*  
*Date: 2026-09-02*  
*Version: 2.0.0*
