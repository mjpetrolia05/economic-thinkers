@echo off
rem Publishes the site: saves every change as a new version and pushes it to GitHub.
rem GitHub Pages then updates the live site within a minute or two.
cd /d "%~dp0"
git add -A
git diff --cached --quiet && (
  echo Nothing has changed since the last publish.
  pause
  exit /b 0
)
set "msg=%~1"
if "%msg%"=="" set "msg=Update site"
git commit -m "%msg%"
git push
echo.
echo Published. The live site will update in a minute or two.
pause
