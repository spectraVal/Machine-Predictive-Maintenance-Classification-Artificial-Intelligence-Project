@echo off
title Machine Predictive Maintenance - Final Run

echo ==================================================
echo  MACHINE FAILURE CLASSIFICATION
echo  Final Experiment Run
echo ==================================================
echo  Creator: -. Muhamad Rival Maulana     (230611055)
echo           -. Isak Sabam Tambunan       (230611132)
echo ==================================================
echo.

REM --- Check virtual environment ---
if not exist venv\Scripts\python.exe (
    echo ERROR: Virtual environment not found.
    echo Please create venv and install dependencies first.
    echo.
    pause
    exit /b
)

REM --- Run final experiment ---
echo Running model...
echo.
venv\Scripts\python.exe -m final_run.main_final

echo.
echo ==================================================
echo Execution finished.
echo Output files are available in the outputs/ folder.
echo ==================================================
pause
