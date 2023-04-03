from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .forms import CreateUserForm, CreateTodoForm, LoginForm, PErrorList
from .models import User, Todo
from django.contrib.auth import login, get_user, logout, authenticate


def sign_up(request):
    user = get_user(request)
    if user.is_authenticated:
        return redirect('/')
    if request.POST:
        form = CreateUserForm(request.POST, error_class=PErrorList)
        if form.is_valid():
            print('valid')
            user = form.save()
            if user is None:
                print(user)
            login(request, user)
            return redirect('/')
        else:
            context = {'form': form}
            return render(request, 'signup.html', context)
    context = {'form': CreateUserForm}
    return render(request, 'signup.html', context)


def sign_in(request):
    error = None
    user = get_user(request)
    if user.is_authenticated:
        return redirect('/')
    if request.POST:
        form = LoginForm(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
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
    user = get_user(request)
    if user.is_authenticated:
        logout(request)
    return redirect(sign_in)


def todo_list(request):
    user = get_user(request)
    if request.POST:
        todo = Todo()
        todo.title = request.POST['title']
        todo.user_id = user
        todo.save()
    context = {
            'form': CreateTodoForm,
            'todos': Todo.objects.filter(user_id=user).order_by('-created_at')
        }
    return render(request, 'todo_list.html', context)


def delete_todo(request, pk):
    Todo.objects.filter(pk=pk).delete()
    return redirect('/')


def check(request, pk):
    todo = Todo.objects.get(pk=pk)
    if todo.done:
        todo.done = False
    else:
        todo.done = True
    todo.save()
    return redirect('/')


def edit_todo(request, pk):
    user = get_user(request)
    todo = Todo.objects.get(pk=pk)
    if request.POST:
        todo.title = request.POST['title']
        todo.save()
        return redirect('/')
    context = {
            'user': user,
            'todo': todo
        }
    return render(request, 'todo_edit.html', context)
    
