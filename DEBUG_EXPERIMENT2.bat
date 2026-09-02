@echo off
echo ===============================================
echo EXPERIMENT 2 - DEBUG MODE
echo ===============================================
echo.
echo This will run the experiment with verbose output
echo to help diagnose any issues.
echo.
echo Press Ctrl+C to cancel, or
pause
echo.
echo Starting experiment in DEBUG mode...
echo.
python -u experiment2_sequential.py 2>&1
echo.
echo ===============================================
echo Experiment finished or encountered an error
echo ===============================================
echo.
echo If the window closed immediately, check the error messages above.
echo.
pause
