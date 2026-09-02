@echo off
echo ===============================================
echo PSYCHOPY SETUP DIAGNOSTIC TEST
echo ===============================================
echo.
echo Checking your setup...
echo.

echo [1/5] Checking Python...
python --version
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Python not found!
    echo Please install Python or PsychoPy Standalone
    pause
    exit /b 1
)
echo OK: Python found!
echo.

echo [2/5] Checking PsychoPy...
python -c "import psychopy; print('PsychoPy version:', psychopy.__version__)"
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: PsychoPy not installed!
    echo Run INSTALL_DEPENDENCIES.bat first
    pause
    exit /b 1
)
echo OK: PsychoPy installed!
echo.

echo [3/5] Checking required packages...
python -c "import pandas; import openpyxl; print('Packages OK')"
if %ERRORLEVEL% NEQ 0 (
    echo WARNING: Some packages missing
    echo Run INSTALL_DEPENDENCIES.bat to fix
)
echo.

echo [4/5] Checking conditions folder...
if not exist "conditions\" (
    echo ERROR: conditions folder not found!
    pause
    exit /b 1
)
if not exist "conditions\practice_conditions.csv" (
    echo ERROR: practice_conditions.csv not found!
    pause
    exit /b 1
)
if not exist "conditions\experiment1_conditions.csv" (
    echo ERROR: experiment1_conditions.csv not found!
    pause
    exit /b 1
)
if not exist "conditions\experiment2_conditions.csv" (
    echo ERROR: experiment2_conditions.csv not found!
    pause
    exit /b 1
)
echo OK: All condition files found!
echo.

echo [5/5] Checking experiment files...
if not exist "experiment1_simultaneous.py" (
    echo ERROR: experiment1_simultaneous.py not found!
    pause
    exit /b 1
)
if not exist "experiment2_sequential.py" (
    echo ERROR: experiment2_sequential.py not found!
    pause
    exit /b 1
)
echo OK: Experiment files found!
echo.

echo ===============================================
echo ALL CHECKS PASSED!
echo ===============================================
echo.
echo Your setup is ready to run experiments!
echo.
echo Next steps:
echo 1. Double-click RUN_EXPERIMENT1.bat or RUN_EXPERIMENT2.bat
echo 2. Enter participant information
echo 3. Follow on-screen instructions
echo.
pause
