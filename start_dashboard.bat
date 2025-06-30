@echo off
title BWGA Nexus Investment Intelligence Platform
color 0A

echo.
echo ========================================
echo   BWGA Nexus Investment Intelligence
echo   Production Platform v7.1.0
echo ========================================
echo.

echo Starting production backend server...
echo.

cd /d "%~dp0production_backend"

echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.9+ from https://python.org
    echo.
    pause
    exit /b 1
)

echo Python found! Starting server...
echo.
echo Server will be available at: http://localhost:8000
echo Dashboard: http://localhost:8000
echo API Docs: http://localhost:8000/api/docs
echo.
echo Press Ctrl+C to stop the server
echo.

python start_production_simple.py

echo.
echo Server stopped.
pause 