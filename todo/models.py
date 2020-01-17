from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Собираем сайт с заметками.
# У заметки есть текст, время создания и автор.

# Если пользователь не залогинен, то отображать
# в хедере ссылки на страницы логина и регистрации,
# и надпись о том, что для использования нужно залогиниться или зарегистрироваться.


# Если пользователь залогинен, то отображать список заметок созданных
# этим пользователем с пагинацией по 10 элементов, и форму с одним полем
# текст внизу этой страницы (пользователя назначать из реквеста).
# В отображаемом списке добавить к каждой заметке кнопку удаления заметки.
# Добавить поиск по заметкам.

class Note(models.Model):
    text = models.TextField(max_length=50)
    post_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name="user", on_delete=models.SET_DEFAULT, default='NoName')