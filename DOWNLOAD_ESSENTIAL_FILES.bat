@echo off
echo ========================================
echo BWGA Nexus Investment Intelligence Platform
echo Essential Files Download Script
echo ========================================
echo.

REM Create download directory
if not exist "BWGA_NEXUS_DOWNLOAD" mkdir "BWGA_NEXUS_DOWNLOAD"

echo Copying essential files...

REM Copy main application files
copy "index.html" "BWGA_NEXUS_DOWNLOAD\"
copy "complete_system.py" "BWGA_NEXUS_DOWNLOAD\"
copy "enhanced_investment_algorithm.py" "BWGA_NEXUS_DOWNLOAD\"
copy "investment_algorithm.py" "BWGA_NEXUS_DOWNLOAD\"

REM Copy requirements and documentation
copy "requirements.txt" "BWGA_NEXUS_DOWNLOAD\"
copy "requirements_backend.txt" "BWGA_NEXUS_DOWNLOAD\"
copy "requirements_production.txt" "BWGA_NEXUS_DOWNLOAD\"
copy "README.md" "BWGA_NEXUS_DOWNLOAD\"
copy "README_BACKEND.md" "BWGA_NEXUS_DOWNLOAD\"
copy "SETUP_GUIDE.md" "BWGA_NEXUS_DOWNLOAD\"

REM Copy deployment files
copy "render_deploy.py" "BWGA_NEXUS_DOWNLOAD\"
copy "serve_dashboard.py" "BWGA_NEXUS_DOWNLOAD\"
copy "start_dashboard.py" "BWGA_NEXUS_DOWNLOAD\"

REM Copy quick start batch files
copy "open_dashboard.bat" "BWGA_NEXUS_DOWNLOAD\"
copy "run_complete_system.bat" "BWGA_NEXUS_DOWNLOAD\"
copy "start_backend.bat" "BWGA_NEXUS_DOWNLOAD\"

REM Copy additional dashboards
copy "enhanced_dashboard.html" "BWGA_NEXUS_DOWNLOAD\"
copy "nexus7.1.html" "BWGA_NEXUS_DOWNLOAD\"
copy "regional_investment_dashboard.html" "BWGA_NEXUS_DOWNLOAD\"
copy "standalone_dashboard.html" "BWGA_NEXUS_DOWNLOAD\"

REM Copy download guide
copy "BWGA_NEXUS_DOWNLOAD_PACKAGE.md" "BWGA_NEXUS_DOWNLOAD\"

echo.
echo ========================================
echo DOWNLOAD COMPLETE!
echo ========================================
echo.
echo Essential files copied to: BWGA_NEXUS_DOWNLOAD\
echo.
echo QUICK START:
echo 1. Open BWGA_NEXUS_DOWNLOAD\index.html in your browser
echo 2. Or run BWGA_NEXUS_DOWNLOAD\run_complete_system.bat
echo.
echo READ: BWGA_NEXUS_DOWNLOAD\BWGA_NEXUS_DOWNLOAD_PACKAGE.md for full instructions
echo.
pause 