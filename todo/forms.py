from django.forms import ModelForm
from django import forms
from todo.models import Note


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['text']
