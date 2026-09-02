# 🔧 TROUBLESHOOTING: Auto-Close Issue

## 🚨 Problem: Window closes after "Measuring frame rate..."

If the experiment window closes immediately after:
1. You click OK on the participant form
2. You see "Measuring frame rate..." 
3. Window closes without showing the experiment

---

## ✅ **SOLUTIONS** (Try these in order):

### **Solution 1: Use Diagnostic Tools (EASIEST)**

We've added diagnostic batch files to help identify the problem!

#### **Step 1: Test Your Setup**
```
Double-click: TEST_SETUP.bat
```

This will check:
- ✓ Python installed?
- ✓ PsychoPy installed?
- ✓ Required packages installed?
- ✓ Conditions folder exists?
- ✓ All CSV files present?
- ✓ Experiment files exist?

**If it says "ALL CHECKS PASSED!" → Your setup is okay, continue to Solution 2**

**If it shows ERROR → Fix the reported problem first!**

---

#### **Step 2: Run in Debug Mode**
```
Double-click: DEBUG_EXPERIMENT1.bat (or DEBUG_EXPERIMENT2.bat)
```

This will:
- Show ALL error messages
- Keep the console window open
- Help you see what went wrong

**Look for error messages like:**
- "FileNotFoundError" → Conditions file missing
- "ImportError" → Package not installed
- "AttributeError" → PsychoPy version issue

---

### **Solution 2: Check Conditions Files**

The most common cause is missing/corrupt conditions files!

#### **Required Files:**
```
conditions/
├── practice_conditions.csv
├── experiment1_conditions.csv
└── experiment2_conditions.csv
```

#### **Check:**
1. Does the `conditions/` folder exist?
2. Are all 3 CSV files inside?
3. Can you open them in Excel/Notepad?

**If missing:**
- Re-download from GitHub
- Or check if you extracted the ZIP completely

---

### **Solution 3: Install/Reinstall Dependencies**

```
Double-click: INSTALL_DEPENDENCIES.bat
```

Wait for "Installation complete!"

**This installs:**
- psychopy
- pandas
- openpyxl
- matplotlib
- scipy

---

### **Solution 4: Check PsychoPy Version**

Open Command Prompt and run:
```bash
python -c "import psychopy; print(psychopy.__version__)"
```

**Required:** PsychoPy 2023.1.0 or newer

**If too old:**
```bash
pip install --upgrade psychopy
```

---

### **Solution 5: Try Windowed Mode**

If fullscreen fails, the experiments will automatically try windowed mode.

**But if it still crashes:**

Edit the experiment files and change:
```python
# Find this line (around line 73):
win = visual.Window([1920, 1080], fullscr=True, units='height', color=[0,0,0], allowGUI=False)

# Change to:
win = visual.Window([1400, 900], fullscr=False, units='height', color=[0,0,0])
```

---

### **Solution 6: Check for Hidden Errors**

The experiments now have better error handling!

**If there's an error:**
- You'll see a message on screen
- It will tell you what went wrong
- Press SPACE to exit (don't press ESC immediately)

**Common errors:**
1. **"Cannot load conditions file"**
   - Fix: Make sure conditions/ folder exists
   - Re-download files from GitHub

2. **"Module not found"**
   - Fix: Run INSTALL_DEPENDENCIES.bat

3. **"Permission denied"**
   - Fix: Run as Administrator
   - Or move folder out of OneDrive/Dropbox

---

### **Solution 7: Run from Command Prompt (Advanced)**

```bash
cd "C:\Users\...\PsychoPy Replica"
python experiment1_simultaneous.py
```

**This will show ALL error messages in the console!**

---

## 🎯 **Quick Diagnostic Checklist**

Run through this checklist:

- [ ] ✅ TEST_SETUP.bat passes all checks
- [ ] ✅ conditions/ folder exists with 3 CSV files
- [ ] ✅ INSTALL_DEPENDENCIES.bat completed successfully
- [ ] ✅ PsychoPy version 2023.1.0 or newer
- [ ] ✅ Running as Administrator (if needed)
- [ ] ✅ Not running from OneDrive/Dropbox (can cause issues)
- [ ] ✅ Antivirus not blocking Python/PsychoPy

---

## 📊 **What Was Fixed**

We've added the following improvements:

### **1. Better Error Handling**
- Window creation errors are caught and displayed
- Frame rate measurement errors are handled gracefully
- Conditions file loading errors show helpful messages
- All errors display before closing

### **2. Visual Feedback**
- "Measuring frame rate..." message displayed
- "Ready! Starting experiment..." confirmation
- Error messages stay on screen until you press SPACE

### **3. Diagnostic Tools**
- TEST_SETUP.bat - Check your complete setup
- DEBUG_EXPERIMENT1.bat - Run with verbose output
- DEBUG_EXPERIMENT2.bat - Run with verbose output

### **4. Fallback Behavior**
- If fullscreen fails → Try windowed mode
- If window fails → Show error and pause
- If conditions fail → Show error message with details

---

## 🆘 **Still Having Issues?**

### **Step 1: Run Diagnostic**
```
Double-click: TEST_SETUP.bat
```

### **Step 2: Run in Debug**
```
Double-click: DEBUG_EXPERIMENT1.bat
```

### **Step 3: Copy Error Message**
Look for lines starting with:
- `ERROR:`
- `Traceback:`
- `Exception:`

### **Step 4: Common Fixes**

**"FileNotFoundError: conditions/..."**
→ Re-download the complete project from GitHub

**"ImportError: No module named 'psychopy'"**
→ Run: `pip install psychopy`

**"AttributeError: module 'psychopy' has no attribute..."**
→ Update PsychoPy: `pip install --upgrade psychopy`

**"PermissionError: [WinError 32]"**
→ Close any open CSV/Excel files, or run as Administrator

---

## 📝 **For Client/Users**

**If you see auto-close:**

1. **DON'T PANIC!** We have tools to help!

2. **Run TEST_SETUP.bat first**
   - This will tell you exactly what's wrong
   - Follow the instructions it gives you

3. **Then run DEBUG_EXPERIMENT1.bat**
   - This shows detailed error messages
   - Take a screenshot of any errors

4. **Common quick fixes:**
   - Re-download from GitHub
   - Run INSTALL_DEPENDENCIES.bat
   - Make sure conditions/ folder exists
   - Check you're using PsychoPy Standalone

---

## ✅ **Prevention Tips**

To avoid this issue in the future:

1. **Always download the COMPLETE project**
   - Don't just download individual files
   - Use "Download ZIP" from GitHub

2. **Keep files together**
   - Don't move files around
   - Keep conditions/ folder with experiments

3. **Install ALL dependencies**
   - Run INSTALL_DEPENDENCIES.bat once
   - Don't skip this step!

4. **Use the batch files**
   - RUN_EXPERIMENT1.bat (not direct Python)
   - These handle errors better

5. **Test before collecting data**
   - Run TEST_SETUP.bat first
   - Do a practice run
   - Make sure everything works

---

## 🎉 **Success Indicators**

**You'll know it's working when you see:**

1. ✅ Participant form appears
2. ✅ You click OK
3. ✅ "Measuring frame rate..." appears
4. ✅ "Ready! Starting experiment..." appears
5. ✅ Instruction screen shows up
6. ✅ Experiment runs normally

**If you see all 6 steps → SUCCESS!** 🎉

---

**Need more help?** Check:
- GABAY_PARA_SA_CLIENT.md (Tagalog guide)
- GABAY_CLIENT.html (Interactive guide)
- README.md (Main documentation)

**GitHub:** https://github.com/Richardd11/PsychoPy-Working-Memory-Experiments
