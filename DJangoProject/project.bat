@echo off

set /P vname="Enter Virutal Environment Name: "
set /P project="Enter Project Name: "
set /P app="Enter App Name: "

python -m venv %vname%

::. %vname%/Scripts/activate

pip install --no-cache-dir django

set /P update_pip="Need to update pip? (Y/N): "

IF %update_pip% == "Y" (
    python -m pip install --upgrade pip
)

django-admin startproject %project%

cd %project%

python manage.py startapp %app%

::
echo "Now run following to start Python Server"
echo "python manage.py runserver"

pause