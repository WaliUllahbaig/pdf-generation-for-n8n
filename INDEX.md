# 🚀 HTML to PDF Converter API

Welcome! This is a **production-grade REST API** that converts HTML strings to PDF files.

## ✨ What You Have

A complete, enterprise-ready project with:
- ✅ Production-grade Flask API with comprehensive error handling
- ✅ Intelligent exception handling and recovery
- ✅ Advanced logging and monitoring
- ✅ Docker support with optimized images
- ✅ Complete test suite included
- ✅ Comprehensive documentation
- ✅ Multiple setup options (Local, Docker, Automated)

## 🎯 Start Here

Choose your path:

### 👤 **I want to get started quickly**
→ Read: [QUICKSTART.md](QUICKSTART.md) (5 minutes)

### 🪟 **I'm on Windows and need help**
→ Read: [WINDOWS_SETUP.md](WINDOWS_SETUP.md)
→ Run: `setup.bat` or `.\setup.ps1` (automated setup)

### 🐳 **I want to use Docker (recommended for production)**
→ Run: `docker-compose up -d`
→ Test: `curl http://localhost:5001/health`

### 📖 **I want to understand everything**
→ Read: [README.md](README.md) (comprehensive guide)

### 🏗️ **I want to see the project structure**
→ Read: [PROJECT_INVENTORY.md](PROJECT_INVENTORY.md)

## 📋 Files Overview

| File | Purpose | Lines |
|------|---------|-------|
| **app.py** | Main Flask API (core logic) | 720+ |
| **requirements.txt** | Python dependencies | 13 |
| **Dockerfile** | Docker image specification | 65 |
| **docker-compose.yml** | Docker orchestration | 45 |
| **test_api.py** | Test suite with 10 test cases | 500+ |
| **README.md** | Full documentation | 500+ |
| **QUICKSTART.md** | Quick start guide | 80 |
| **WINDOWS_SETUP.md** | Windows-specific guide | 400+ |
| **PROJECT_INVENTORY.md** | Architecture & inventory | 500+ |
| **setup.bat** | Automated Windows setup (batch) | 60 |
| **setup.ps1** | Automated Windows setup (PowerShell) | 80 |
| **.env.example** | Environment variables template | 15 |
| **.gitignore** | Git ignore patterns | 45 |

## ⚡ 30-Second Quick Start

### Option A: Docker (Easiest)
```bash
docker-compose up -d
curl http://localhost:5001/health
```

### Option B: Local Python
```bash
# First time only: Create conda environment
conda create -n html_to_pdf python=3.11 -y
conda activate html_to_pdf
pip install -r requirements.txt

# Every time: Run the API
python app.py
```

### Option C: Windows Automated
```bash
setup.bat
```

## 🧪 Test the API

**In a new terminal:**

```bash
# Run full test suite
python test_api.py

# Or test manually with curl
curl -X POST http://localhost:5001/html-to-pdf \
  -H "Content-Type: application/json" \
  -d '{"html": "<html><body><h1>Hello</h1><p>World</p></body></html>"}' \
  --output report.pdf
```

## 📊 Key Features

### 🛡️ Production-Grade Error Handling
- Comprehensive exception handling for all scenarios
- Never crashes on invalid requests
- Detailed error messages with context
- Custom exception classes
- Global error handlers

### 📝 Intelligent Logging
- Structured logging with timestamps
- Request/response tracking
- PDF generation details
- Error tracebacks
- Performance metrics

### 🔐 Security
- Input validation & sanitization
- Size limits (10MB HTML, 50MB total)
- Type checking
- Error message sanitization
- Non-root Docker user
- Read-only filesystem

### 🚀 Scalability
- Gunicorn multi-worker support
- Stateless design
- Docker orchestration ready
- Health checks for monitoring
- Resource limits

## 🔧 API Endpoints

### Convert HTML to PDF
```http
POST /html-to-pdf
Content-Type: application/json

{
  "html": "<html>...</html>"
}
```
Returns: Binary PDF file

### Health Check
```http
GET /health
```
Returns: `{"status": "ok", "service": "html-to-pdf-api", "version": "1.0.0"}`

### API Info
```http
GET /info
```
Returns: API metadata and capabilities

## 📦 What You Need

### For Local Development
- Python 3.11+
- Conda/Anaconda (optional, but recommended)
- System dependencies for WeasyPrint

### For Docker
- Docker
- Docker Compose
- Nothing else required!

## 🎓 Learning Resources

