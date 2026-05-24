#!/usr/bin/env python3
"""
🚀 HTML to PDF API - Simple Launcher
Just run this file - everything is automatic!
No commands needed.
"""

import subprocess
import sys
import os
import time
import webbrowser
import threading

def main():
    print("\n")
    print("="*70)
    print("                🚀 HTML to PDF API Launcher")
    print("="*70)
    print("\n")
    
    # Check Python
    print("[✓] Python is working")
    print(f"[✓] Python version: {sys.version.split()[0]}")
    print("\n")
    
    # Check Flask
    print("[*] Checking dependencies...")
    try:
        import flask
        print("[✓] Flask found")
    except ImportError:
        print("[✗] Flask not found - installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "Flask"], check=False)
    
    # Check Flasgger
    try:
        import flasgger
        print("[✓] Flasgger found")
    except ImportError:
        print("[✗] Flasgger not found - installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "flasgger"], check=False)
    
    # Check WeasyPrint
    try:
        import weasyprint
        print("[✓] WeasyPrint found")
        weasyprint_ok = True
    except ImportError:
        print("[✗] WeasyPrint not found - installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "WeasyPrint"], check=False)
        weasyprint_ok = False
    
    print("\n")
    print("="*70)
    print("                  🚀 Starting API...")
    print("="*70)
    print("\n")
    
    # Start the app
    try:
        # Run app.py
        process = subprocess.Popen([sys.executable, "app.py"])
        
        # Wait for app to start
        time.sleep(3)
        
        # Try to open browser
        print("[*] Opening browser in 2 seconds...\n")
        time.sleep(2)
        
        try:
            webbrowser.open("http://localhost:5001/apidocs")
        except:
            pass
        
        print("="*70)
        print("                    ✅ API IS RUNNING!")
        print("="*70)
        print("\n")
        print("📖 CLICK THIS LINK TO TEST THE API:")
        print("   http://localhost:5001/apidocs")
        print("\n")
        print("🔗 QUICK LINKS:")
        print("   Test API:    http://localhost:5001/apidocs")
        print("   Health:      http://localhost:5001/health")
        print("   API Info:    http://localhost:5001/info")
        print("\n")
        print("🐳 FOR n8n PRODUCTION (Docker):")
        print("   URL: http://YOUR-SERVER-IP:5001/html-to-pdf")
        print("   (Replace YOUR-SERVER-IP with your server's IP address)")
        print("\n")
        print("⏹  TO STOP: Press Ctrl+C")
        print("\n")
        print("="*70)
        print("\n")
        
        # Keep running
        process.wait()
        
    except KeyboardInterrupt:
        print("\n\n✅ API stopped")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\n💡 Try using Docker instead:")
        print("   START.bat (if you have Docker installed)")
        sys.exit(1)


if __name__ == "__main__":
    main()
