# Quick Start Guide

## 🚀 Quick Setup (Choose One)

### Option A: Docker Compose (Easiest - Recommended for Production)

```bash
cd "d:\Raw Projects\PDF generator"
docker-compose up -d
```

Then test:
```bash
curl http://localhost:5001/health
```

### Option B: Local Python (Windows)

```bash
# 1. Activate the conda environment
conda activate html_to_pdf

# 2. Install dependencies (first time only)
pip install -r requirements.txt

# 3. Run the API
python app.py
```

Then in another terminal:
```bash
curl -X POST http://localhost:5001/html-to-pdf ^
  -H "Content-Type: application/json" ^
  -d "{\"html\": \"<html><body><h1>Test</h1></body></html>\"}" ^
  --output report.pdf
```

## 📝 Project Files

- **app.py** - Flask API with comprehensive error handling
- **requirements.txt** - Python dependencies
- **Dockerfile** - Docker image specification
- **docker-compose.yml** - Docker Compose configuration
- **README.md** - Full documentation
- **test_api.py** - Comprehensive test suite
- **.gitignore** - Git ignore rules
- **.env.example** - Environment variables template

## 🧪 Testing

### Test with Python Script
```bash
python test_api.py
```

### Test Manually
```bash
# Simple test
curl -X POST http://localhost:5001/html-to-pdf \
  -H "Content-Type: application/json" \
  -d "{\"html\": \"<html><body><h1>Hello</h1><p>World</p></body></html>\"}" \
  --output test.pdf

# Check health
curl http://localhost:5001/health

# Get API info
curl http://localhost:5001/info
```

## 🛑 Stop the API

### Docker
```bash
docker-compose down
```

### Python
Press `Ctrl+C` in the terminal running `python app.py`

## 📊 Features

✅ Production-grade error handling
✅ Comprehensive logging
✅ Health check endpoints
✅ Request validation
✅ Memory limits
✅ Docker support
✅ Comprehensive documentation
✅ Test suite included

## 🔧 Configuration

### Docker Resource Limits
Edit `docker-compose.yml`:
```yaml
mem_limit: 1g          # Adjust memory
cpus: '2'              # Adjust CPU count
```

### Flask Configuration
Edit `app.py`:
```python
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # Max request size
# HTML size limit in validate_html_input function
```

## 📖 Documentation

For full documentation, see `README.md`

## ✅ Verification Checklist

- [ ] Conda environment created
- [ ] Dependencies installed
- [ ] API running locally or in Docker
- [ ] Health check passes
- [ ] Test API script runs successfully
- [ ] PDF files generated in test_output/

## 🐛 Troubleshooting

**"conda: not recognized"** - Install Anaconda or use Docker instead

**"Module not found"** - Install dependencies: `pip install -r requirements.txt`

**"Cannot connect to localhost:5001"** - Make sure API is running

**"Port 5001 in use"** - Change port in `docker-compose.yml` or `app.py`

## 🔐 Production Deployment

1. Use Docker Compose for easy deployment
2. Set environment to production
3. Use Nginx as reverse proxy for HTTPS
4. Implement rate limiting
5. Add API authentication if needed
6. Monitor logs and resource usage
7. Set up health checks for your orchestrator

## 📞 Support

Refer to `README.md` for:
- Detailed API documentation
- Advanced configuration
- Error handling details
- Performance optimization
- Security considerations
- Production deployment guide
