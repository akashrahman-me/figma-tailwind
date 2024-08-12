@echo off

REM Activate the virtual environment (using relative path)
call %~dp0\.venv\Scripts\activate.bat

REM Run your Python script (using relative path)
python %~dp0\theme_gen.py

REM Wait for 2 seconds before closing the terminal
timeout /t 2 /nobreak >nul

REM Close the terminal
exit
