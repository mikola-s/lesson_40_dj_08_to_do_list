from django.urls import path, include
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('share_note_list', views.PublicNoteList.as_view(), name='public_note_list'),
    path('create_note/', views.CreateNote.as_view(), name='create_note'),
    path('delete_note/<int:pk>', views.DeleteNote.as_view(), name='delete_note'),
    path('update_note_status/<int:pk>', views.UpdateNoteStatus.as_view(), name='update_note_status'),
    path('register/', views.CreateUser.as_view(), name='create'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
]
