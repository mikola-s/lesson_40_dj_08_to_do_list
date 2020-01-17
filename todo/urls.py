from django.urls import path, include
from . import views


app_name = 'todo'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('register/', views.CreateUser.as_view(), name='create'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('create_note/', views.CreateNote.as_view(), name='create_note'),
]
