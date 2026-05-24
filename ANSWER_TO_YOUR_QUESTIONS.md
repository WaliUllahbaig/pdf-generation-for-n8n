# 🎯 EXACTLY WHAT YOU ASKED FOR

## ✅ Question 1: "Just run app.py and it should work"

You're right - that should work. But Windows + WeasyPrint = library issues.

**Solution: Use the launcher files instead**

---

## 🚀 How to Run (Pick ONE)

### **Option 1: Click This (Easiest if Docker installed)**
```
START.bat
```
- Click it
- Wait 2-3 minutes
- Browser opens automatically
- Done!

### **Option 2: Run This (Works without Docker)**
```
launcher_simple.py
```
- Right-click → Open with Python
- OR double-click if Python file associations are set
- Wait 1-2 minutes
- Browser opens automatically
- Done!

### **Option 3: Manual Python (Advanced)**
```
python app.py
```

---

## 📖 Question 2: "Swagger link to test"

**When running locally:**
```
http://localhost:5001/apidocs
```

This is where you test everything. Click it and you'll see a beautiful interface with:
- POST /html-to-pdf (main button)
- Health check
- API info

Just click "Try it out" and paste HTML!

---

## 🐳 Question 3: "What link when hosted on Docker for n8n"

**When deployed on Docker (Production):**

```
http://YOUR-SERVER-IP:5001/html-to-pdf
```

**Examples:**
- If server IP is `192.168.1.100`: `http://192.168.1.100:5001/html-to-pdf`
- If using domain: `http://your-domain.com:5001/html-to-pdf`
- If Docker on same machine: `http://localhost:5001/html-to-pdf`

**How to use in n8n:**
1. Add HTTP request node in n8n
2. Set URL to: `http://YOUR-SERVER-IP:5001/html-to-pdf`
3. Set method: POST
4. Set content-type: application/json
5. Send: `{"html": "<html>...</html>"}`
6. Get: PDF file as response

---

## 📋 Complete Reference

| Scenario | Link | Use Case |
|----------|------|----------|
| **Test API (Local)** | `http://localhost:5001/apidocs` | Before using in n8n |
| **n8n (Same Machine)** | `http://localhost:5001/html-to-pdf` | Testing locally |
| **n8n (Docker Server)** | `http://192.168.X.X:5001/html-to-pdf` | Production |
| **Health Check** | `http://localhost:5001/health` | Monitor API |

---

## 🎯 Your Exact Workflow

### **Step 1: Run the API**
```
Click: START.bat
or
Run: launcher_simple.py
```

### **Step 2: Test It**
```
Open: http://localhost:5001/apidocs
```

### **Step 3: Deploy to Docker (Production)**
```
Run: docker-compose up -d
```

### **Step 4: Use in n8n**
```
URL: http://YOUR-SERVER-IP:5001/html-to-pdf
```

---

## ✨ That's All!

No complex commands. Just:
1. Click a file
2. Paste a link
3. Use in n8n

**Everything else is handled automatically!**

---

## 🆘 If Something Goes Wrong

**Error with START.bat:** Install Docker Desktop, then try again

**Error with launcher_simple.py:** Run `pip install -r requirements.txt`, then try again

**For n8n production:** Ask your DevOps team for the server IP, then use: `http://SERVER-IP:5001/html-to-pdf`

---

**That's it! You're all set! 🎉**
