@echo off
title FuzzyVitals Loader - Jakub Sikora
echo ====================================================
echo   FuzzyVitals
echo   Autor: Jakub Sikora (347903)
echo ====================================================

python --version >nul 2>&1
if %errorlevel% neq 0 (
	echo [BLAD] Python nie jest zainstalowany.
	pause
    exit
)

python -m pip install streamlit numpy scipy matplotlib scikit-fuzzy networkx >nul 2>&1

start /b python -m streamlit run app.py --server.headless true

timeout /t 5 /nobreak >nul

start chrome --app=http://localhost:8502

exit