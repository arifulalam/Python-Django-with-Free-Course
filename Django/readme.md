1. In terminal run ``python -m venv <virtual_environment_name>``
2. Run ``. <virtual_environment_name>/Scripts/activate``
3. Type `Y` or `A` and press ``[Enter]``
4. Run ``pip install django``
5. Run ``python -m pip install --upgrade pip``
6. Run ``django-admin startproject <project-name>``
7. Run ``cd <project-name>``
8. Run ``python manage.py startapp <application-name>``
9. Open ``<project-name>/<project-name>/settings.py`` and find
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
Add ``<application-name>`` at the end
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    '<application-name>',
]
```

then find ``STATIC_URL = 'static/'``
and add following after above
```
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
```
Also create two directories `media` and `static` inside `<project-name>/<application-name>` directory

10. Run `python manage.py collectstatic`. Run this every time new static files (i.e.: js, css, images, etc.) added to /static/ directory
11. Open `<project-name>/<project-name>/urls.py` and change following lines.
```
from django.urls import path
```
to
```
from django.urls import path, include
```
and
```
urlpatterns = [
    path('admin/', admin.site.urls),
]
```
to
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('<application-name>.urls'), name='<application-name>')
]
```
12. Create a file `urls.py` inside `<application-name>` and following lines
```
from django.urls import path

urlpatterns = []
```
13. Create a directory `templates` inside `<application-name>` directory.
14. To activate django admin panel,
    <br/>a. Run `python manage.py makemigrations`
    <br/>b. Run `python manage.py migrate`
    <br/>c. Run `python manage.py createsuperuser` and follow instruction there to create a admin user.
15. Run ``python manage.py runserver [port](optional)`` to run **server** and **project** and press ``[ctrl]`` + ``[c]`` and `y`, then ``[Enter]`` to stop **server** and **project**
16. To browse project, in browser visit http://127.0.0.1:8000 and for admin panel visit http://127.0.0.1:8000/admin/. If different port number used to run server, then have to use that port in url (i.e.: `http://127.0.0.1:<defined_port>`)
17. create `index.html`, `about.html` and `masterpage.html` files to `<application-name>/templates` directory and directories with `style.css` at `<application-name>\static\assets\css\style.css`
    <br/>a. `index.html` is for home page content.
    <br/>b. `about.html` is for about page content.
    <br/>c. `masterpage.html` is for container content which will hold all the common html part to avoid repeation of codes.