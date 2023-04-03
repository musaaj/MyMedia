from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import sign_up, todo_list, sign_out, sign_in, delete_todo, edit_todo, check


urlpatterns=[
        path('', login_required(todo_list), name='todo'),
        path('edit/<int:pk>', login_required(edit_todo), name='edit'),
        path('delete/<int:pk>', login_required(delete_todo), name='delete'),
        path('check/<int:pk>', login_required(check), name='check'),
        path('accounts/signup/', sign_up, name='signup'),
        path('logout/', login_required(sign_out), name='logout'),
        path('accounts/login/', sign_in, name='login'),
    ]
