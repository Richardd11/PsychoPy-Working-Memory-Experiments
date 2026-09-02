@echo off
setlocal
cd /d "%~dp0"
title PsychoPy Experiment Launcher

set "EXPERIMENT_FILE=%~1"
set "EXPERIMENT_NAME=%~2"
set "PSYCHOPY_PYTHON="

if not defined EXPERIMENT_FILE goto INVALID_REQUEST
if not exist "%EXPERIMENT_FILE%" goto INVALID_REQUEST

call :CHECK_PYTHON "%ProgramFiles%\PsychoPy\python.exe"
call :CHECK_PYTHON "%ProgramFiles%\PsychoPy3\python.exe"
call :CHECK_PYTHON "%ProgramFiles(x86)%\PsychoPy\python.exe"
call :CHECK_PYTHON "%ProgramFiles(x86)%\PsychoPy3\python.exe"
call :CHECK_PYTHON "%LOCALAPPDATA%\Programs\PsychoPy\python.exe"
call :CHECK_PYTHON "%LOCALAPPDATA%\PsychoPy\python.exe"

for /f "delims=" %%P in ('where python 2^>nul') do call :CHECK_PYTHON "%%P"
for /f "delims=" %%P in ('where python3 2^>nul') do call :CHECK_PYTHON "%%P"

if not defined PSYCHOPY_PYTHON goto PSYCHOPY_NOT_FOUND
if /I "%~3"=="--check-only" (
    echo PsychoPy interpreter: %PSYCHOPY_PYTHON%
    exit /b 0
)

echo ===============================================
echo %EXPERIMENT_NAME%
echo ===============================================
echo.
echo Starting automatically. Please wait...
echo.
"%PSYCHOPY_PYTHON%" -u "%~dp0experiment_launcher.py" "%~dp0%EXPERIMENT_FILE%"
set "RUN_RESULT=%ERRORLEVEL%"

if "%RUN_RESULT%"=="0" goto FINISHED
echo.
echo ===============================================
echo The experiment stopped because of an error.
echo ===============================================
echo.
echo Please send the latest file inside the logs folder
echo to the researcher. No technical troubleshooting is needed.
echo.
pause
exit /b %RUN_RESULT%

:FINISHED
echo.
echo Experiment finished. Data is saved in the data folder.
timeout /t 3 /nobreak >nul
exit /b 0

:CHECK_PYTHON
if defined PSYCHOPY_PYTHON exit /b 0
echo(%~1| findstr /I /C:"\WindowsApps\" >nul && exit /b 0
if not exist "%~1" exit /b 0
"%~1" -c "import psychopy" >nul 2>&1
if not errorlevel 1 set "PSYCHOPY_PYTHON=%~1"
exit /b 0

:PSYCHOPY_NOT_FOUND
echo PsychoPy Standalone was not found on this computer.
powershell -NoProfile -ExecutionPolicy Bypass -Command "Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show('PsychoPy Standalone was not found. Please install PsychoPy, then double-click this experiment again.','PsychoPy is required','OK','Error')" >nul 2>&1
echo.
echo Download PsychoPy from: https://www.psychopy.org/download.html
echo.
pause
exit /b 1

:INVALID_REQUEST
echo The experiment package is incomplete. Please download and extract it again.
pause
exit /b 1
