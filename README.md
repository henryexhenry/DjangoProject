# DJANGO PROJECT

## Setup enviornment
we need python3.6, pip(a package manager for python), pipenv(virtual env for python), django2.1(to be installed in venv)
```
> pip install pipenv
> cd <your project folder>
```
Then create virtual environment in current folder with django2.1 installed.
```
> pipenv install django==2.1
```
You should now have Pipfile and Pipfile.lock in your folder.

Start a project by django-admin in (.) current directory.
```
> django-admin startproject jangoProject .
```

Run django server.
```
> python manage.py runserver
```
Now you can open your browser and goto [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to check out the django server you have just created.

You should be able to see the following sentence.

```The install worked successfully! Congratulations!```