@echo off
echo ===============================================
echo EXPERIMENT 2 - Sequential (FULL ARRAY TEST)
echo Version 2.1.0
echo ===============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ===============================================
    echo ERROR: Python is not installed!
    echo ===============================================
    echo.
    echo You need to install PsychoPy first!
    echo.
    echo Please follow these steps:
    echo 1. Go to: https://www.psychopy.org/download.html
    echo 2. Download PsychoPy Standalone for Windows
    echo 3. Install it ^(use default settings^)
    echo 4. Then run this file again
    echo.
    echo OR read: START_HERE.md for detailed instructions
    echo.
    pause
    exit /b 1
)

REM Check if PsychoPy is installed
python -c "import psychopy" >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ===============================================
    echo ERROR: PsychoPy is not installed!
    echo ===============================================
    echo.
    echo Python is installed, but PsychoPy is missing.
    echo.
    echo Please follow these steps:
    echo 1. Go to: https://www.psychopy.org/download.html
    echo 2. Download PsychoPy Standalone for Windows
    echo 3. Install it ^(use default settings^)
    echo 4. Then run this file again
    echo.
    echo OR run: INSTALL_DEPENDENCIES.bat
    echo.
    pause
    exit /b 1
)

echo Starting experiment...
echo.
python experiment2_sequential.py
echo.
echo Experiment finished!
pause
