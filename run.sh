#!/bin/bash

# Start HTML to PDF API - Linux/Mac Shell Script
# This script activates the conda environment and starts the API

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║          HTML to PDF Converter API - Starting...              ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Check if conda is available
if ! command -v conda &> /dev/null; then
    echo "[ERROR] Conda not found!"
    echo ""
    echo "Please install Anaconda or Miniconda:"
    echo "  https://www.anaconda.com/download"
    echo ""
    exit 1
fi

# Activate conda environment
echo "[*] Activating conda environment: html_to_pdf"
# For bash/zsh compatibility
if [ -f "$CONDA_PREFIX/etc/profile.d/conda.sh" ]; then
    source "$CONDA_PREFIX/etc/profile.d/conda.sh"
fi

conda activate html_to_pdf 2>/dev/null
if [ $? -ne 0 ]; then
    echo "[ERROR] Failed to activate environment!"
    echo ""
    echo "Please create it first:"
    echo "  conda create -n html_to_pdf python=3.11 -y"
    echo "  pip install -r requirements.txt"
    echo ""
    exit 1
fi

echo "[✓] Environment activated"
echo ""

# Check if Flask is installed
python -c "import flask" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "[ERROR] Flask not installed!"
    echo "Please run: pip install -r requirements.txt"
    exit 1
fi

echo "[✓] Dependencies found"
echo ""

# Display banner with instructions
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║                    🚀 API IS STARTING...                      ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""
echo "API will be available at: http://localhost:5001"
echo ""
echo "📖 Documentation:"
echo "   - Interactive API Docs: http://localhost:5001/apidocs"
echo "   - Health Check:         http://localhost:5001/health"
echo "   - API Info:             http://localhost:5001/info"
echo ""
echo "🧪 Test the API:"
echo "   curl -X POST http://localhost:5001/html-to-pdf \\"
echo "     -H 'Content-Type: application/json' \\"
echo "     -d '{\"html\": \"<html><body><h1>Test</h1></body></html>\"}' \\"
echo "     --output report.pdf"
echo ""
echo "Press Ctrl+C to stop the API"
echo ""
echo "════════════════════════════════════════════════════════════════"
echo ""

# Start the Flask app
python app.py
