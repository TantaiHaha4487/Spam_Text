@echo off
:someRoutine
setlocal
:%@Try%
  python start.py
%@EndTry%
:@Catch
  start https://www.python.org/downloads/
  echo You don't have python Please dowload and install
  echo next Time if you want to use Plaese Open "spame.bat
:@EndCatch
echo Install Finish!!
pause