@echo off
color 2
set loop=0
set loopmax=999

:PROMPT
SET /P AREYOUSURE=Create "%loopmax%" files (Y/[N])?
IF /I "%AREYOUSURE%" NEQ "Y" GOTO END

:loop
@echo on
@echo %random%> %random%.txt
set /a loop=%loop%+1 
if "%loop%"=="%loopmax%" goto next
goto loop

:next
@echo off
cls
echo Erfolgreich "%loop%" Dateien Erstellt!
pause
goto END

:END
exit
