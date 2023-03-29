from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .forms import CreateUserForm, CreateTodoForm, LoginForm
from .models import User, Todo
from django.contrib.auth import login, user_logged_in, get_user, logout, authenticate, user_logged_out


def sign_up(request):
    user = get_user(request)
    if user.is_authenticated:
        return redirect('/')
    if request.POST:
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    context = {'form': CreateUserForm}
    return render(request, 'signup.html', context)


def sign_in(request):
    error = None
    user = get_user(request)
    if user.is_authenticated:
        return redirect('/')
    if request.POST:
        form = LoginForm(request.POST)
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        user = authenticate(phone_number=phone_number, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error = 'Invalid credentials'
    context = {
            'form': LoginForm,
            'error': error
        }
    return render(request, 'signin.html', context)


def sign_out(request):
    if user_logged_in:
        logout(request)
        return redirect(sign_in)
    return redirect('/')


def todo_list(request):
    user = get_user(request)
    if request.POST:
        todo = Todo()
        todo.title = request.POST['title']
        todo.user_id = user
        todo.save()
    context = {
            'form': CreateTodoForm,
            'todos': Todo.objects.filter(user_id=user)
        }
    return render(request, 'todo_list.html', context)
