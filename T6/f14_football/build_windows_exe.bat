@echo off
setlocal

set PYTHON_EXE=C:\Users\mniedziolka\AppData\Local\Programs\Python\Python310\python.exe
set APP_DIR=%~dp0
set ICON_FILE=%APP_DIR%assets\football.ico

pushd "%APP_DIR%"
"%PYTHON_EXE%" -m PyInstaller --noconfirm --clean --onefile --windowed --icon "%ICON_FILE%" --name FootballTeamBalancer 14_football_app.py
popd

echo.
echo Build finished. Executable is in dist\FootballTeamBalancer.exe
pause