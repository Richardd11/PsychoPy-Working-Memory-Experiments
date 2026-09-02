@echo off
title PsychoPy Experiments - Setup Wizard
color 0A
cls

:MENU
echo.
echo ===============================================
echo   PSYCHOPY EXPERIMENTS - SETUP WIZARD
echo ===============================================
echo.
echo What do you want to do?
echo.
echo 1. Check if PsychoPy is installed
echo 2. Install PsychoPy ^(opens download page^)
echo 3. Install Python packages
echo 4. Run complete setup test
echo 5. Run Experiment 1
echo 6. Run Experiment 2
echo 7. Exit
echo.
set /p choice="Enter your choice (1-7): "

if "%choice%"=="1" goto CHECK_PSYCHOPY
if "%choice%"=="2" goto INSTALL_PSYCHOPY
if "%choice%"=="3" goto INSTALL_PACKAGES
if "%choice%"=="4" goto TEST_SETUP
if "%choice%"=="5" goto RUN_EXP1
if "%choice%"=="6" goto RUN_EXP2
if "%choice%"=="7" goto EXIT
goto MENU

:CHECK_PSYCHOPY
cls
echo.
echo ===============================================
echo Checking Python installation...
echo ===============================================
python --version
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ❌ Python is NOT installed!
    echo    You need to install PsychoPy first.
    echo.
    pause
    goto MENU
) else (
    echo ✅ Python is installed!
)

echo.
echo ===============================================
echo Checking PsychoPy installation...
echo ===============================================
python -c "import psychopy; print('PsychoPy version:', psychopy.__version__)"
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ❌ PsychoPy is NOT installed!
    echo    Please choose option 2 to install.
    echo.
    pause
    goto MENU
) else (
    echo ✅ PsychoPy is installed!
)

echo.
echo ===============================================
echo ✅ ALL CHECKS PASSED!
echo ===============================================
echo.
echo PsychoPy is ready to use!
echo Next step: Install Python packages ^(option 3^)
echo.
pause
goto MENU

:INSTALL_PSYCHOPY
cls
echo.
echo ===============================================
echo Installing PsychoPy
echo ===============================================
echo.
echo Opening PsychoPy download page in your browser...
echo.
echo Instructions:
echo 1. Download "PsychoPy Standalone" for Windows
echo 2. Double-click the downloaded file
echo 3. Follow installation wizard ^(use default settings^)
echo 4. Wait for installation to complete ^(10-15 minutes^)
echo 5. Come back here and choose option 1 to verify
echo.
pause
start https://www.psychopy.org/download.html
goto MENU

:INSTALL_PACKAGES
cls
echo.
echo ===============================================
echo Installing Python Packages
echo ===============================================
echo.
call INSTALL_DEPENDENCIES.bat
echo.
pause
goto MENU

:TEST_SETUP
cls
echo.
echo ===============================================
echo Running Complete Setup Test
echo ===============================================
echo.
call TEST_SETUP.bat
echo.
pause
goto MENU

:RUN_EXP1
cls
echo.
echo ===============================================
echo Running Experiment 1 - Simultaneous
echo ===============================================
echo.
call RUN_EXPERIMENT1.bat
goto MENU

:RUN_EXP2
cls
echo.
echo ===============================================
echo Running Experiment 2 - Sequential
echo ===============================================
echo.
call RUN_EXPERIMENT2.bat
goto MENU

:EXIT
cls
echo.
echo ===============================================
echo Thank you for using PsychoPy Experiments!
echo ===============================================
echo.
echo Need help? Read:
echo   - START_HERE.md
echo   - GABAY_CLIENT.html
echo.
pause
exit
