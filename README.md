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

## make a todo app
### 1. Start a new app
```
> python manage.py startapp todo
```
### 2. Create template
- create new folder
```
> mkdir template
```
- add new file todo.html
```
<h1> this is a todView! <h1>
```
- add todo.html in djangoProject/setting
```
'DIRS': [os.path.join(BASE_DIR, 'templates')]
```
### 3. View
```
from django.shortcuts import render
from django.http import HttpResponse

def myView(request):
    return render(request, 'todo.html')
```
### 4. Add todo list in todo.html
```
<ul>
    <li> todo list 1
    <li> todo list 2
</ul>
```
### 5. Create model (sqlite)
- models.py
    ```
    class TodoItem(models.Model):
        content = models.TextField()
    ```
- create migration file
    ```
    > python manage.py makemigrations
    ```
    to change the configuration of our database.

    To execute the changing:
    ```
    > python manage.py migrate
    ```
- interact with the model
    ```
    > python manage.py shell
    ```
    ```
    >>> from todo.models import TodoItem
    ```
    - Create item
        ```
        a = TodoItem(content = 'permanent todo item A')
        a.save()
        ```
    - Retrive item
        ```
        allItems = TodoItem.objects.all()
        ```
    - Delete item
        ```
        allItems[0].delete()
        ```

### 6. Pass the items from model to view
view.py
```
from .models import TodoItem

def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html',
    {'all_items': all_todo_items})
```
### 7. Pass the items from view to template
todo.html
```
<ul>
    {% for todo_item in all_items %}
        <li>{{ todo_item.content }}</li>
    {% endfor %}
</ul>
```
### 8. Configure urls.py
Add new template and function in urls.py
### 9. Create form
> action="/addTodo"
"/addTodo" is url string
django will look for urlpatterns to find respective function (addTodo), the addTodo function is imported from view.py


