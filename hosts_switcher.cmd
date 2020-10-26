@echo off & setlocal enabledelayedexpansion

if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)

set hosts=%windir%\system32\drivers\etc\hosts

echo Please choose site

echo 1 is for UA
echo 2 is for UK
echo 3 is for GTM (default auto location detection mode)

set /p input= Enter your choice :
if %input%==1 (
findstr /i /v "10.20.30.40" %hosts% >%temp%\hostback.txt
type %temp%\hostback.txt >%hosts%
echo 10.20.30.40 mysite.com >>%hosts%
findstr /i /v "15.25.35.45" %hosts% >%temp%\hostback.txt
type %temp%\hostback.txt >%hosts%
echo 15.25.35.45 my-new.site.com >>%hosts%
findstr /i /v "16.26.36.46" %hosts% >%temp%\hostback.txt

type %temp%\hostback.txt >%hosts%
echo #16.26.36.46 my-new.site.com >>%hosts%
findstr /i /v "17.27.37.47" %hosts% >%temp%\hostback.txt

type %temp%\hostback.txt >%hosts%
echo #17.27.37.47 mysite.com >>%hosts%
echo done!!

Echo.. checking and confirming..
findstr /i /B "10.20.30.40" %hosts%>nul
if %errorlevel% == 1 (
echo Something is wrong with 10.20.30.40
pause
)
findstr /i /B "15.25.35.45" %hosts%>nul
if %errorlevel% == 1 (
echo Something is wrong with 15.25.35.45
pause
)
findstr /i /B "#16.26.36.46" %hosts%>nul
if %errorlevel% == 1 (
echo Something is wrong with 16.26.36.46
pause
)
findstr /i /B "#17.27.37.47" %hosts%>nul
if %errorlevel% == 1 (
echo Something is wrong with 17.27.37.47
pause
)
echo.
)

if %input%==2 (
findstr /i /v "16.26.36.46" %hosts% >%temp%\hostback.txt
type %temp%\hostback.txt >%hosts%
echo 16.26.36.46 my-new.site.com >>%hosts%
findstr /i /v "17.27.37.47" %hosts% >%temp%\hostback.txt
type %temp%\hostback.txt >%hosts%
echo 17.27.37.47 mysite.com >>%hosts%
findstr /i /v "10.20.30.40" %hosts% >%temp%\hostback.txt

type %temp%\hostback.txt >%hosts%
echo #10.20.30.40 mysite.com >>%hosts%
findstr /i /v "15.25.35.45" %hosts% >%temp%\hostback.txt

type %temp%\hostback.txt >%hosts%
echo #15.25.35.45 my-new.site.com >>%hosts%
echo done!!

Echo.. checking and confirming..
findstr /i /B "16.26.36.46" %hosts%>nul
if %errorlevel% == 1 (
echo Something is wrong with 16.26.36.46
pause
)
findstr /i /B "17.27.37.47" %hosts%>nul
if %errorlevel% == 1 (
echo Something is wrong with 17.27.37.47
pause
)
findstr /i /B "#10.20.30.40" %hosts%>nul
if %errorlevel% == 1 (
echo Something is wrong with 10.20.30.40
pause
)
findstr /i /B "#15.25.35.45" %hosts%>nul
if %errorlevel% == 1 (
echo Something is wrong with 15.25.35.45
pause
)
echo.
)

if %input%==3 (
findstr /i /v "16.26.36.46" %hosts% >%temp%\hostback.txt

type %temp%\hostback.txt >%hosts%
echo #16.26.36.46 my-new.site.com >>%hosts%
findstr /i /v "17.27.37.47" %hosts% >%temp%\hostback.txt

type %temp%\hostback.txt >%hosts%
echo #17.27.37.47 mysite.com >>%hosts%
findstr /i /v "10.20.30.40" %hosts% >%temp%\hostback.txt

type %temp%\hostback.txt >%hosts%
echo #10.20.30.40 mysite.com >>%hosts%
findstr /i /v "15.25.35.45" %hosts% >%temp%\hostback.txt

type %temp%\hostback.txt >%hosts%
echo #15.25.35.45my-new.site.com >>%hosts%
echo done!!

Echo.. checking and confirming..
findstr /i /B "#16.26.36.46" %hosts%>nul
if %errorlevel% == 1 (
echo Something is wrong with 16.26.36.46
pause
exit /b
)
findstr /i /B "#17.27.37.47" %hosts%>nul
if %errorlevel% == 1 (
echo Something is wrong with 17.27.37.47
pause
exit /b
)
findstr /i /B "#10.20.30.40" %hosts%>nul
if %errorlevel% == 1 (
echo Something is wrong with 10.20.30.40
pause
exit /b
)
findstr /i /B "#15.25.35.45" %hosts%>nul
if %errorlevel% == 1 (
echo Something is wrong with 15.25.35.45
pause
exit /b
)
echo.
)

findstr /i /B "10.20.30.40" %hosts%>nul
if %errorlevel% == 0 (
echo UA entry 10.20.30.40 is active.
)

findstr /i /B "#10.20.30.40" %hosts%>nul
if %errorlevel% == 0 (
echo UA entry 10.20.30.40 is inactive.
)
echo.

findstr /i /B "15.25.35.45" %hosts%>nul
if %errorlevel% == 0 (
echo UA entry 15.25.35.45 is active.
)

findstr /i /B "#15.25.35.45" %hosts%>nul
if %errorlevel% == 0 (
echo UA entry 15.25.35.45 is inactive.
)
echo.

findstr /i /B "16.26.36.46" %hosts%>nul
if %errorlevel% == 0 (
echo UK entry 16.26.36.46 is active.
)

findstr /i /B "#16.26.36.46" %hosts%>nul
if %errorlevel% == 0 (
echo UK entry 16.26.36.46 is inactive.
)
echo.

findstr /i /B "17.27.37.47" %hosts%>nul
if %errorlevel% == 0 (
echo UK entry 17.27.37.47 is active.
)

findstr /i /B "#17.27.37.47" %hosts%>nul
if %errorlevel% == 0 (
echo UK entry 17.27.37.47 is inactive.
)
echo.

echo off

echo Flushing DNS cache...

ipconfig /flushdns
pause
