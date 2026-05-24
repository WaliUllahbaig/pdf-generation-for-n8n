# ⚡ IMMEDIATE FIX - WeasyPrint Windows Error

## Your Error
```
OSError: cannot load library 'libgobject-2.0-0': error 0x7e
```

## ✅ Quick Fix (Pick One)

### **EASIEST - Use Docker** (Recommended!)
```bash
docker-compose up -d
```
Then: http://localhost:5001/apidocs

**Why:** No Windows library issues. Works immediately.

---

### **FAST - Run Automatic Fix** (Windows)

**Option A: Batch Script**
1. Open: **Anaconda Prompt** (not regular Command Prompt)
2. Navigate: `cd d:\Raw Projects\PDF generator`
3. Run: `install_windows.bat`
4. Wait 3-5 minutes ⏳
5. Then: `python app.py`

**Option B: PowerShell Script**
1. Open: **PowerShell**
2. Navigate: `cd 'd:\Raw Projects\PDF generator'`
3. Run: `.\install_windows.ps1`
4. Wait 3-5 minutes ⏳
5. Then: `python app.py`

---

### **MANUAL - Use conda-forge**

If scripts don't work, do this manually:

```cmd
# 1. Delete broken environment
conda env remove -n html_to_pdf

# 2. Create with conda-forge (has system libraries)
conda create -n html_to_pdf -c conda-forge python=3.11 pango gdk-pixbuf libffi cairo -y

# 3. Activate
conda activate html_to_pdf

# 4. Install Python packages
pip install -r requirements.txt

# 5. Test
python -c "from weasyprint import HTML; print('✓ Works!')"

# 6. Run
python app.py
```

---

## 🎯 Recommendation

**For you right now:** Use Docker or `install_windows.bat`

Both work without thinking about library dependencies.

---

## 📖 Full Documentation

Read: `WINDOWS_WEASYPRINT_FIX.md`

---

## 🚀 After Fix

Once fixed, start with:
```cmd
run.bat
```

Or:
```bash
python app.py
```

Then: http://localhost:5001/apidocs

✓ Done!
