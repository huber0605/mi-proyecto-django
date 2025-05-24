
@echo off
cd /d "%~dp0"
call mi_entorno\Scripts\activate.bat
pyinstaller --noconsole --onefile --add-data "crm\static;crm\static" --add-data "crm\templates;crm\templates" --add-data "db.sqlite3;." --add-data "manage.py;." --icon=icono.ico app.py
pause
