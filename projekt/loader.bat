@echo off
title FuzzyVitals Loader - Jakub Sikora
echo ====================================================
echo   FuzzyVitals
echo   Autor: Jakub Sikora (347903)
echo ====================================================

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [BLAD] Python nie jest zainstalowany lub nie zostal dodany do PATH.
    pause
    exit
)

echo Instalowanie wymaganych bibliotek... (to moze chwilke potrwac)
:: Usunieto ">nul 2>&1", aby widziec bledy, i dodano --user
python -m pip install --upgrade pip
python -m pip install streamlit numpy scipy matplotlib scikit-fuzzy networkx --user

if %errorlevel% neq 0 (
    echo [BLAD] Instalacja bibliotek nie powiodla sie. Przeczytaj komunikaty powyzej.
    pause
    exit
)

echo Uruchamianie aplikacji Streamlit...
start /b python -m streamlit run app.py --server.headless true

timeout /t 5 /nobreak >nul

start chrome --app=http://localhost:8501

exit