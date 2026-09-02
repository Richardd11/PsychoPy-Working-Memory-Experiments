# 🎮 FIX: Graphics Card / Shader Errors

## 🚨 Error Messages You're Seeing:

```
ERROR: Shader compilation failed
ERROR: '*' : wrong operand types
ERROR: 'normalize' : function is not known
Fullscreen failed: Shader compilation failed
```

---

## 🎯 **What This Means:**

Your graphics card or drivers have compatibility issues with PsychoPy's advanced graphics features.

**This is NOT a problem with the experiment code!**  
**This is a graphics card/driver issue.**

---

## ✅ **SOLUTION 1: Update Graphics Drivers (BEST FIX)**

### **For Windows:**

#### **Step 1: Identify Your Graphics Card**
1. Press `Windows + R`
2. Type: `dxdiag`
3. Press Enter
4. Go to "Display" tab
5. Note your graphics card name (e.g., "NVIDIA GTX", "AMD Radeon", "Intel HD Graphics")

#### **Step 2: Download Latest Drivers**

**NVIDIA:**
- Go to: https://www.nvidia.com/download/index.aspx
- Select your card model
- Download and install

**AMD:**
- Go to: https://www.amd.com/en/support
- Auto-detect or manually select your card
- Download and install

**Intel:**
- Go to: https://www.intel.com/content/www/us/en/download-center/home.html
- Search for your graphics card
- Download and install

#### **Step 3: Restart Computer**

#### **Step 4: Try Running Experiment Again**
```
Double-click: RUN_EXPERIMENT1.bat
```

---

## ✅ **SOLUTION 2: Use Windowed Mode (Already Implemented!)**

The experiments now automatically fall back to windowed mode if fullscreen fails.

**When you run the experiment:**
1. It tries fullscreen first
2. ❌ Fullscreen fails (shader error)
3. ✅ **Automatically switches to windowed mode**
4. ✅ **Disables problematic graphics features**
5. ✅ **Experiment runs!**

**You don't need to do anything special!** Just run it normally:
```
Double-click: RUN_EXPERIMENT1.bat
```

---

## ✅ **SOLUTION 3: Force Windowed Mode (If Still Having Issues)**

If experiments still crash, manually force windowed mode:

### **Edit the Experiment Files:**

1. Open `experiment1_simultaneous.py` in Notepad
2. Find this line (around line 73):
   ```python
   win = visual.Window([1920, 1080], fullscr=True, ...
   ```
3. Change `fullscr=True` to `fullscr=False`
4. Save and close
5. Try running again

---

## ✅ **SOLUTION 4: Disable Advanced Graphics**

If windowed mode still has issues, add these settings:

### **Edit Window Creation:**

Find the window creation section and modify it:

```python
win = visual.Window(
    size=[1024, 768],  # Smaller size
    fullscr=False, 
    units='height', 
    color=[0,0,0],
    allowGUI=True,
    useFBO=False,      # ← Add this
    useRetina=False,   # ← Add this
    winType='pyglet',  # ← Add this
    allowStencil=False # ← Add this
)
```

---

## ✅ **SOLUTION 5: Use Older OpenGL Version**

Some old graphics cards need older OpenGL:

### **Add to Top of Experiment File:**

```python
# Add these lines BEFORE importing visual
import os
os.environ['PYOPENGL_PLATFORM'] = 'egl'  # Or try 'osmesa'

from psychopy import visual, core, data, event, gui
# ... rest of imports
```

---

## 🔍 **Check Your System:**

### **Minimum Requirements:**
- **OS:** Windows 10 or later
- **Graphics:** OpenGL 2.0+ support
- **RAM:** 4 GB minimum
- **Drivers:** Updated within last 2 years

### **To Check OpenGL Version:**

**Method 1:** Run this in Python:
```python
from pyglet.gl import gl_info
print(gl_info.get_version())
print(gl_info.get_renderer())
```

**Method 2:** Download OpenGL Extensions Viewer
- https://www.realtech-vr.com/home/glview

---

## 🎮 **Common Graphics Card Issues:**

