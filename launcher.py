#!/usr/bin/env python3
"""
Simple GUI Launcher for HTML to PDF API
Just run this file - no commands needed!
"""

import tkinter as tk
from tkinter import messagebox, ttk
import subprocess
import sys
import os
import threading
import webbrowser
import time

class APILauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("🚀 HTML to PDF API Launcher")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        
        # Center window
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 600) // 2
        y = (screen_height - 500) // 2
        self.root.geometry(f"+{x}+{y}")
        
        self.api_process = None
        self.setup_ui()
        
    def setup_ui(self):
        # Title
        title = tk.Label(
            self.root,
            text="🚀 HTML to PDF API",
            font=("Arial", 18, "bold"),
            fg="#2196F3"
        )
        title.pack(pady=20)
        
        # Status
        self.status_label = tk.Label(
            self.root,
            text="Status: Not Running",
            font=("Arial", 12),
            fg="#666"
        )
        self.status_label.pack(pady=10)
        
        # Main buttons frame
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)
        
        # Start button
        self.start_btn = tk.Button(
            button_frame,
            text="▶ START API",
            font=("Arial", 14, "bold"),
            bg="#4CAF50",
            fg="white",
            padx=30,
            pady=15,
            command=self.start_api,
            cursor="hand2"
        )
        self.start_btn.pack(side=tk.LEFT, padx=10)
        
        # Stop button
        self.stop_btn = tk.Button(
            button_frame,
            text="⏹ STOP API",
            font=("Arial", 14, "bold"),
            bg="#f44336",
            fg="white",
            padx=30,
            pady=15,
            command=self.stop_api,
            cursor="hand2",
            state=tk.DISABLED
        )
        self.stop_btn.pack(side=tk.LEFT, padx=10)
        
        # Links frame
        links_frame = tk.LabelFrame(
            self.root,
            text="📖 API Links",
            font=("Arial", 11, "bold"),
            padx=15,
            pady=15
        )
        links_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
        
        # Swagger link
        swagger_frame = tk.Frame(links_frame)
        swagger_frame.pack(fill=tk.X, pady=8)
        
        tk.Label(
            swagger_frame,
            text="Swagger UI (Test API):",
            font=("Arial", 10, "bold")
        ).pack(side=tk.LEFT)
        
        self.swagger_link = tk.Label(
            swagger_frame,
            text="http://localhost:5001/apidocs",
            font=("Arial", 10, "underline"),
            fg="#2196F3",
            cursor="hand2"
        )
        self.swagger_link.pack(side=tk.LEFT, padx=10)
        self.swagger_link.bind("<Button-1>", lambda e: self.open_link("http://localhost:5001/apidocs"))
        
        # Health check link
        health_frame = tk.Frame(links_frame)
        health_frame.pack(fill=tk.X, pady=8)
        
        tk.Label(
            health_frame,
            text="Health Check:",
            font=("Arial", 10, "bold")
        ).pack(side=tk.LEFT)
        
        health_link = tk.Label(
            health_frame,
            text="http://localhost:5001/health",
            font=("Arial", 10, "underline"),
            fg="#2196F3",
            cursor="hand2"
        )
        health_link.pack(side=tk.LEFT, padx=10)
        health_link.bind("<Button-1>", lambda e: self.open_link("http://localhost:5001/health"))
        
        # Info frame
        info_frame = tk.Frame(links_frame)
        info_frame.pack(fill=tk.X, pady=8)
        
        tk.Label(
            info_frame,
            text="What is this?",
            font=("Arial", 10, "bold")
        ).pack(side=tk.LEFT)
        
        tk.Label(
            info_frame,
            text="Click links above to test the API. Swagger UI is interactive.",
            font=("Arial", 9),
            fg="#666"
        ).pack(side=tk.LEFT, padx=10)
        
        # Docker info
        docker_frame = tk.LabelFrame(
            self.root,
            text="🐳 For Docker/n8n Production",
            font=("Arial", 11, "bold"),
            padx=15,
            pady=10
        )
        docker_frame.pack(padx=20, pady=10, fill=tk.BOTH)
        
        docker_text = tk.Text(
            docker_frame,
            height=4,
            width=65,
            font=("Courier", 9),
            bg="#f5f5f5"
        )
        docker_text.pack()
        
        docker_info = """Docker Link: http://your-docker-host:5001/html-to-pdf
Docker Swagger: http://your-docker-host:5001/apidocs

For n8n: Use http://your-docker-host:5001/html-to-pdf
Replace "your-docker-host" with your server IP or domain"""
        
        docker_text.insert(1.0, docker_info)
        docker_text.config(state=tk.DISABLED)
        
    def start_api(self):
        try:
            # Start Flask app
            self.api_process = subprocess.Popen(
                [sys.executable, "app.py"],
                cwd=os.getcwd(),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            
            self.status_label.config(text="Status: ✓ Running", fg="#4CAF50")
            self.start_btn.config(state=tk.DISABLED)
            self.stop_btn.config(state=tk.NORMAL)
            
            messagebox.showinfo(
                "✓ API Started",
                "API is running!\n\n"
                "Click the links to test:\n"
                "• Swagger UI: http://localhost:5001/apidocs\n"
                "• Health: http://localhost:5001/health\n\n"
                "API will run until you click STOP"
            )
            
            # Try to open Swagger in browser
            threading.Timer(2.0, lambda: webbrowser.open("http://localhost:5001/apidocs")).start()
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start API:\n{str(e)}")
            
    def stop_api(self):
        if self.api_process:
            self.api_process.terminate()
            try:
                self.api_process.wait(timeout=5)
            except:
                self.api_process.kill()
            
            self.status_label.config(text="Status: Stopped", fg="#666")
            self.start_btn.config(state=tk.NORMAL)
            self.stop_btn.config(state=tk.DISABLED)
            
            messagebox.showinfo("✓ API Stopped", "API has been stopped")
            
    def open_link(self, url):
        webbrowser.open(url)


if __name__ == "__main__":
    root = tk.Tk()
    app = APILauncher(root)
    root.mainloop()
