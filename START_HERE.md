# 🚀 START HERE - First Time Setup Guide

**Welcome! Follow these steps in order. Don't skip any step!**

---

## ⚠️ **IMPORTANT: What You Need to Download**

Your download from GitHub **ONLY includes the experiment code**.

You still need to install:
1. ✅ **PsychoPy** (the software that runs experiments)
2. ✅ **Python packages** (for Excel export and analysis)

**Don't worry! We'll guide you through everything below. 👇**

---

## 📋 **COMPLETE SETUP CHECKLIST**

Follow these steps **IN ORDER**:

---

### **STEP 1: Download the Codebase** ✅ (You probably did this already!)

1. Go to GitHub:
   ```
   https://github.com/Richardd11/PsychoPy-Working-Memory-Experiments
   ```

2. Click the **GREEN button** that says **"Code"**

3. Click **"Download ZIP"**

4. **Extract the ZIP file:**
   - Right-click the downloaded ZIP
   - Choose "Extract All..."
   - Pick a location (e.g., Desktop or Documents)
   - Click "Extract"

5. You should now have a folder:
   ```
   PsychoPy-Working-Memory-Experiments-master/
   ```

**✅ STEP 1 COMPLETE!** You now have the code.

---

### **STEP 2: Install PsychoPy** ❌ (Need to download separately!)

**Why?** PsychoPy is the software that runs psychology experiments. It's NOT included in the GitHub download.

**Size:** ~500 MB (takes 5-10 minutes to download and install)

#### **How to Install:**

1. **Go to the official PsychoPy website:**
   ```
   https://www.psychopy.org/download.html
   ```

2. **Download the "Standalone" version for your system:**
   - **Windows:** Download `.exe` file
   - **Mac:** Download `.dmg` file
   - **Linux:** Follow instructions on website

3. **Run the installer:**
   - Double-click the downloaded file
   - Follow the installation wizard
   - Use **default settings** (just click "Next")
   - Wait for installation to complete (5-10 minutes)

4. **Verify it installed:**
   - Search "PsychoPy" in your Start Menu
   - You should see the PsychoPy app
   - **Don't open it yet!** We'll use batch files instead.

**✅ STEP 2 COMPLETE!** PsychoPy is installed.

---

### **STEP 3: Install Python Packages** ❌ (Need to download!)

**Why?** The experiments need special packages for:
- Excel export (openpyxl)
- Data processing (pandas)
- Statistics (scipy)
- Graphs (matplotlib)

**Size:** ~50-100 MB total

**Time:** 2-5 minutes

#### **EASY METHOD (Recommended):**

1. **Go to your extracted folder:**
   ```
   PsychoPy-Working-Memory-Experiments-master/
   ```

2. **Double-click this file:**
   ```
   INSTALL_DEPENDENCIES.bat
   ```

3. **Wait for it to finish:**
   - You'll see packages being downloaded and installed
   - Wait until you see: **"Installation complete!"**
   - **DO NOT CLOSE THE WINDOW** until it says "Press any key to continue"

4. **Press any key to close**

**✅ STEP 3 COMPLETE!** All packages installed.

---

### **STEP 4: Verify Everything Works** ✅

Let's make sure everything is set up correctly!

1. **Go to your extracted folder:**
   ```
   PsychoPy-Working-Memory-Experiments-master/
   ```

2. **Double-click this file:**
   ```
   TEST_SETUP.bat
   ```

3. **Wait for the checks:**
   - [1/5] Checking Python...
   - [2/5] Checking PsychoPy...
   - [3/5] Checking required packages...
   - [4/5] Checking conditions folder...
   - [5/5] Checking experiment files...

4. **Look for this message:**
   ```
   ===============================================
   ALL CHECKS PASSED!
   ===============================================
   ```

**✅ If you see "ALL CHECKS PASSED!" → You're ready to run experiments!**

**❌ If you see any ERROR messages:**
- Read the error carefully
- Follow the instructions it gives you
- Common issues:
  - Python not found → Install PsychoPy Standalone
  - Packages missing → Run INSTALL_DEPENDENCIES.bat again
  - Files missing → Re-download and extract ZIP completely

---

### **STEP 5: Run Your First Experiment!** 🎉

Now you're ready!

1. **Go to your folder:**
   ```
   PsychoPy-Working-Memory-Experiments-master/
   ```

2. **Choose an experiment:**
   - **Double-click:** `RUN_EXPERIMENT1.bat` (Simultaneous)
   - **OR Double-click:** `RUN_EXPERIMENT2.bat` (Sequential)

3. **Enter participant information:**
   - Participant ID: (e.g., `P001`)
   - Age: (e.g., `25`)
   - Gender: Choose from dropdown
   - Session: (e.g., `001`)

