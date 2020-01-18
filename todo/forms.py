from django.forms import ModelForm
from todo.models import Note


class CreateNoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['text']

    # def __init__(self, author_id, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.author_id = author_id
