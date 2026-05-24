# HTML to PDF API - Windows PowerShell Setup Script
# This script sets up the conda environment and installs dependencies

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "HTML to PDF Converter API - Setup Script" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Initialize conda
Write-Host "Initializing conda..."
$CondaInit = & conda shell.powershell hook | Out-String
Invoke-Expression $CondaInit

if ($LASTEXITCODE -ne 0) {
    Write-Host "Error: Conda not found or failed to initialize" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please ensure Anaconda/Miniconda is installed." -ForegroundColor Yellow
    Write-Host "Try one of these:" -ForegroundColor Yellow
    Write-Host "  1. Use 'Anaconda Prompt' instead of PowerShell" -ForegroundColor Yellow
    Write-Host "  2. Initialize conda with: conda init powershell (then restart)" -ForegroundColor Yellow
    Write-Host "  3. Use WSL2 with Docker for easier setup" -ForegroundColor Yellow
    pause
    exit 1
}

Write-Host "[✓] Conda is available" -ForegroundColor Green
Write-Host ""

# Create conda environment
Write-Host "Creating conda environment: html_to_pdf..."
& conda create -n html_to_pdf python=3.11 -y

if ($LASTEXITCODE -ne 0) {
    Write-Host "Error: Failed to create conda environment" -ForegroundColor Red
    pause
    exit 1
}

Write-Host "[✓] Conda environment created" -ForegroundColor Green
Write-Host ""

# Activate the environment
Write-Host "Activating environment..."
& conda activate html_to_pdf

if ($LASTEXITCODE -ne 0) {
    Write-Host "Error: Failed to activate environment" -ForegroundColor Red
    pause
    exit 1
}

Write-Host "[✓] Environment activated" -ForegroundColor Green
Write-Host ""

# Install requirements
Write-Host "Installing Python dependencies..."
Write-Host "This may take several minutes on first run..." -ForegroundColor Yellow
Write-Host ""

& pip install -r requirements.txt

if ($LASTEXITCODE -ne 0) {
    Write-Host "Error: Failed to install dependencies" -ForegroundColor Red
    Write-Host ""
    Write-Host "Try running this command manually:" -ForegroundColor Yellow
    Write-Host "  pip install -r requirements.txt" -ForegroundColor Yellow
    pause
    exit 1
}

Write-Host ""
Write-Host "[✓] Dependencies installed" -ForegroundColor Green
Write-Host ""

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Setup Complete!" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "To run the API:" -ForegroundColor Green
Write-Host "  1. Open 'Anaconda Prompt'" -ForegroundColor Green
Write-Host "  2. Navigate to: d:\Raw Projects\PDF generator" -ForegroundColor Green
Write-Host "  3. Activate environment: conda activate html_to_pdf" -ForegroundColor Green
Write-Host "  4. Run: python app.py" -ForegroundColor Green
Write-Host ""

Write-Host "API will be available at: http://localhost:5001" -ForegroundColor Green
Write-Host ""

Write-Host "Test endpoints:" -ForegroundColor Green
Write-Host "  - Health check: curl http://localhost:5001/health" -ForegroundColor Green
Write-Host "  - Run tests: python test_api.py" -ForegroundColor Green
Write-Host ""

Write-Host "Press any key to exit..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
