# 🚀 SIMPLEST WAY TO RUN - No Commands!

## ✅ Step 1: Click to Start

**Just double-click this file:**
```
START.bat
```

That's it! Wait 2-3 minutes and the API will be running.

---

## 📖 Step 2: Test the API

After clicking `START.bat`, a browser will open automatically showing:

```
http://localhost:5001/apidocs
```

You'll see a beautiful interface where you can:
- Click "POST /html-to-pdf"
- Click "Try it out"
- Paste HTML
- Click "Execute"
- Download your PDF

---

## 🔗 Quick Links

**For Testing (Local Machine):**
```
http://localhost:5001/apidocs
```

**For n8n (Local Machine):**
```
http://localhost:5001/html-to-pdf
```

**For Health Check:**
```
http://localhost:5001/health
```

---

## 🐳 When You Deploy to Docker/Server for n8n

After you deploy on your server, use:

```
http://YOUR-SERVER-IP:5001/html-to-pdf
```

**Examples:**
- If server IP is `192.168.1.100`: 
  ```
  http://192.168.1.100:5001/html-to-pdf
  ```

- If using domain name:
  ```
  http://your-domain.com:5001/html-to-pdf
  ```

- If using Docker on same machine:
  ```
  http://localhost:5001/html-to-pdf
  ```

---

## 📝 For n8n Configuration

### Local Machine:
```
URL: http://localhost:5001/html-to-pdf
Method: POST
Content-Type: application/json
Body:
{
  "html": "<html><body><h1>Your HTML Here</h1></body></html>"
}
```

### Docker/Server:
```
URL: http://YOUR-SERVER-IP:5001/html-to-pdf
Method: POST
Content-Type: application/json
Body:
{
  "html": "<html><body><h1>Your HTML Here</h1></body></html>"
}
```

---

## ❌ If START.bat Shows "Docker Not Found"

You need to install Docker Desktop:
1. Download from: https://www.docker.com/products/docker-desktop
2. Install it
3. Run START.bat again

---

## ⏹ To Stop the API

Just close the window where `START.bat` is running, or press:
```
Ctrl+C
```

---

## 📋 Summary

| What | Link | When to Use |
|------|------|------------|
| Test in Browser | `http://localhost:5001/apidocs` | Development |
| Use in n8n (Local) | `http://localhost:5001/html-to-pdf` | Testing n8n locally |
| Use in n8n (Docker) | `http://SERVER-IP:5001/html-to-pdf` | Production n8n |
| Health Check | `http://localhost:5001/health` | Monitoring |

---

## 🎯 That's All!

1. Click `START.bat`
2. Wait for browser to open
3. Test the API
4. Use the links for n8n

**Everything just works!** 🎉
