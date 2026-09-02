# 📊 Professional Excel Export Guide

## 🎨 Features

Your CSV data files are now converted to **beautifully formatted Excel workbooks** with:

### ✨ Visual Enhancements
- 🎨 **Color-coded headers** (professional dark blue)
- 📊 **Alternating row colors** (better readability)
- 📐 **Centered text alignment** (clean look)
- 📏 **Auto-adjusted column widths** (no more tiny columns!)
- 🔒 **Frozen header row** (headers stay visible when scrolling)

### 🎯 Smart Formatting
- ✅ **Green cells** = Correct answers (1)
- ❌ **Red cells** = Incorrect answers (0)
- ⚠️ **Yellow cells** = Not applicable (NA)
- 🔄 **Bold text** for accuracy columns

### 📈 Summary Statistics Sheet
**Automatically included:**
- Participant information
- Overall performance metrics
- Memory accuracy & reaction times
- Parity task accuracy
- Performance breakdown by load condition (0, 2, 4)
- Min/Max values for each metric

---

## 🚀 How to Use

### Method 1: After Experiment (Recommended)
The experiment will ask if you want to export to Excel automatically!

### Method 2: Manual Conversion
1. **Run the batch file:**
   ```
   Double-click: EXPORT_TO_EXCEL.bat
   ```

2. **Or run Python directly:**
   ```bash
   python export_to_excel.py
   ```

3. **Find your formatted files in the `data/` folder:**
   ```
   Original:  participant_001_data.csv
   Formatted: participant_001_data_FORMATTED.xlsx
   ```

---

## 📂 Excel Workbook Structure

### Sheet 1: Summary
```
┌─────────────────────────────────────┐
│   EXPERIMENT DATA SUMMARY           │
├─────────────────────────────────────┤
│ Participant ID:    001              │
│ Experiment Date:   2024-01-15       │
│ Age:               25               │
│ Gender:            female           │
├─────────────────────────────────────┤
│   PERFORMANCE STATISTICS            │
├──────────────┬────────┬──────┬──────┤
│ Metric       │ Value  │ Min  │ Max  │
├──────────────┼────────┼──────┼──────┤
│ Memory Acc   │ 87.5%  │ 0.00 │ 1.00 │
│ Memory RT    │ 1.234s │ 0.5s │ 3.2s │
│ Parity Acc   │ 92.3%  │ 0.00 │ 1.00 │
│ Total Trials │ 144    │      │      │
├─────────────────────────────────────┤
│   PERFORMANCE BY LOAD CONDITION     │
├──────────┬──────────┬─────────┬─────┤
│ Load     │ Accuracy │ RT(avg) │ Trials│
├──────────┼──────────┼─────────┼──────┤
│ Load 0   │ 91.7%    │ 1.123s  │ 48  │
│ Load 2   │ 88.5%    │ 1.234s  │ 48  │
│ Load 4   │ 83.3%    │ 1.456s  │ 48  │
└──────────┴──────────┴─────────┴─────┘
```

### Sheet 2: Raw Data
All trial-by-trial data with:
- Color-coded accuracy columns
- Centered text
- Alternating row colors
- Frozen header row

---

## 🎨 Color Scheme

| Element | Color | Hex Code |
|---------|-------|----------|
| Header Background | Dark Blue | #1F4788 |
| Header Text | White | #FFFFFF |
| Alternating Rows | Light Gray | #F8F9FA |
| Correct (1) | Light Green | #D4EDDA |
| Incorrect (0) | Light Red | #F8D7DA |
| N/A | Light Yellow | #FFF3CD |
| Summary Header | Green | #28A745 |

---

## 📊 What Gets Formatted

### Automatically Styled Columns:
- ✅ `memory_correct` - Memory test accuracy
- ✅ `parity_correct_1` - Parity digit 1 accuracy
- ✅ `parity_correct_2` - Parity digit 2 accuracy
- ✅ `parity_correct_3` - Parity digit 3 accuracy
- ✅ `parity_correct_4` - Parity digit 4 accuracy

