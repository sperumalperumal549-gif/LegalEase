@echo off
cd /d "%~dp0"
if exist venv\Scripts\activate.bat call venv\Scripts\activate.bat
start "LegalEase Backend" cmd /k uvicorn legalEaseAPI.main:app --port 8000
timeout /t 4 >nul
streamlit run frontend/app.py
