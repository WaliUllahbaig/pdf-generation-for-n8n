# 🚀 How to Run & Test the API

This guide shows you how to run the HTML to PDF API and test it with various methods, including **interactive Swagger UI**.

## ⚡ Quick Start (30 seconds)

### Option 1: Windows - One Click
```bash
run.bat
```

### Option 2: Linux/Mac - One Command
```bash
bash run.sh
```

### Option 3: Docker - One Command
```bash
run_docker.bat    # Windows
# or
docker-compose up -d  # All platforms
```

---

## 🔥 Main Testing Method: Swagger/OpenAPI UI

The **easiest way to test** the API is through the interactive Swagger UI!

### 1. Start the API
```bash
python app.py
# or use: run.bat (Windows), run.sh (Linux/Mac), or run_docker.bat (Docker)
```

### 2. Open Swagger UI in Browser
Go to: **http://localhost:5001/apidocs**

You'll see the interactive API documentation with:
- ✅ All endpoints listed
- ✅ Request/response schemas
- ✅ Try-it-out button to test directly
- ✅ Example payloads
- ✅ Response previews

### 3. Test the Conversion
1. Click on **POST /html-to-pdf**
2. Click **Try it out**
3. Enter HTML in the request body:
   ```json
   {
     "html": "<html><body><h1>Hello World</h1><p>This is my first PDF</p></body></html>"
   }
   ```
4. Click **Execute**
5. Download the PDF from the response!

---

## 📖 Different Ways to Run

### Method 1: Windows Batch (Recommended for Windows Users)

```bash
run.bat
```

**What it does:**
- Activates conda environment
- Checks dependencies
- Displays startup info
- Shows API endpoints
- Starts the Flask app

**When to use:** Windows users who want automatic setup

---

### Method 2: Linux/Mac Shell Script

```bash
chmod +x run.sh    # Make executable (first time only)
bash run.sh
```

**When to use:** Linux/Mac development

---

### Method 3: Manual Python (All Platforms)

```bash
# Activate environment
conda activate html_to_pdf

# Run the app
python app.py
```

**When to use:** Direct control, debugging

---

### Method 4: Docker Compose (Production Recommended)

**Option A: Windows**
```bash
run_docker.bat
```

**Option B: All Platforms**
```bash
docker-compose up -d
```

**When to use:** Production, consistent environment, no local Python needed

---

### Method 5: Docker - Build & Run Manually

```bash
# Build image
docker build -t html-to-pdf-api .

# Run container
docker run -p 5001:5001 html-to-pdf-api
```

---

## 🧪 Testing Methods

### 1️⃣ **Interactive Swagger UI** (Easiest!)

**URL:** http://localhost:5001/apidocs

**Features:**
- Visual interface
- Click "Try it out"
- See live responses
- Download PDFs directly
- Auto-generated documentation

**Best for:** Quick testing, demos, learning

---

### 2️⃣ **Terminal/PowerShell Commands**

**Simple HTML:**
```bash
curl -X POST http://localhost:5001/html-to-pdf \
  -H "Content-Type: application/json" \
  -d '{"html": "<html><body><h1>Test</h1></body></html>"}' \
  --output report.pdf
```

**Windows PowerShell:**
```powershell
$body = @{
    html = "<html><body><h1>Test</h1><p>Hello World</p></body></html>"
} | ConvertTo-Json

Invoke-WebRequest -Uri http://localhost:5001/html-to-pdf `
  -Method POST `
  -ContentType "application/json" `
  -Body $body `
  -OutFile "report.pdf"
```

**Windows CMD:**
```cmd
curl -X POST http://localhost:5001/html-to-pdf ^
  -H "Content-Type: application/json" ^
  -d "{\"html\": \"<html><body><h1>Test</h1></body></html>\"}" ^
  --output report.pdf
```

---

### 3️⃣ **Postman Collection**

**Steps:**
1. Open Postman
2. Create new request: `POST http://localhost:5001/html-to-pdf`
3. Set Headers:
   ```
   Content-Type: application/json
   ```
4. Set Body (raw JSON):
   ```json
   {
     "html": "<html><body><h1>Hello</h1></body></html>"
   }
   ```
5. Send
6. Right-click response → Save response → Save to file

---

### 4️⃣ **Python Script**

```python
import requests

url = "http://localhost:5001/html-to-pdf"
html_content = "<html><body><h1>Hello</h1><p>This is my PDF</p></body></html>"

response = requests.post(
    url,
    json={"html": html_content},
    headers={"Content-Type": "application/json"}
)

if response.status_code == 200:
    with open("report.pdf", "wb") as f:
        f.write(response.content)
    print("✓ PDF saved as report.pdf")
else:
    print(f"Error: {response.json()}")
```

---

### 5️⃣ **VS Code REST Client Extension**

1. Install "REST Client" extension
2. Create file `test.http`:
   ```
   POST http://localhost:5001/html-to-pdf
   Content-Type: application/json

   {
     "html": "<html><body><h1>Hello</h1></body></html>"
   }
   ```