### **Intel HD Graphics (Older)**
- Often has shader compilation issues
- **Fix:** Update Intel graphics drivers
- **Workaround:** Use windowed mode with `useFBO=False`

### **Old NVIDIA/AMD Cards**
- May not support newer shaders
- **Fix:** Update drivers to latest
- **Workaround:** Force older OpenGL version

### **Virtual Machines**
- Limited GPU pass-through
- **Fix:** Run on host machine instead
- **Workaround:** Use software rendering (slower)

### **Remote Desktop / TeamViewer**
- No direct GPU access
- **Fix:** Don't run experiments over remote desktop
- **Workaround:** Not recommended for experiments

---

## 📝 **What the Experiments Now Do Automatically:**

The latest version of the experiments includes:

✅ **Automatic Fallback:**
1. Try fullscreen with advanced graphics
2. If fails → Try windowed mode
3. If fails → Disable FBO (framebuffer objects)
4. If fails → Disable Retina support
5. If fails → Show error and exit gracefully

✅ **Better Error Messages:**
- Clear explanation of what went wrong
- Suggestions for fixes
- Doesn't just crash silently

✅ **Console Output:**
- Shows what it's trying
- Shows what failed
- Shows what worked

---

## 🆘 **Still Not Working?**

### **Option 1: Run on Different Computer**
If your graphics card is very old or doesn't support OpenGL 2.0+, you may need to run on a different machine.

### **Option 2: Use Basic Graphics Mode**
Contact us for a "basic graphics" version that:
- No fancy shaders
- No fullscreen
- Minimal OpenGL requirements
- Works on older hardware

### **Option 3: Update Everything**
1. Update graphics drivers
2. Update Windows
3. Update PsychoPy: `pip install --upgrade psychopy`
4. Restart computer
5. Try again

---

## ✅ **Quick Test:**

To test if your graphics card can run the experiments:

```python
from psychopy import visual, core

# Try creating a simple window
try:
    win = visual.Window([800, 600], fullscr=False, useFBO=False)
    print("SUCCESS: Window created!")
    
    # Try drawing a simple shape
    circle = visual.Circle(win, radius=0.1, fillColor='red')
    circle.draw()
    win.flip()
    core.wait(2)
    
    win.close()
    print("SUCCESS: Graphics working!")
    
except Exception as e:
    print(f"ERROR: {e}")
    print("Your graphics card may need driver updates.")
```

Save this as `test_graphics.py` and run it.

---

## 📊 **Expected Behavior:**

### **With Updated Drivers:**
```
Creating experiment window...
Fullscreen window created successfully
Measuring frame rate...
Ready! Starting experiment...
✅ Experiment runs perfectly
```

### **With Shader Issues (Auto-fixed):**
```
Creating experiment window...
Fullscreen failed: Shader compilation failed
Trying windowed mode without advanced graphics...
Windowed mode created successfully
Measuring frame rate...
Ready! Starting experiment...
✅ Experiment runs in windowed mode
```

### **With Severe Graphics Issues:**
```
Creating experiment window...
Fullscreen failed: Shader compilation failed
Trying windowed mode without advanced graphics...
Window creation failed completely: [error details]

Your graphics card may not support the required features.
Please update your graphics card drivers.

Press Enter to exit...
```

---

## 💡 **Prevention:**

To avoid these issues in the future:

1. ✅ Keep graphics drivers updated
2. ✅ Keep Windows updated
3. ✅ Don't use very old computers (10+ years)
4. ✅ Test on target machine before data collection
5. ✅ Have a backup computer available

---

## 📞 **Need Help?**

If you've tried all solutions and still having issues:

1. **Check your graphics card model:**
   - Windows + R → `dxdiag` → Display tab

2. **Check your OpenGL version:**
   - Run the test script above

3. **Document the error:**
   - Copy the complete error message
   - Note your graphics card model
   - Note your Windows version

4. **Contact for support** with this information

---

**✅ Bottom Line:** Update your graphics drivers, and the experiments will work! The code now handles fallbacks automatically. 🎮
