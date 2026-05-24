@echo off
REM ============================================================================
REM                      JUST CLICK AND RUN - SIMPLE!
REM ============================================================================
REM This is the easiest way to run the API - Docker handles everything
REM ============================================================================

color 0A
cls

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║                                                                ║
echo ║             🚀 HTML to PDF API - Docker Launcher              ║
echo ║                                                                ║
echo ║              Just click and let it run! (2-3 min)             ║
echo ║                                                                ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

REM Check if Docker is installed
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    color 0C
    cls
    echo.
    echo ╔════════════════════════════════════════════════════════════════╗
    echo ║                      ❌ DOCKER NOT FOUND                       ║
    echo ╚════════════════════════════════════════════════════════════════╝
    echo.
    echo Docker is not installed or not running.
    echo.
    echo SOLUTION:
    echo 1. Download Docker Desktop from: https://www.docker.com/products/docker-desktop
    echo 2. Install it (takes 5 minutes)
    echo 3. Run this file again
    echo.
    echo Then the API will start automatically!
    echo.
    pause
    exit /b 1
)

echo [✓] Docker found
echo.

REM Check if Docker daemon is running
docker ps >nul 2>&1
if %errorlevel% neq 0 (
    color 0C
    cls
    echo.
    echo ╔════════════════════════════════════════════════════════════════╗
    echo ║                  ❌ DOCKER NOT RUNNING                         ║
    echo ╚════════════════════════════════════════════════════════════════╝
    echo.
    echo Docker is installed but not running.
    echo.
    echo SOLUTION: Start Docker Desktop and run this file again
    echo.
    pause
    exit /b 1
)

echo [✓] Docker is running
echo.

echo [*] Starting API with Docker...
echo     (This takes 1-2 minutes first time, then 10 seconds after)
echo.

REM Build and start
docker-compose up -d

if %errorlevel% neq 0 (
    color 0C
    cls
    echo.
    echo ╔════════════════════════════════════════════════════════════════╗
    echo ║                      ❌ ERROR STARTING                          ║
    echo ╚════════════════════════════════════════════════════════════════╝
    echo.
    echo Failed to start Docker containers.
    echo.
    echo Try: docker-compose down
    echo Then run this file again
    echo.
    pause
    exit /b 1
)

echo.
echo [✓] Docker containers starting...
echo.

REM Wait for service to be ready
echo [*] Waiting for API to be ready (checking health...)
timeout /t 5 /nobreak >nul

setlocal enabledelayedexpansion
set "attempts=0"
:health_check
set /a attempts+=1
if %attempts% gtr 30 (
    echo [WARNING] API took too long to start
    goto open_browser
)

docker exec html-to-pdf-api curl -s http://localhost:5001/health >nul 2>&1
if %errorlevel% neq 0 (
    echo [*] Still starting... (wait %attempts%/30)
    timeout /t 2 /nobreak >nul
    goto health_check
)

:open_browser
echo [✓] API is READY!
echo.

REM Display success banner
color 0A
cls
echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║                                                                ║
echo ║              ✅ API IS RUNNING - READY TO USE!               ║
echo ║                                                                ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

echo 📖 TEST THE API:
echo    Open your browser and go to:
echo.
echo    ► http://localhost:5001/apidocs
echo.
echo    You will see a beautiful interface to test the API!
echo.

echo 🔗 LINKS:
echo    Test API:    http://localhost:5001/apidocs
echo    Health:      http://localhost:5001/health
echo    API Info:    http://localhost:5001/info
echo.

echo 🐳 FOR DOCKER PRODUCTION / n8n:
echo    API Link:    http://localhost:5001/html-to-pdf
echo    (When hosted on Docker: replace localhost with your server IP)
echo.

echo ⏹  TO STOP THE API:
echo    Press Ctrl+C here, or run: docker-compose down
echo.

echo ════════════════════════════════════════════════════════════════
echo.

REM Open browser automatically
start http://localhost:5001/apidocs

REM Keep running and show logs
echo [*] Opening browser and showing logs...
echo.
docker-compose logs -f html-to-pdf-api
