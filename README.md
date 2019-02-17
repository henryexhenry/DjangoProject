# DJANGO PROJECT

## Setup enviornment
We need to first install these packages:
- python3.6, 
- pip (a package manager for python), 
- pipenv (virtual env for python), 
- django2.1 (to be installed in venv)
```
> pip install pipenv
> cd <your new project folder>
```
Then create virtual environment in current folder with django2.1 installed.
```
> pipenv install django==2.1
```
You should now have Pipfile and Pipfile.lock in your folder.

Start a project by django-admin in (.) current directory.
```
> django-admin startproject djangoProject .
```

Run django server.
```
> python manage.py runserver
```
Now you can open your browser and goto [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to check out the django server you have just created.

You should be able to see the following sentence.

```The install worked successfully! Congratulations!```

---
## Making a Hello World App with Django
Each project may have multiple apps. Now we demonstrate the steps we need for making a Hellp World App.
### **1. Create new APP**
Create a new app named hello
```
> python manage.py startapp hello
```
Go to setting.py add the app 'hello' into INSTALLED_APP
### **2. Create new view**

Open views.py and add following function

```
from django.shortcuts import render
from django.http import HttpResponse

def myView(request):
    return HttpResponse('Hello, World')
```
### **3. Add path in url.py**

Edit url.py to add path of new view. Also import the new view function into url.py
```
from django.contrib import admin
from django.urls import path
from hello.views import myView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sayHello/', myView),
]
```

### **4. Testing**
If you finish the previous steps correctly, now you can run the server and enter the url http://127.0.0.1:8000/sayhello in your browser to see what happen.
```
> python manage.py runserver
```