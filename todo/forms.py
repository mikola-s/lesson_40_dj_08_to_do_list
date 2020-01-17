from django.forms import ModelForm
from todo.models import Note


class CreateNoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['author', 'text']
