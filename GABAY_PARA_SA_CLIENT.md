# 📥 GABAY PARA SA CLIENT - PAANO I-DOWNLOAD AT GAMITON

**Kompleto nga giya para sa pag-download kag paggamit sang PsychoPy Experiments**

---

## 📋 TABLE OF CONTENTS

1. [Pag-download sang Files](#1-pag-download-sang-files)
2. [Pag-install sang PsychoPy](#2-pag-install-sang-psychopy)
3. [Pag-install sang Python Packages](#3-pag-install-sang-python-packages)
4. [Paano Mag-run sang Experiment](#4-paano-mag-run-sang-experiment)
5. [Paano Mag-export sang Data sa Excel](#5-paano-mag-export-sang-data-sa-excel)
6. [Kung May Problema](#6-kung-may-problema)

---

## 1️⃣ PAG-DOWNLOAD SANG FILES

### 🌐 **Option A: Download ZIP (PINAKA-EASY)**

1. **Kadto sa GitHub:**
   ```
   https://github.com/Richardd11/PsychoPy-Working-Memory-Experiments
   ```

2. **I-click ang GREEN BUTTON na "Code"**
   - Makita mo sa taas-kamot nga parte sang page

3. **I-click ang "Download ZIP"**
   - Mag-download ini sang tanan nga files (mga 1-2 MB)

4. **I-extract ang ZIP file:**
   - Right-click sa downloaded file
   - Click "Extract All..."
   - Choose location (e.g., Desktop or Documents)
   - Click "Extract"

5. **Open ang folder:**
   ```
   PsychoPy-Working-Memory-Experiments-master/
   ```

✅ **TAPOS! May ara na kamo sang tanan nga files!**

---

### 🔧 **Option B: Clone using Git (For Advanced Users)**

Kung ara kamo Git installed:

```bash
cd Desktop
git clone https://github.com/Richardd11/PsychoPy-Working-Memory-Experiments.git
cd PsychoPy-Working-Memory-Experiments
```

---

## 2️⃣ PAG-INSTALL SANG PSYCHOPY

### 📥 **Download PsychoPy Standalone (RECOMMENDED)**

1. **Kadto sa:**
   ```
   https://www.psychopy.org/download.html
   ```

2. **Choose your operating system:**
   - Windows: Download `.exe` installer
   - Mac: Download `.dmg` file
   - Linux: Follow instructions sa website

3. **I-install ang PsychoPy:**
   - Double-click ang installer
   - Follow ang installation wizard
   - Default settings okay na

4. **I-check kung nag-install:**
   - Search "PsychoPy" sa Start Menu
   - Dapat makita mo ang app

✅ **TAPOS! PsychoPy ready na!**

---

## 3️⃣ PAG-INSTALL SANG PYTHON PACKAGES

Kailangan ta ng special packages para sa Excel export feature.

### 🔧 **Method 1: Auto-Install (PINAKA-EASY)**

1. **Kadto sa folder:**
   ```
   PsychoPy-Working-Memory-Experiments-master/
   ```

2. **Double-click:**
   ```
   INSTALL_DEPENDENCIES.bat
   ```

3. **Mag-install na siya automatically:**
   - openpyxl (for Excel)
   - pandas (for data)
   - matplotlib (for graphs)
   - scipy (for stats)

4. **Hulaton lang ang "Installation complete!"**

✅ **TAPOS! Ready na ang tanan!**

---

### 🔧 **Method 2: Manual Install (kung di nag-work ang bat file)**

Open Command Prompt or PowerShell:

```bash
cd Desktop\PsychoPy-Working-Memory-Experiments-master
pip install -r requirements.txt
```

Or install individually:

```bash
pip install psychopy
pip install pandas
pip install openpyxl
pip install matplotlib
pip install scipy
```

---

## 4️⃣ PAANO MAG-RUN SANG EXPERIMENT

### 🚀 **Method 1: Double-Click (PINAKA-EASY)**

#### **Para sa Experiment 1 (Simultaneous):**

1. **Kadto sa folder:**
   ```
   PsychoPy-Working-Memory-Experiments-master/
   ```

2. **Double-click:**
   ```
   RUN_EXPERIMENT1.bat
   ```

3. **Enter participant info:**
   - Participant ID (e.g., P001)
   - Age
   - Gender
   - Session number

4. **Press OK** - Experiment mag-start na!

#### **Para sa Experiment 2 (Sequential):**

1. **Double-click:**
   ```
   RUN_EXPERIMENT2.bat
   ```

2. **Same process - enter participant info**

✅ **TAPOS! Experiment running na!**

---

### 🔧 **Method 2: Using PsychoPy App**

1. **Open PsychoPy app**

2. **Click "Open" or "File > Open"**

3. **Choose ang experiment file:**
   - `experiment1_simultaneous.py` (Experiment 1)
   - `experiment2_sequential.py` (Experiment 2)

4. **Click ang GREEN RUN BUTTON** (or press Ctrl+R)

5. **Enter participant info**

✅ **TAPOS! Running na!**

---

### 🔧 **Method 3: Using Command Line**

```bash
cd Desktop\PsychoPy-Working-Memory-Experiments-master
python experiment1_simultaneous.py
```

or

```bash
python experiment2_sequential.py
```

---

## 5️⃣ PAANO MAG-EXPORT SANG DATA SA EXCEL

After mag-run ng experiment, may ara CSV files sa `data/` folder.

### 📊 **Convert CSV to Beautiful Excel:**

#### **Step 1: Make sure installed ang packages**
```
(Kung nag-run na kamo ng INSTALL_DEPENDENCIES.bat, okay na ini)
```

#### **Step 2: Run ang Excel converter**

**EASY WAY:**
```
Double-click: EXPORT_TO_EXCEL.bat
```

**Or manually:**
```bash
python export_to_excel.py
```

#### **Step 3: Check ang output**

Kadto sa `data/` folder:

**Before:**
```
P001_Experiment1_Simultaneous_2026_Sep02_1430_data.csv
```

**After:**
```
P001_Experiment1_Simultaneous_2026_Sep02_1430_data_FORMATTED.xlsx
```

✅ **TAPOS! May ara na kamo ng professional Excel file!**

---

### 🎨 **Ano ang Makita Mo sa Excel:**

#### **Sheet 1: Summary**
- Participant information
- Overall accuracy
- Average reaction times
- Performance by load condition
- Statistics summary

#### **Sheet 2: Raw Data**
- All trial data
- Color-coded accuracy:
  - 🟢 **Green** = Correct (1)
  - 🔴 **Red** = Incorrect (0)
  - 🟡 **Yellow** = N/A
- Centered text
- Professional formatting

---

## 6️⃣ KUNG MAY PROBLEMA

### ❌ **Problem: "Python not found"**

**Solution:**
```
Install Python first:
https://www.python.org/downloads/

Or use PsychoPy Standalone (already includes Python)
```

---

### ❌ **Problem: "pip not found"**

**Solution:**
```
1. Open Command Prompt as Administrator
2. Run: python -m ensurepip --upgrade
3. Try again: pip install -r requirements.txt
```

---

### ❌ **Problem: "openpyxl not found"**

**Solution:**
```
pip install openpyxl
```

---

### ❌ **Problem: "Module not found" errors**

**Solution:**
```
Make sure nag-run kamo ng:
INSTALL_DEPENDENCIES.bat

Or manually:
pip install psychopy pandas openpyxl matplotlib scipy
```

---

### ❌ **Problem: Experiment crashes or won't start**

**Solution:**
```
1. Check kung may syntax errors (open sa PsychoPy app)
2. Make sure ara ang conditions/ folder
3. Check kung ara ang CSV files sa conditions/:
   - practice_conditions.csv
   - experiment1_conditions.csv
   - experiment2_conditions.csv
```

---

### ❌ **Problem: "Permission denied" sa Excel export**

**Solution:**
```
1. Close ang Excel file kung bukas
2. Try export ulit
3. Kung persistent pa, right-click > Run as Administrator
```

---

### ❌ **Problem: Data folder not found**

**Solution:**
```
The data/ folder is auto-created when you run experiments.
Kung wala pa gid, create manually:
Right-click > New > Folder > name it "data"
```

---

## 📂 FOLDER STRUCTURE

After ma-download, dapat ini ang makita mo:

```
PsychoPy-Working-Memory-Experiments-master/
│
├── 📄 experiment1_simultaneous.py       ← Experiment 1
├── 📄 experiment2_sequential.py         ← Experiment 2
│
├── 🚀 RUN_EXPERIMENT1.bat               ← I-click para run Exp 1
├── 🚀 RUN_EXPERIMENT2.bat               ← I-click para run Exp 2
│
├── 📊 export_to_excel.py                ← Excel converter
├── 🚀 EXPORT_TO_EXCEL.bat               ← I-click para export
│
├── 🔧 INSTALL_DEPENDENCIES.bat          ← I-click para install packages
├── 📋 requirements.txt                  ← List of packages
│
├── 📁 conditions/                       ← Trial conditions
│   ├── practice_conditions.csv
│   ├── experiment1_conditions.csv
│   └── experiment2_conditions.csv
│
├── 📁 data/                             ← Output folder (auto-created)
│   ├── P001_Experiment1_..._data.csv
│   └── P001_Experiment1_..._data_FORMATTED.xlsx
│
├── 📖 README.md                         ← Main documentation
├── 📖 CLIENT_README.md                  ← Client guide (English)
├── 📖 GABAY_PARA_SA_CLIENT.md          ← This file (Tagalog/Hiligaynon)
├── 📖 EXCEL_EXPORT_GUIDE.md            ← Excel guide
├── 📖 DATA_DICTIONARY.md               ← Variable descriptions
│
├── 🌐 COMPLETE_GUIDE.html              ← Interactive guide
├── 🌐 VISUAL_EXPLANATION.html          ← Visual explainer
└── 🌐 EXCEL_PREVIEW.html               ← Excel preview
```

---

## 🎮 RESPONSE KEYS (REMINDER)

### During Experiment:

| Task | Key | Meaning |
|------|-----|---------|
| **Parity** | F | Odd number |
| | J | Even number |
| **Memory** | S | SAME (all 4 colors identical) |
| | D | DIFFERENT (at least 1 changed) |
| **Thought** | 1-8 | Category number |
| **Navigation** | SPACE | Continue/Next |
| | ESC | Quit experiment |

---

## ✅ QUICK CHECKLIST

Bago mag-start:

- [ ] ✅ Downloaded ang files from GitHub
- [ ] ✅ Extracted ang ZIP file
- [ ] ✅ Installed PsychoPy (or Python)
- [ ] ✅ Ran INSTALL_DEPENDENCIES.bat
- [ ] ✅ Checked kung ara ang conditions/ folder
- [ ] ✅ Ready ang participant

Para mag-run:

- [ ] ✅ Double-click RUN_EXPERIMENT1.bat or RUN_EXPERIMENT2.bat
- [ ] ✅ Enter participant info
- [ ] ✅ Complete ang experiment
- [ ] ✅ Data saved sa data/ folder

Para sa Excel:

- [ ] ✅ Double-click EXPORT_TO_EXCEL.bat
- [ ] ✅ Open ang _FORMATTED.xlsx file
- [ ] ✅ Check Summary sheet
- [ ] ✅ Check Raw Data sheet

---

## 📞 CONTACT / HELP

Kung may problema pa:

1. **Check ang README.md** - Complete English documentation
2. **Open COMPLETE_GUIDE.html** - Interactive guide
3. **Read EXCEL_EXPORT_GUIDE.md** - Excel export details
4. **Check DATA_DICTIONARY.md** - Variable descriptions

---

## 🎯 SUMMARY (PINAKA-IMPORTANT!)

### **Para Mag-start:**

1. **Download** from GitHub (ZIP file)
2. **Extract** ang ZIP
3. **Install PsychoPy** (standalone version)
4. **Run** INSTALL_DEPENDENCIES.bat
5. **Double-click** RUN_EXPERIMENT1.bat or RUN_EXPERIMENT2.bat
6. **Run** EXPORT_TO_EXCEL.bat para sa beautiful Excel files

---

## 💡 TIPS

- ✅ **Backup data regularly** - Copy ang data/ folder
- ✅ **Test first** - Run practice trials before actual data collection
- ✅ **Close other apps** - Para smooth ang experiment
- ✅ **Use fullscreen** - Better experience
- ✅ **Check monitor** - 60Hz refresh rate recommended
- ✅ **Good lighting** - Para makita sang participant ang screen

---

## 🎉 TAPOS NA!

**Ready na kamo mag-collect ng data!** 🚀

Kung may questions pa, check lang ang other documentation files! 📚

---

**Version:** 2.1.0  
**Last Updated:** September 2, 2026  
**Language:** Tagalog/Hiligaynon  
**GitHub:** https://github.com/Richardd11/PsychoPy-Working-Memory-Experiments
