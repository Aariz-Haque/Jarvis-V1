@echo off
setlocal enabledelayedexpansion

rem Define the name of your virtual environment
set venv_name=env

rem Check if the virtual environment exists
if exist %venv_name%\Scripts\activate (
    echo Activating virtual environment...
    call %venv_name%\Scripts\activate
) else (
    echo Virtual environment not found. Skipping activation.
)

rem Install project requirements
echo Installing project requirements...
pip install -r requirements.txt

rem Run the main.py file
echo Running main.py...
python main.py

rem Deactivate the virtual environment (if activated)
if defined VIRTUAL_ENV (
    echo Deactivating virtual environment...
    deactivate
)

echo Project execution complete.