### Calculated Statistics:
- 📊 Memory accuracy (percentage)
- ⏱️ Average reaction times
- 📈 Performance by load condition
- 🎯 Min/Max values for all metrics

---

## 💡 Tips for Best Results

### Before Running:
1. ✅ Install required packages:
   ```bash
   Double-click: INSTALL_DEPENDENCIES.bat
   ```
   Or manually:
   ```bash
   pip install openpyxl pandas
   ```

### After Conversion:
1. 📂 Open the `_FORMATTED.xlsx` file
2. 📊 Check the **Summary** sheet first (overview)
3. 📝 Switch to **Raw Data** sheet for details
4. 🔍 Scroll through data (headers stay frozen!)
5. 🎨 Notice color coding for easy spotting of errors

### For Multiple Participants:
- Run `EXPORT_TO_EXCEL.bat` after collecting all data
- All CSV files will be converted in one go
- Each participant gets their own formatted Excel file

---

## 🔧 Troubleshooting

### Problem: "openpyxl not found"
**Solution:**
```bash
pip install openpyxl
# Or run: INSTALL_DEPENDENCIES.bat
```

### Problem: "Permission denied" when saving
**Solution:**
- Close the Excel file if it's open
- The script cannot overwrite open files

### Problem: Colors not showing
**Solution:**
- Make sure you're opening the `_FORMATTED.xlsx` file (not the CSV)
- CSV files don't support colors

### Problem: "No CSV files found"
**Solution:**
- Run the experiment first to generate data
- CSV files should be in the `data/` folder
- Files must end with `_data.csv`

---

## 📸 Preview

**Before (CSV):**
```
trial_number,memory_correct,memory_rt
1,1,1.234
2,0,2.345
3,1,0.987
```

**After (Excel):**
```
┌─────────────┬────────────────┬────────────┐
│ Trial Number│ Memory Correct │ Memory RT  │ ← Dark blue header
├─────────────┼────────────────┼────────────┤
│      1      │       1        │   1.234    │ ← Green cell (correct)
├─────────────┼────────────────┼────────────┤
│      2      │       0        │   2.345    │ ← Red cell (incorrect)
├─────────────┼────────────────┼────────────┤
│      3      │       1        │   0.987    │ ← Green cell (correct)
└─────────────┴────────────────┴────────────┘
         ↑            ↑              ↑
    Centered    Color-coded    Auto-width
```

---

## 🎯 Benefits

### For Researchers:
- ✅ **Instant visual feedback** on participant performance
- ✅ **No manual formatting** needed
- ✅ **Professional presentation** for reports
- ✅ **Easy error detection** with color coding

### For Data Analysis:
- ✅ **Summary statistics** ready to copy into papers
- ✅ **Performance by condition** pre-calculated
- ✅ **Clean, organized data** for further analysis
- ✅ **Publication-ready tables**

### For Clients:
- ✅ **Professional appearance**
- ✅ **Easy to understand** at a glance
- ✅ **No Excel skills required** to read
- ✅ **Ready to share** with stakeholders

---

## 📝 Notes

- **Original CSV files are NOT deleted** (kept as backup)
- **Excel files can be regenerated** anytime
- **Works with both Experiment 1 and Experiment 2** data
- **Compatible with Excel, Google Sheets, LibreOffice**

---

## ✅ Quick Checklist

- [ ] Install dependencies (`INSTALL_DEPENDENCIES.bat`)
- [ ] Run experiment to generate CSV data
- [ ] Run `EXPORT_TO_EXCEL.bat`
- [ ] Open `_FORMATTED.xlsx` file
- [ ] Check Summary sheet first
- [ ] Enjoy beautiful, professional data! 🎉

---

**Ready to create beautiful Excel reports!** 🚀📊✨
