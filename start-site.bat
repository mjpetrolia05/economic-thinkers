@echo off
rem Serves the Great Economic Thinkers site at http://localhost:8080 and opens the home page.
rem Double-click to start; close this window (or press Ctrl+C) to stop.
cd /d "%~dp0"
python serve.py
pause
