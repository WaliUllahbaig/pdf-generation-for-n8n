# Windows WeasyPrint Installation Fix - PowerShell
# This script properly installs WeasyPrint with conda-forge dependencies

Write-Host ""
Write-Host "╔════════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║      WeasyPrint Windows Installation Fix (PowerShell)          ║" -ForegroundColor Cyan
Write-Host "║                                                                ║" -ForegroundColor Cyan
Write-Host "║  This script will set up WeasyPrint correctly on Windows      ║" -ForegroundColor Cyan
Write-Host "║  using conda-forge which includes system dependencies         ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# Check if conda is installed
Write-Host "[*] Checking for conda..." -ForegroundColor Yellow
$CondaInit = & conda shell.powershell hook | Out-String
Invoke-Expression $CondaInit

if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] Conda not found!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please install Anaconda from: https://www.anaconda.com/download" -ForegroundColor Yellow
    Write-Host "Or use 'Anaconda Prompt' instead of regular PowerShell" -ForegroundColor Yellow
    Write-Host ""
    pause
    exit 1
}

Write-Host "[✓] Conda found" -ForegroundColor Green
Write-Host ""

# Check if environment exists
Write-Host "[*] Checking for html_to_pdf environment..." -ForegroundColor Yellow
$EnvExists = & conda env list | Select-String "html_to_pdf"

if ($null -eq $EnvExists) {
    Write-Host "[*] Environment not found. Creating new environment..." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "This may take 3-5 minutes on first run..." -ForegroundColor Yellow
    Write-Host ""
    
    & conda create -n html_to_pdf -c conda-forge python=3.11 pango gdk-pixbuf libffi cairo -y
    
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[ERROR] Failed to create environment" -ForegroundColor Red
        pause
        exit 1
    }
    Write-Host "[✓] Environment created" -ForegroundColor Green
} else {
    Write-Host "[✓] Environment already exists" -ForegroundColor Green
}

Write-Host ""

# Activate environment
Write-Host "[*] Activating environment..." -ForegroundColor Yellow
& conda activate html_to_pdf

if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] Failed to activate environment" -ForegroundColor Red
    pause
    exit 1
}

Write-Host "[✓] Environment activated" -ForegroundColor Green
Write-Host ""

# Install Python packages
Write-Host "[*] Installing Python packages..." -ForegroundColor Yellow
Write-Host ""

pip install --upgrade pip setuptools wheel
pip install Flask==3.0.0 Werkzeug==3.0.1 flasgger==0.9.7.1
pip install WeasyPrint==60.1 Pillow==10.1.0 html5lib==1.1 fonttools==4.46.0 pydyf==0.5.0
pip install gunicorn==21.2.0 python-dotenv==1.0.0

if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] Failed to install packages" -ForegroundColor Red
    pause
    exit 1
}

Write-Host ""
Write-Host "[✓] All packages installed successfully!" -ForegroundColor Green
Write-Host ""

# Test WeasyPrint
Write-Host "[*] Testing WeasyPrint installation..." -ForegroundColor Yellow
python -c "from weasyprint import HTML; print('[✓] WeasyPrint works!')"

if ($LASTEXITCODE -ne 0) {
    Write-Host "[WARNING] WeasyPrint test failed" -ForegroundColor Yellow
    Write-Host "Please try running with Docker instead" -ForegroundColor Yellow
    Write-Host "Command: docker-compose up -d" -ForegroundColor Yellow
    pause
    exit 1
}

Write-Host ""
Write-Host "╔════════════════════════════════════════════════════════════════╗" -ForegroundColor Green
Write-Host "║              ✓ Installation Complete!                         ║" -ForegroundColor Green
Write-Host "╚════════════════════════════════════════════════════════════════╝" -ForegroundColor Green
Write-Host ""

Write-Host "You can now run the API:" -ForegroundColor Green
Write-Host ""
Write-Host "  1. Make sure you're in Anaconda Prompt or PowerShell" -ForegroundColor Green
Write-Host "  2. Run: run.bat" -ForegroundColor Green
Write-Host ""
Write-Host "Or manually:" -ForegroundColor Green
Write-Host ""
Write-Host "  conda activate html_to_pdf" -ForegroundColor Green
Write-Host "  python app.py" -ForegroundColor Green
Write-Host ""
Write-Host "Then open: http://localhost:5001/apidocs" -ForegroundColor Green
Write-Host ""

Write-Host "Press any key to exit..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
