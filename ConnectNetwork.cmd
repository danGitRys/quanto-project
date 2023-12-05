@echo off

set "flag="

:loop
if "%1"=="" goto execute
if "%1"=="-c" set "flag=create"
shift
goto loop

:execute
if "%flag%"=="create" (
    docker network create --subnet=172.20.0.0/16 PMTNET
    docker network connect --ip 127.20.0.2/16 PMTNET dbserver
    docker network connect --ip 127.20.0.3/16 PMTNET djangoserver
) else (
    docker network connect --ip 127.20.0.2/16 PMTNET dbserver
    docker network connect --ip 127.20.0.3/16 PMTNET djangoserver
)