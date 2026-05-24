@echo off
REM Start HTML to PDF API - Windows Batch Script
REM This script activates the conda environment and starts the API

color 0A
cls

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║          HTML to PDF Converter API - Starting...              ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

REM Check if conda is initialized
where conda >nul 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] Conda not found! 
    echo.
    echo Please use Anaconda Prompt instead of regular Command Prompt
    echo OR run: conda init cmd.exe ^(then restart^)
    echo.
    pause
    exit /b 1
)

REM Activate conda environment
echo [*] Activating conda environment: html_to_pdf
call conda activate html_to_pdf 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] Failed to activate environment!
    echo Please run: conda create -n html_to_pdf python=3.11 -y
    echo And then: pip install -r requirements.txt
    pause
    exit /b 1
)

echo [✓] Environment activated
echo.

REM Check if Flask is installed
python -c "import flask" 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] Flask not installed!
    echo Please run: pip install -r requirements.txt
    pause
    exit /b 1
)

echo [✓] Dependencies found
echo.

REM Display banner with instructions
echo ╔════════════════════════════════════════════════════════════════╗
echo ║                    🚀 API IS STARTING...                      ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.
echo API will be available at: http://localhost:5001
echo.
echo 📖 Documentation:
echo    - Interactive API Docs: http://localhost:5001/apidocs
echo    - Health Check:         http://localhost:5001/health
echo    - API Info:             http://localhost:5001/info
echo.
echo 🧪 Test the API:
echo    curl -X POST http://localhost:5001/html-to-pdf ^
echo      -H "Content-Type: application/json" ^
echo      -d "{\"html\": \"^<html^>^<body^>^<h1^>Test^</h1^>^</body^>^</html^>\"}" ^
echo      --output report.pdf
echo.
echo Press Ctrl+C to stop the API
echo.
echo ════════════════════════════════════════════════════════════════
echo.

REM Start the Flask app
python app.py

pause
