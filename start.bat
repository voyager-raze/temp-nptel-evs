@echo off
cd /d "%~dp0"
echo Starting NPTEL EVS Practice App at http://localhost:8765
echo Press Ctrl+C to stop.
python -m http.server 8765
