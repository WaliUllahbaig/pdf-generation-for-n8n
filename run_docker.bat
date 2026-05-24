@echo off
REM Start HTML to PDF API with Docker Compose - Windows
REM This script builds and starts the API in Docker

color 0A
cls

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║       HTML to PDF Converter API - Docker Startup              ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

REM Check if Docker is installed
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Docker is not installed or not in PATH!
    echo.
    echo Please install Docker Desktop from:
    echo   https://www.docker.com/products/docker-desktop
    echo.
    pause
    exit /b 1
)

echo [✓] Docker found
echo.

REM Check if Docker daemon is running
docker ps >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Docker daemon is not running!
    echo.
    echo Please start Docker Desktop
    echo.
    pause
    exit /b 1
)

echo [✓] Docker daemon is running
echo.

REM Build Docker image
echo [*] Building Docker image...
docker-compose build

if %errorlevel% neq 0 (
    echo [ERROR] Docker build failed!
    pause
    exit /b 1
)

echo [✓] Docker image built successfully
echo.

REM Start containers
echo [*] Starting Docker containers...
docker-compose up -d

if %errorlevel% neq 0 (
    echo [ERROR] Docker containers failed to start!
    pause
    exit /b 1
)

echo [✓] Docker containers started successfully
echo.

REM Wait for service to be ready
echo [*] Waiting for API to be ready...
timeout /t 3 /nobreak >nul

REM Check health
:health_check
docker exec html-to-pdf-api curl -s http://localhost:5001/health >nul 2>&1
if %errorlevel% neq 0 (
    echo [*] Waiting for service to be ready...
    timeout /t 2 /nobreak >nul
    goto health_check
)

echo [✓] API is ready!
echo.

REM Display banner with instructions
echo ╔════════════════════════════════════════════════════════════════╗
echo ║              🚀 API IS RUNNING IN DOCKER!                     ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.
echo API is available at: http://localhost:5001
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
echo 📋 Useful commands:
echo    - View logs:        docker-compose logs -f
echo    - Stop API:         docker-compose down
echo    - Stop and remove:  docker-compose down -v
echo.
echo ════════════════════════════════════════════════════════════════
echo.
echo [*] Press any key to view logs (Ctrl+C to exit)...
pause

docker-compose logs -f html-to-pdf-api
