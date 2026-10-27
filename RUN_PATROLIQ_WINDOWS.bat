@echo off
cd /d %~dp0
echo === PatrolIQ setup and launch ===
where py >nul 2>nul
if errorlevel 1 (echo Python launcher 'py' not found. Install Python and enable Add Python to PATH. & pause & exit /b 1)
if not exist .venv py -m venv .venv
call .venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 (echo Dependency installation failed. Check internet and Python version. & pause & exit /b 1)
streamlit run app.py
pause
