@echo off
cd /d "%~dp0"
git add .
git commit -m "update %date%"
git push
pause