3. Click "Send Request"

---

## 📊 Testing More Complex HTML

### Test 1: HTML with Styling

**Via Swagger:**
```json
{
  "html": "<html><head><style>body { font-family: Arial; margin: 20px; } h1 { color: blue; } .highlight { background-color: yellow; }</style></head><body><h1>Styled Report</h1><p>This has <span class='highlight'>CSS</span> styling!</p></body></html>"
}
```

### Test 2: HTML with Table

```json
{
  "html": "<html><head><style>table { border-collapse: collapse; width: 100%; } th, td { border: 1px solid #ddd; padding: 8px; text-align: left; } th { background-color: #4CAF50; color: white; }</style></head><body><h1>Sales Report</h1><table><tr><th>Month</th><th>Sales</th></tr><tr><td>January</td><td>$10,000</td></tr><tr><td>February</td><td>$12,500</td></tr></table></body></html>"
}
```

### Test 3: HTML with Images

```json
{
  "html": "<html><body><h1>Report with Image</h1><img src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==' style='width: 200px;'><p>Image embedded in PDF</p></body></html>"
}
```

---

## ✅ Other Test Endpoints

### Health Check

**Swagger UI:** http://localhost:5001/apidocs → GET /health

**curl:**
```bash
curl http://localhost:5001/health
```

**Response:**
```json
{
  "status": "ok",
  "service": "html-to-pdf-api",
  "version": "1.0.0"
}
```

### API Info

**Swagger UI:** http://localhost:5001/apidocs → GET /info

**curl:**
```bash
curl http://localhost:5001/info
```

---

## 🐛 Troubleshooting

### "Cannot connect to http://localhost:5001"
- Make sure API is running
- Check it shows "Server running on http://0.0.0.0:5001"
- Try `curl http://localhost:5001/health` in terminal

### "Swagger not loading"
- Update requirements.txt: `pip install -r requirements.txt`
- Restart the API
- Clear browser cache (Ctrl+Shift+Delete)
- Try: http://localhost:5001/apidocs

### "Port 5001 already in use"
- Change port in `app.py` line ~65: `port=5002`
- Or: Find process using 5001 and stop it

### "Module not found"
- Install dependencies: `pip install -r requirements.txt`
- Check you're in correct environment: `conda activate html_to_pdf`

---

## 🚀 Production Testing

### Docker Deployment Test

```bash
# Start
docker-compose up -d

# Test health
curl http://localhost:5001/health

# View logs
docker-compose logs -f

# Stop
docker-compose down
```

### Automated Test Suite

```bash
# Run all 10 test cases
python test_api.py
```

---

## 📋 Quick Reference

| Task | Command |
|------|---------|
| Start (Windows) | `run.bat` |
| Start (Linux/Mac) | `bash run.sh` |
| Start (Docker) | `docker-compose up -d` or `run_docker.bat` |
| Open Swagger UI | http://localhost:5001/apidocs |
| Health check | `curl http://localhost:5001/health` |
| Run tests | `python test_api.py` |
| Stop (Ctrl+C for local, Docker: | `docker-compose down` |
| View logs | `docker-compose logs -f` |

---

## 💡 Pro Tips

1. **Use Swagger for quick testing** - Easiest way to see what the API does
2. **Use `run.bat` on Windows** - Handles all setup automatically
3. **Use Docker for production** - Consistent, reproducible environment
4. **Keep terminal open** - Shows logs and errors in real-time
5. **Test before deployment** - Run `python test_api.py` to verify everything works

---

## 🎯 Workflow Example

### Day 1: Setup & Testing
```bash
# 1. Run startup script
run.bat

# 2. Open browser
# http://localhost:5001/apidocs

# 3. Test with Swagger UI
# Try: POST /html-to-pdf with sample HTML

# 4. Download generated PDF
```

### Day 2+: Integration & Testing
```bash
# 1. Start API (keeps running)
run.bat

# 2. Test from your application
python your_app.py

# 3. Monitor in separate terminal
docker-compose logs -f  # If using Docker

# 4. Deploy
docker-compose up -d  # For production
```

---

## 📚 API Endpoints Summary

| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | `/html-to-pdf` | Convert HTML to PDF (main) |
| GET | `/health` | Health check |
| GET | `/info` | API information |
| GET | `/apidocs` | Interactive Swagger UI ⭐ |
| GET | `/flasgger_static/...` | Swagger resources |

---

## 🎉 Next Steps

1. **Start the API** using `run.bat`, `run.sh`, or `docker-compose up -d`
2. **Open Swagger UI** at http://localhost:5001/apidocs
3. **Click "Try it out"** on POST /html-to-pdf
4. **Paste HTML** and click "Execute"
5. **Download PDF** from response
6. **Deploy** when ready with `docker-compose up -d`

---

**Ready to test? Start with `run.bat` or visit http://localhost:5001/apidocs!** 🚀
