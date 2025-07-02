#!/usr/bin/env python3
import http.server
import socketserver
import os
import sys

# Change to the directory containing the HTML files
os.chdir('/workspace')

# Define the port
PORT = 54812

# Create a custom handler to serve files with proper MIME types
class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        # Add headers to allow iframe embedding
        self.send_header('X-Frame-Options', 'ALLOWALL')
        super().end_headers()

# Create the server
with socketserver.TCPServer(("0.0.0.0", PORT), MyHTTPRequestHandler) as httpd:
    print(f"Server running at http://localhost:{PORT}")
    print(f"Serving files from: {os.getcwd()}")
    print("Press Ctrl+C to stop the server")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        sys.exit(0)