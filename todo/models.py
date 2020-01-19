from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import localtime


class Note(models.Model):
    text = models.TextField(max_length=200)
    post_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        text = self.text if len(self.text) < 30 else self.text[:19:]
        time = localtime(self.post_time).strftime("%H:%M:%S %Y-%m-%d")
        return f"{self.author} / {text} / {time}"
