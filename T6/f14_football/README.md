# Football Team Balancer

This folder contains a standalone Windows build setup for the Tkinter app.

## Run The Standalone App

If the executable was already built, open:

- `dist\FootballTeamBalancer.exe`

You can double-click the file in Windows Explorer. Python does not need to be installed on the target machine.

## Rebuild The Executable

If you change the Python source and want a fresh `.exe`:

1. Double-click `build_windows_exe.bat`
2. Wait until the build finishes
3. The new executable will be created in `dist\FootballTeamBalancer.exe`

## Files In This Folder

- `14_football_app.py` - main Tkinter source
- `build_windows_exe.bat` - rebuild script for Windows
- `assets\football.ico` - app icon used by the executable

## Notes

- The app is built with PyInstaller in one-file windowed mode.
- On some Windows systems, SmartScreen may show a warning because the executable is unsigned.
- No installation is required for normal use. Copy the `.exe` and run it.