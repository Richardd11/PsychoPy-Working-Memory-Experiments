@echo off
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║                                                               ║
echo ║         CSV TO EXCEL ENHANCER                                 ║
echo ║         Convert raw CSV to beautiful Excel with colors!       ║
echo ║                                                               ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.
echo This will convert your CSV data files to formatted Excel files
echo with colors, borders, and centered text!
echo.
echo Features:
echo   • Color-coded headers
echo   • Alternating row colors
echo   • Green for correct answers
echo   • Red for incorrect answers
echo   • Centered text
echo   • Auto-sized columns
echo   • Summary statistics sheet
echo.
echo ═══════════════════════════════════════════════════════════════
echo.

cd /d "%~dp0"
python enhance_data.py

pause
