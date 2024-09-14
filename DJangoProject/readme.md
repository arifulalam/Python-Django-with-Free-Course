## Steps to install DJango

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

## To craete new super user, run following command and follow instruction there.
```
python manage.py createsuperuser
```

### Created following super user
```arifulalam:@cc3$5Denied```

## To change password for dJango Admin account
```
python manage.py changepassword <user_name>
```

1. Create a ``templates`` directory inside ``<application_folder>`` and create a ``index.html`` file there.
2. Create another directory ``static`` inside ``<application_folder>`` and copy any assets files (i.e: css, js, images, ico etc.).
3. Add ``{% static '<your_css_js_etc_file_location_inside_static_direcotry>' %}`` for your all ``script``, ``css``, ``images`` file location.
4. Open ``<project_directory>``/``<project_directory>``/``settings.py`` file and find ``STATIC_URL = 'static/'`` line. After this line add following lines (if are not there).
```
APP_URL = BASE_DIR
STATIC_ROOT = BASE_DIR / 'static'
```
5. In console/terminal write ``python manage.py collectstatic`` so that links get updated.
6. To create a model class in database open ``models.py`` inside ``<application_folder>`` as follows
```
class <Model_Name>(models.Model):
    <field_name> = models.<field_type>(<field_settings_comma_seperated_values>)
    <field_name> = models.<field_type>(<field_settings_comma_seperated_values>)
```
To know more about <field_type>, check [here](link=https://docs.djangoproject.com/en/5.1/ref/models/fields/#model-field-types).
7. Then we have to register all created models to ``admin.py`` so that can be migrated to database tables.
    a. First import created model to ``admin.py``.
    ```
    from .models import <model_class_name>
    ```
    b. Then register the model as follows
    ```
    admin.site.register(<>model_class_name)
    ```
8. After creating each model and/or all models (which will treated as database tables), have to run following commands one after another.
```
python manage.py makemigrations
python manage.py migrate
```