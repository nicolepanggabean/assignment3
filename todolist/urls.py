from django.urls import path
from todolist.views import show_todolist, register, login_user, logout_user, new_task, show_json, show_ajax


app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task', new_task, name='new_task'),
    path('json/', show_json, name='show_json'),
    path('ajax/', show_ajax, name="show_ajax")
]
