@echo off
REM HTML to PDF API - Windows Setup Script
REM This script sets up the conda environment and installs dependencies

echo.
echo ========================================
echo HTML to PDF Converter API - Setup Script
echo ========================================
echo.

REM Initialize conda for this shell session
call conda.bat activate base 2>nul
if errorlevel 1 (
    echo Error: Conda not found in PATH
    echo Please ensure Anaconda/Miniconda is installed and added to PATH
    echo.
    echo Try one of these:
    echo 1. Use Anaconda Prompt instead of regular Command Prompt
    echo 2. Initialize conda with: conda init cmd.exe (then restart)
    echo 3. Use WSL2 with Docker for easier setup
    pause
    exit /b 1
)

echo [✓] Conda is available
echo.

REM Create conda environment
echo Creating conda environment: html_to_pdf
call conda create -n html_to_pdf python=3.11 -y
if errorlevel 1 (
    echo Error: Failed to create conda environment
    pause
    exit /b 1
)

echo [✓] Conda environment created
echo.

REM Activate the environment
echo Activating environment...
call conda activate html_to_pdf
if errorlevel 1 (
    echo Error: Failed to activate environment
    pause
    exit /b 1
)

echo [✓] Environment activated
echo.

REM Install requirements
echo Installing Python dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo Error: Failed to install dependencies
    pause
    exit /b 1
)

echo [✓] Dependencies installed
echo.

echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo To run the API:
echo   1. Open Anaconda Prompt
echo   2. Navigate to: d:\Raw Projects\PDF generator
echo   3. Run: python app.py
echo.
echo API will be available at: http://localhost:5001
echo.
echo Test endpoints:
echo   - Health check: curl http://localhost:5001/health
echo   - Run tests: python test_api.py
echo.
pause
