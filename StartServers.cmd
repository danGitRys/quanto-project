@echo off

set "flag="

:loop
if "%1"=="" goto execute
if "%1"=="-b" set "flag=backend"
if "%1"=="-f" set "flag=frontend"
if "%1"=="-baran" set "flag=baran"
if "%1"=="-michele" set "flag=michele"
shift
goto loop

:execute
if "%flag%"=="backend" (
    start cmd.exe /k "cd ..\venv\quanto\Scripts && activate && cd ..\..\..\quanto-project\backend && python manage.py runserver"
) else (
    if "%flag%"=="frontend" (
        start cmd.exe /k "cd frontend\quanto-front && npm run dev"
    ) else (
        if "%flag%"=="baran" (
            start cmd.exe /k "cd ..\venv\quanto\Scripts && activate && cd ..\..\..\quanto-project\backend && python manage.py runserver --setting=quantoserver.settings.baran"
            start cmd.exe /k "cd frontend\quanto-front && npm run dev"
        ) else (
            if "%flag%"=="michele" (
                start cmd.exe /k "cd ..\venv\quanto\Scripts && activate && cd ..\..\..\quanto-project\backend && python manage.py runserver --setting=quantoserver.settings.michele"
                start cmd.exe /k "cd frontend\quanto-front && npm run dev"
            ) else (
                start cmd.exe /k "cd ..\venv\quanto\Scripts && activate && cd ..\..\..\quanto-project\backend && python manage.py runserver"
                start cmd.exe /k "cd frontend\quanto-front && npm run dev"
            )
        )
    )
)
