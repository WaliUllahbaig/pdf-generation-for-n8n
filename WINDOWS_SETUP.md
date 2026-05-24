# Windows Setup Guide for HTML to PDF API

## Prerequisites Check

Before starting, ensure you have:
- [ ] Windows 10 or Windows 11
- [ ] Anaconda or Miniconda installed
- [ ] Docker Desktop (optional, for Docker setup)

## Method 1: Automated Setup (Easiest)

### Using Batch Script

1. **Open Command Prompt**
   - Press `Win+R`
   - Type `cmd` and press Enter
   - Navigate to project: `cd d:\Raw Projects\PDF generator`

2. **Run setup script**
   ```cmd
   setup.bat
   ```

3. **Follow the prompts** - the script will:
   - Create the conda environment
   - Install all dependencies
   - Provide next steps

### Using PowerShell Script

1. **Open PowerShell**
   - Right-click on your desktop or taskbar
   - Select "Open PowerShell here" or "Open Terminal here"
   - Navigate to project: `cd 'd:\Raw Projects\PDF generator'`

2. **Enable execution policy** (one time)
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

3. **Run setup script**
   ```powershell
   .\setup.ps1
   ```

4. **Follow the prompts**

## Method 2: Manual Setup (More Control)

### Step 1: Open Anaconda Prompt

1. Press `Win+R`
2. Type `Anaconda Prompt` and press Enter
3. This opens a special command prompt with conda initialized

**Important:** Always use "Anaconda Prompt" instead of regular "Command Prompt" when working with conda!

### Step 2: Navigate to Project

```cmd
cd d:\Raw Projects\PDF generator
```

### Step 3: Create Conda Environment

```cmd
conda create -n html_to_pdf python=3.11 -y
```

Wait for this to complete (it will take a few minutes).

### Step 4: Activate Environment

```cmd
conda activate html_to_pdf
```

You should see `(html_to_pdf)` at the beginning of your command line.

### Step 5: Install Dependencies

```cmd
pip install -r requirements.txt
```

This will take 5-10 minutes. You'll see lots of download progress messages.

### Step 6: Verify Installation

```cmd
python -c "import flask; import weasyprint; print('✓ All dependencies installed successfully!')"
```

If you see the checkmark message, you're ready!

## Running the API

### Local Development

1. **Open Anaconda Prompt**

2. **Navigate to project**
   ```cmd
   cd d:\Raw Projects\PDF generator
   ```

3. **Activate environment**
   ```cmd
   conda activate html_to_pdf
   ```

4. **Start the API**
   ```cmd
   python app.py
   ```

   You should see:
   ```
   ================================================================================
   Starting HTML to PDF Converter API
   ================================================================================
   Server running on http://0.0.0.0:5001
   ...
   ```

5. **API is now running!** Leave this window open.

### Testing the API (New Terminal)

1. **Open another Anaconda Prompt**

2. **Navigate to project**
   ```cmd
   cd d:\Raw Projects\PDF generator
   ```

3. **Run the test suite**
   ```cmd
   python test_api.py
   ```

   Or use curl to test manually:

   ```cmd
   curl -X POST http://localhost:5001/html-to-pdf -H "Content-Type: application/json" -d "{\"html\": \"<html><body><h1>Test</h1></body></html>\"}" --output report.pdf
   ```

4. **Check the results**
   - If test passed, you'll see "All tests passed" message
   - PDF files will be generated in `test_output/` folder

### Stop the API

In the terminal where the API is running, press `Ctrl+C`

## Method 3: Docker Setup (Recommended for Production)

### Prerequisites
- Docker Desktop for Windows installed
- Docker running

### Running

1. **Open Command Prompt or PowerShell**

2. **Navigate to project**
   ```cmd
   cd d:\Raw Projects\PDF generator
   ```

3. **Start with Docker Compose**
   ```cmd
   docker-compose up -d
   ```

