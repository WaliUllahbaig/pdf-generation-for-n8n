@echo off
REM Windows WeasyPrint Installation Fix
REM This script properly installs WeasyPrint with conda-forge dependencies

color 0A
cls

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║      WeasyPrint Windows Installation Fix                      ║
echo ║                                                                ║
echo ║  This script will set up WeasyPrint correctly on Windows      ║
echo ║  using conda-forge which includes system dependencies         ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

REM Check if conda is installed
where conda >nul 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] Conda not found!
    echo.
    echo Please use Anaconda Prompt instead of regular Command Prompt
    echo OR install Anaconda from: https://www.anaconda.com/download
    echo.
    pause
    exit /b 1
)

echo [✓] Conda found
echo.

REM Check if environment exists
echo [*] Checking for html_to_pdf environment...
call conda env list | findstr "html_to_pdf" >nul
if %errorlevel% neq 0 (
    echo [*] Environment not found. Creating new environment...
    echo.
    echo This may take 3-5 minutes on first run...
    echo.
    call conda create -n html_to_pdf -c conda-forge python=3.11 pango gdk-pixbuf libffi cairo -y
    if %errorlevel% neq 0 (
        echo [ERROR] Failed to create environment
        pause
        exit /b 1
    )
    echo [✓] Environment created
) else (
    echo [✓] Environment already exists
)

echo.

REM Activate environment
echo [*] Activating environment...
call conda activate html_to_pdf
if %errorlevel% neq 0 (
    echo [ERROR] Failed to activate environment
    pause
    exit /b 1
)

echo [✓] Environment activated
echo.

REM Install Python packages
echo [*] Installing Python packages...
echo.
pip install --upgrade pip setuptools wheel
pip install Flask==3.0.0 Werkzeug==3.0.1 flasgger==0.9.7.1
pip install WeasyPrint==60.1 Pillow==10.1.0 html5lib==1.1 fonttools==4.46.0 pydyf==0.5.0
pip install gunicorn==21.2.0 python-dotenv==1.0.0

if %errorlevel% neq 0 (
    echo [ERROR] Failed to install packages
    pause
    exit /b 1
)

echo.
echo [✓] All packages installed successfully!
echo.

REM Test WeasyPrint
echo [*] Testing WeasyPrint installation...
python -c "from weasyprint import HTML; print('[✓] WeasyPrint works!')"
if %errorlevel% neq 0 (
    echo [WARNING] WeasyPrint test failed
    echo Please try running with Docker instead
    echo Command: docker-compose up -d
    pause
    exit /b 1
)

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║              ✓ Installation Complete!                         ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.
echo You can now run the API:
echo.
echo   1. Make sure you're in Anaconda Prompt
echo   2. Run: run.bat
echo.
echo Or manually:
echo.
echo   conda activate html_to_pdf
echo   python app.py
echo.
echo Then open: http://localhost:5001/apidocs
echo.
pause
