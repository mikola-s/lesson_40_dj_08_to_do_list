from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, TemplateView, LogoutView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView

from . import models
from . import forms


class SearchNoteFormMixin:
    """ for classes Index, PublicNoteList """

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context.update({
            'search_note_form': forms.SearchNoteForm(self.request.GET),
        })
        return context


class Index(SearchNoteFormMixin, ListView):
    template_name = 'todo/index.html'
    http_method_names = ['get', 'post']
    model = models.Note
    context_object_name = 'notes'
    paginate_by = 10
    ordering = '-post_time'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(author_id=self.request.user.pk)
        search = self.request.GET.get('search')
        qs = qs.filter(text__contains=search) if search else qs
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)

        context.update({'create_note_form': forms.CreateNoteForm,
                        'update_note_status': forms.UpdateNoteStatusForm,
                        })
        return context


class PublicNoteList(SearchNoteFormMixin, ListView):
    template_name = 'todo/public_note_list.html'
    http_method_names = ['get', 'post']
    model = models.Note
    context_object_name = 'notes'
    paginate_by = 10
    ordering = '-post_time'
    queryset = model.objects.filter(status=True)

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get('search')
        qs = qs.filter(text__contains=search) if search else qs
        return qs


class CreateUser(CreateView):
    template_name = 'todo/register.html'
    form_class = UserCreationForm
    success_url = '/'

    def form_valid(self, form):
        data = super().form_valid(form)
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return data


class CreateNote(CreateView):
    template_name = 'todo/create_note.html'
    form_class = forms.CreateNoteForm
    success_url = '/'

    def form_valid(self, form):
        form_with_user_pk = form.save(commit=False)
        form_with_user_pk.author_id = self.request.user.pk
        return super().form_valid(form)


class Login(LoginView):
    template_name = 'todo/login.html'
    success_url = '/'


class Logout(LogoutView):
    template_name = 'todo/logout.html'
    next_page = '/'


class DeleteNote(DeleteView):
    model = models.Note
    template_name = 'todo/delete_note.html'
    success_url = '/'


class SearchNote(FormView):
    form_class = forms.Note
    http_method_names = ['get']
    template_name = 'todo/index.html'


class UpdateNoteStatus(UpdateView):
    form_class = forms.UpdateNoteStatusForm
    model = models.Note
    template_name = 'todo/update_note_status.html'
    success_url = '/'

    def get_success_url(self):
        url = super().get_success_url()
        success_url = self.request.POST.get('success_url')
        return success_url if success_url else url
