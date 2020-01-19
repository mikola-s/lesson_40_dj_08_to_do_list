from django.forms import ModelForm
from django import forms
from todo.models import Note


class CreateNoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['text']


class SearchNoteForm(forms.Form):
    search = forms.CharField(
        max_length=256,
        required=False,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Search'})
    )


class UpdateNoteStatusForm(ModelForm):
    class Meta:
        model = Note
        fields = ['status']
        labels = {'status': ''}

