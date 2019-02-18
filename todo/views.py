from django.shortcuts import render
from .models import TodoItem 
from django.http import HttpResponseRedirect
# Create your views here.

def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html',
    {'all_items': all_todo_items})

def addTodo(request):
    new_item = TodoItem(content = request.POST[name])
    new_item.save()
    return HttpResponseRedirect('todo/')