1. **New to this project?** → Start with [QUICKSTART.md](QUICKSTART.md)
2. **Need setup help?** → See [WINDOWS_SETUP.md](WINDOWS_SETUP.md)
3. **Want full details?** → Read [README.md](README.md)
4. **Understand architecture?** → Check [PROJECT_INVENTORY.md](PROJECT_INVENTORY.md)
5. **Explore code?** → Read [app.py](app.py) (well-documented)
6. **Test it out?** → Run [test_api.py](test_api.py)

## ✅ Verification

After setup, verify everything works:

```bash
# Health check
curl http://localhost:5001/health

# Run tests
python test_api.py

# Check API info
curl http://localhost:5001/info
```

All three should return JSON responses without errors.

## 🚀 Next Steps

1. **Choose setup method** (Local/Docker/Automated)
2. **Follow setup guide** for your platform
3. **Start the API** (`python app.py` or `docker-compose up -d`)
4. **Run tests** (`python test_api.py`)
5. **Explore endpoints** (see README.md for examples)
6. **Deploy to production** (use Docker Compose)

## 📋 Project Structure

```
HTML to PDF API/
├── Core Files
│   ├── app.py                    # Flask application
│   ├── requirements.txt          # Dependencies
│   └── test_api.py               # Test suite
│
├── Docker & Deployment
│   ├── Dockerfile                # Docker image
│   ├── docker-compose.yml        # Docker Compose
│   ├── setup.bat                 # Windows batch setup
│   └── setup.ps1                 # PowerShell setup
│
├── Documentation
│   ├── README.md                 # Full documentation
│   ├── QUICKSTART.md             # Quick start
│   ├── WINDOWS_SETUP.md          # Windows guide
│   ├── PROJECT_INVENTORY.md      # Architecture
│   └── INDEX.md                  # This file
│
└── Configuration
    ├── .env.example              # Environment template
    └── .gitignore                # Git ignore rules
```

## 💡 Pro Tips

1. **Development**: Run locally with `python app.py`
2. **Testing**: Use included `test_api.py` test suite
3. **Production**: Use `docker-compose up -d`
4. **Debugging**: Check logs with `docker-compose logs -f`
5. **Monitoring**: Use `/health` endpoint for health checks

## 🆘 Troubleshooting

**"Module not found"**
→ Install dependencies: `pip install -r requirements.txt`

**"Cannot connect to API"**
→ Make sure API is running: `python app.py`

**"Port 5001 in use"**
→ Change port in `app.py` or find/kill process using port

**"Conda not recognized"**
→ Use Anaconda Prompt instead of regular Command Prompt

**"Docker issues"**
→ Make sure Docker Desktop is running

## 📞 Getting Help

- 📖 Full docs: [README.md](README.md)
- ⚡ Quick start: [QUICKSTART.md](QUICKSTART.md)
- 🪟 Windows help: [WINDOWS_SETUP.md](WINDOWS_SETUP.md)
- 🏗️ Architecture: [PROJECT_INVENTORY.md](PROJECT_INVENTORY.md)

## ✨ What Makes This Special

✅ **Production-Ready**: Not a toy project - enterprise-grade error handling
✅ **Intelligent**: Handles edge cases and errors gracefully
✅ **Well-Documented**: 2000+ lines of documentation
✅ **Easy to Deploy**: Docker support built-in
✅ **Tested**: Comprehensive test suite included
✅ **Secure**: Input validation, size limits, error sanitization
✅ **Scalable**: Multi-worker, container-ready
✅ **Maintainable**: Clean code, good structure, logging

## 🎯 Common Tasks

### Run the API
```bash
# Local
python app.py

# Docker
docker-compose up -d
```

### Test the API
```bash
python test_api.py
```

### Stop the API
```bash
# Local: Ctrl+C in terminal
# Docker: docker-compose down
```

### View Logs
```bash
# Docker
docker-compose logs -f html-to-pdf-api
```

### Deploy to Production
```bash
docker-compose up -d
```

## 🎉 You're Ready!

Your production-grade HTML to PDF API is ready to use!

1. Choose your setup method
2. Follow the guide for your platform
3. Run the API
4. Test with the included test suite
5. Deploy with Docker

**Questions?** Check the documentation files or see Troubleshooting section.

---

**Version**: 1.0.0 | **Status**: Production-Ready ✅ | **Last Updated**: May 24, 2026

**Need help?** Start with [QUICKSTART.md](QUICKSTART.md) or [WINDOWS_SETUP.md](WINDOWS_SETUP.md)
