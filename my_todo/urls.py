from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import sign_up, todo_list, sign_out, sign_in


urlpatterns=[
        path('', login_required(todo_list), name='todo'),
        path('accounts/signup/', sign_up, name='sign_up'),
        path('accounts/logout/', login_required(sign_out), name='logout'),
        path('accounts/login/', sign_in, name='login'),
    ]