4. **Click OK**

5. **Follow on-screen instructions!**

**✅ CONGRATULATIONS! Your first experiment is running!** 🎊

---

## 🔄 **WHAT YOU DON'T NEED TO DOWNLOAD**

✅ Already included in the GitHub download:
- ✅ Experiment code (Python files)
- ✅ Conditions files (CSV files)
- ✅ Documentation
- ✅ Batch file launchers
- ✅ Excel export scripts

❌ Need to download separately:
- ❌ PsychoPy software (~500 MB)
- ❌ Python packages (~50-100 MB)

---

## 📊 **After Running Experiments: Export to Excel**

Your data is saved as CSV files. Want them in beautiful Excel format?

1. **Make sure experiments have run** (you have CSV files in `data/` folder)

2. **Double-click:**
   ```
   EXPORT_TO_EXCEL.bat
   ```

3. **Wait for conversion** (1-2 seconds per file)

4. **Check the `data/` folder:**
   - Original: `P001_..._data.csv`
   - **NEW:** `P001_..._data_FORMATTED.xlsx` ← Open this!

5. **Open the Excel file:**
   - **Sheet 1 (Summary):** Statistics and performance overview
   - **Sheet 2 (Raw Data):** All trial data with color coding

---

## ⏱️ **Total Time Required**

| Step | Time | Downloads |
|------|------|-----------|
| Download codebase | 1 min | ~2 MB |
| Install PsychoPy | 10 min | ~500 MB |
| Install packages | 5 min | ~100 MB |
| Verify setup | 1 min | - |
| **TOTAL** | **~17 min** | **~600 MB** |

**Internet required:** YES (for downloading PsychoPy and packages)  
**After setup:** Can run offline

---

## 🆘 **Troubleshooting**

### **Problem: "Python not found"**
**Solution:** Install PsychoPy Standalone (it includes Python)

### **Problem: "PsychoPy not installed"**
**Solution:** Go to https://www.psychopy.org/download.html and install

### **Problem: "Packages missing"**
**Solution:** Run `INSTALL_DEPENDENCIES.bat` again

### **Problem: Window closes immediately**
**Solution:** Run `DEBUG_EXPERIMENT1.bat` to see error messages

### **Problem: "File not found"**
**Solution:** Make sure you extracted the ZIP file completely

### **Problem: Can't install packages**
**Solution:** Run Command Prompt as Administrator, then:
```bash
cd "path\to\PsychoPy-Working-Memory-Experiments-master"
pip install -r requirements.txt
```

---

## 📚 **More Help**

After setup, check these guides:

- **GABAY_CLIENT.html** - Interactive guide (open in browser)
- **GABAY_PARA_SA_CLIENT.md** - Tagalog/Hiligaynon guide
- **README.md** - Main documentation (English)
- **TROUBLESHOOTING_AUTOCLOSE.md** - If window closes too fast
- **EXCEL_EXPORT_GUIDE.md** - Excel export instructions

---

## ✅ **Quick Reference - What to Run**

After setup is complete, you'll use these files:

| File | Purpose |
|------|---------|
| `RUN_EXPERIMENT1.bat` | Run Experiment 1 (Simultaneous) |
| `RUN_EXPERIMENT2.bat` | Run Experiment 2 (Sequential) |
| `EXPORT_TO_EXCEL.bat` | Convert CSV to formatted Excel |
| `TEST_SETUP.bat` | Check if everything is installed correctly |
| `DEBUG_EXPERIMENT1.bat` | Run Exp 1 with error messages |
| `DEBUG_EXPERIMENT2.bat` | Run Exp 2 with error messages |

---

## 🎯 **Success Checklist**

You'll know setup is complete when:

- [x] ✅ Folder extracted from ZIP
- [x] ✅ PsychoPy installed and appears in Start Menu
- [x] ✅ `INSTALL_DEPENDENCIES.bat` completed successfully
- [x] ✅ `TEST_SETUP.bat` shows "ALL CHECKS PASSED!"
- [x] ✅ Can launch experiment and see participant form
- [x] ✅ Experiment runs without closing immediately

**If all checked ✅ → You're ready to collect data!** 🎉

---

## 💡 **Tips**

1. **Run TEST_SETUP.bat first** - It checks everything!
2. **Keep files together** - Don't move files out of the main folder
3. **Backup data folder** - Copy `data/` folder regularly
4. **Use batch files** - Don't run `.py` files directly
5. **Close other apps** - For smooth experiment performance

---

**Need help?** Open `GABAY_CLIENT.html` in your browser for an interactive guide!

**GitHub:** https://github.com/Richardd11/PsychoPy-Working-Memory-Experiments

---

**🎉 You're all set! Good luck with your experiments!** 🚀
