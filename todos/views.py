from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from flask import redirect

from todos.forms import Todo_form
from .models import Todo

# Create your views here.
def todo(request):
    todos= Todo.objects.all()
    return render(request, 'todo.html', {'todos':todos})




def create(request):
    form = Todo_form(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    if request.method == 'GET':
        return render(request, 'c.html',)



def Update(request, id):
    todo= Todo.objects.get(id=id)
    form = Todo_form(request.POST, instance=todo)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    if request.method == 'GET':
        print(todo.due_date)
        return render(request, 'u.html', {'todo':todo})


def delete(request, id):
    todo= Todo.objects.get(id=id)
    todo.delete()
    return HttpResponseRedirect('/')


def detail(request, id):
    todo=Todo.objects.get(id=id)
    return render(request, 'detail.html', {'todo':todo})