@echo off
echo.
echo ========================================
echo   BWGA Nexus Investment Intelligence
echo   Version 7.1.0 - Unified System
echo ========================================
echo.

echo Starting BWGA Nexus...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher
    pause
    exit /b 1
)

REM Install requirements if needed
echo Installing requirements...
pip install -r requirements.txt

REM Start the application
echo.
echo Starting server...
echo.
python app.py

pause 