4. **Verify it's running**
   ```cmd
   curl http://localhost:5001/health
   ```

5. **Check logs**
   ```cmd
   docker-compose logs -f html-to-pdf-api
   ```

### Stop

```cmd
docker-compose down
```

## Troubleshooting

### Problem: "Anaconda Prompt not found"

**Solution:** Anaconda is not installed or not in PATH

1. Install Anaconda from: https://www.anaconda.com/download
2. During installation, check "Add Anaconda to PATH"
3. Restart your computer
4. Try again

### Problem: "conda: The term 'conda' is not recognized"

**Solution:** Using regular Command Prompt instead of Anaconda Prompt

1. Press `Win+R`
2. Type `anaconda` (or search for it)
3. Click "Anaconda Prompt"
4. Now conda commands will work

### Problem: "Module not found" when running app

**Solution:** Dependencies not installed correctly

1. Activate environment: `conda activate html_to_pdf`
2. Reinstall: `pip install -r requirements.txt`
3. Try again

### Problem: "Port 5001 is already in use"

**Solution:** Something else is using port 5001

1. Change port in `app.py`: Find `port=5001` and change to `port=5002`
2. Or find and stop the program using port 5001:
   ```cmd
   netstat -ano | findstr :5001
   taskkill /PID <PID> /F
   ```

### Problem: "SSL: CERTIFICATE_VERIFY_FAILED" when installing

**Solution:** Firewall or SSL issue

Try:
```cmd
pip install --trusted-host pypi.python.org -r requirements.txt
```

Or use Docker instead (avoids this issue).

### Problem: Installation is very slow

**Solution:** Network issue or pip server is slow

1. Use pip's faster mirror:
   ```cmd
   pip install -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt
   ```

2. Or just wait - it can take 10-15 minutes on first install

### Problem: Test script says "Cannot connect to http://localhost:5001"

**Solution:** API is not running

1. Make sure you started the API with `python app.py`
2. Leave that window open
3. Run tests in a different terminal
4. Make sure the API shows "Server running on http://0.0.0.0:5001"

## Quick Reference

### Conda Commands

```cmd
# List all environments
conda env list

# Activate environment
conda activate html_to_pdf

# Deactivate environment
conda deactivate

# Delete environment (if needed)
conda env remove -n html_to_pdf

# Create fresh environment
conda create -n html_to_pdf python=3.11 -y
```

### Project Commands

```cmd
# Run the API locally
python app.py

# Run tests
python test_api.py

# Check health
curl http://localhost:5001/health

# Get API info
curl http://localhost:5001/info

# Docker start
docker-compose up -d

# Docker stop
docker-compose down

# Docker logs
docker-compose logs -f
```

## Next Steps

1. ✅ Environment set up
2. ✅ API running
3. ✅ Tests passing

Now you can:
- Read [README.md](README.md) for full documentation
- Check [QUICKSTART.md](QUICKSTART.md) for quick reference
- Review [app.py](app.py) to understand the code
- Deploy to production using Docker

## Production Deployment

For production, use Docker Compose:

```cmd
docker-compose up -d
```

This provides:
- ✓ Consistent environment
- ✓ Easy scaling
- ✓ Health checks
- ✓ Resource limits
- ✓ Logging
- ✓ Automatic restart

## Getting Help

If you encounter issues:
1. Check [README.md](README.md) Troubleshooting section
2. Review the error message carefully
3. Try the Docker method if local setup fails
4. Ensure all prerequisites are installed

## Verification Checklist

After setup, verify:
- [ ] Conda environment created: `conda info --envs | findstr html_to_pdf`
- [ ] Environment activated: Command prompt shows `(html_to_pdf)`
- [ ] Dependencies installed: `pip list | findstr Flask`
- [ ] API starts: `python app.py` shows "Server running"
- [ ] Health check works: `curl http://localhost:5001/health`
- [ ] Tests pass: `python test_api.py`

All checks passing? You're ready to go! 🎉
