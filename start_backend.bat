@echo off
echo Starting Global Investment Intelligence Dashboard Backend...
echo.

cd backend

echo Installing dependencies...
pip install -r ../requirements_backend.txt

echo.
echo Starting server...
python start_backend.py

pause 