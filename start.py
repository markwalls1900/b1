#!/usr/bin/env python3
"""
Simple startup script for BWGA Nexus
"""

import subprocess
import sys
import os

def main():
    print("🚀 Starting BWGA Nexus Investment Intelligence Platform...")
    print("Version: 7.1.0 - Unified System")
    print("-" * 50)
    
    # Check if required files exist
    required_files = ['app.py', 'investment_algorithm.py']
    missing_files = []
    
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing required files: {', '.join(missing_files)}")
        print("Please ensure all files are present in the current directory.")
        return
    
    print("✅ All required files found")
    print("🌍 Starting server...")
    print("-" * 50)
    
    try:
        # Start the Flask app
        subprocess.run([sys.executable, 'app.py'])
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"❌ Error starting server: {e}")

if __name__ == "__main__":
    main() 