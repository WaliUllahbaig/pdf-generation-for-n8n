# 🔧 Windows WeasyPrint Fix Guide

## Problem
You're getting this error on Windows:
```
OSError: cannot load library 'libgobject-2.0-0': error 0x7e
```

This happens because WeasyPrint needs system libraries (GObject, Pango, etc.) that aren't available on Windows.

---

## ✅ Solution 1: Use the Windows Installation Script (EASIEST)

### Step 1: Use Anaconda Prompt
- Press `Win+R` → Type "Anaconda Prompt" → Press Enter
- This is important! NOT regular Command Prompt

### Step 2: Navigate to project
```cmd
cd d:\Raw Projects\PDF generator
```

### Step 3: Run the fix script
```cmd
install_windows.bat
```

This script will:
- ✅ Create environment with conda-forge dependencies
- ✅ Install all system libraries (pango, gdk-pixbuf, etc.)
- ✅ Install WeasyPrint correctly
- ✅ Test the installation
- ✅ Show success message

**Time: 3-5 minutes**

---

## ✅ Solution 2: Manual conda-forge Installation

### Step 1: Delete the broken environment
```cmd
conda env remove -n html_to_pdf
```

### Step 2: Create new environment with conda-forge
```cmd
conda create -n html_to_pdf -c conda-forge python=3.11 pango gdk-pixbuf libffi cairo -y
```

### Step 3: Activate environment
```cmd
conda activate html_to_pdf
```

### Step 4: Install Python packages
```cmd
pip install -r requirements.txt
```

### Step 5: Test
```cmd
python -c "from weasyprint import HTML; print('✓ Works!')"
```

---

## ✅ Solution 3: Use Docker (Recommended for Production)

If conda-forge installation doesn't work, Docker is the easiest alternative:

### Step 1: Make sure Docker is running
- Start Docker Desktop

### Step 2: Run with Docker
```cmd
docker-compose up -d
```

### Step 3: Access API
```
http://localhost:5001/apidocs
```

**No Windows dependencies needed!** ✓

---

## ✅ Solution 4: Using environment.yml

The project now includes `environment.yml` with all dependencies pre-configured:

### Step 1: Delete old environment
```cmd
conda env remove -n html_to_pdf
```

### Step 2: Create from environment file
```cmd
conda env create -f environment.yml
```

### Step 3: Activate
```cmd
conda activate html_to_pdf
```

### Step 4: Run
```cmd
python app.py
```

---

## 🚀 Quick Decision Tree

### I want the easiest solution on Windows:
→ Use **Docker**: `docker-compose up -d`

### I want local Python but with automatic fix:
→ Run **install_windows.bat**

### I'm comfortable with manual commands:
→ Follow **Solution 2: Manual conda-forge**

### I have conda and want pre-configured setup:
→ Use **environment.yml**: `conda env create -f environment.yml`

---

## 📋 What Was Wrong

**Old setup (doesn't work on Windows):**
```bash
conda create -n html_to_pdf python=3.11 -y
pip install weasyprint
# ❌ Missing system libraries!
```

**New setup (works on Windows):**
```bash
conda create -n html_to_pdf -c conda-forge python=3.11 pango gdk-pixbuf libffi cairo -y
pip install weasyprint
# ✅ All system libraries included!
```

The difference: Using `conda-forge` channel includes pre-built system libraries.

---

## 🐳 Why Docker Works Better

Docker automatically installs:
- ✅ Python
- ✅ Pango, GdkPixbuf, Cairo
- ✅ System fonts
- ✅ All dependencies
- ✅ Clean environment

No Windows dependency issues!

---

## 📖 Updated Setup Guide

### For Windows Users: Recommended Order

1. **Try Docker first** (easiest, most reliable)
   ```cmd
   docker-compose up -d
   ```

2. **If Docker doesn't work, use automatic fix**
   ```cmd
   install_windows.bat
   ```

3. **If that fails, use environment.yml**
   ```cmd
   conda env create -f environment.yml
   ```

4. **Last resort: manual conda-forge**
   ```cmd
   conda create -n html_to_pdf -c conda-forge python=3.11 pango gdk-pixbuf libffi cairo -y
   pip install -r requirements.txt
   ```

---

## ✅ Verify Installation

After setup, test with:

```cmd
# Test 1: Python import
python -c "from weasyprint import HTML; print('✓ WeasyPrint works!')"

# Test 2: Start API
python app.py
# Should show: "Server running on http://0.0.0.0:5001"

# Test 3: Open browser
# http://localhost:5001/apidocs
```

All three should work!

---

## 🆘 Still Having Issues?

### Error: "libgobject-2.0-0 not found"
- Use **Docker** (simplest solution)
- Or run `install_windows.bat`

### Error: "Pango not found"
- Run `conda install -c conda-forge pango -y`

### Error: "Failed to load dynamic library"
- Delete environment: `conda env remove -n html_to_pdf`
- Run `install_windows.bat`

### Error: "Can't find cairo"
- Run: `conda install -c conda-forge cairo -y`

### Multiple errors:
- **Use Docker!** `docker-compose up -d`

---

## 📊 Summary of Files

| File | Purpose |
|------|---------|
| environment.yml | Pre-configured conda environment |
| install_windows.bat | Automatic Windows setup |
| run.bat | Quick start (Windows) |
| run_docker.bat | Docker start (Windows) |

---

## 🎯 Recommended Quick Start Now

### Windows Users:

**Option 1: Docker (Most Reliable)**
```cmd
docker-compose up -d
```

**Option 2: Automatic Fix**
```cmd
install_windows.bat
```

Then in either case:
```cmd
python app.py
```

Open: http://localhost:5001/apidocs

---

## 💡 Why This Happens

WeasyPrint needs:
- Pango (text rendering)
- GdkPixbuf (image handling)
- Cairo (drawing)
- GObject (bindings)
- libffi (C bindings)

On Linux/Mac: These are system packages (apt-get, brew)
On Windows: Not available natively
**Solution:** Docker or conda-forge

---

## ✨ Next Steps

1. Choose your solution (Docker is easiest)
2. Run the setup
3. Start the API
4. Open http://localhost:5001/apidocs
5. Test in Swagger UI

---

**Most people succeed with Docker or install_windows.bat!** 🚀
