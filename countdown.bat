@echo off
title Countdown

echo set a timer name, the time from now when you want to be notified and a notification type.
echo.

:loop
    python countdown.py
goto :loop
