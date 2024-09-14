#Steps to install DJango

01. ```python -m venv <virtual_environment_name>```
02. ```. <virtual_environment_name>/Scripts/activate```
03. Type ``Y`` or ``A`` and press enter
04. ```pip install django```
05. ```python -m pip install --upgrade pip```
06. ```django-admin startproject <project_name>```
07. enter to ``<project_name>`` by ```cd <project_name>```
08. ```python manage.py startapp <application_name>```
09. open ``<project_name>/<project_name>/settings.py`` and add ``<application_name>`` as last value for ``INSTALLED_APPS`` list.
10. open ``<project_name>/<project_name>/urls.py`` and copy line *18* to *22*. Then add `, include` at the end of line *18* and add following after line *21*
```
path('', include('<application_name>.urls', name = '<application_name>'))
```
11. create ``urls.py`` file inside ``<project_name>/<application_name>`` directory and paste the copied lines. And delete *4th* line.
12. create ``templates`` directory under ``<application_name>`` directory. And create a ``index.html`` file there with basic html.
13. create a *function* in ``<application_name>/views.py`` as follows
```
def base(request):
    return render(request, 'index.html')
```
<!---12. ```python manage.py collectionstatic```-->
14. ```python manage.py runserver``` and browse ```http://localhost:8000``` in web browser