from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import Http404
from django.http.response import HttpResponseRedirect
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import NotesForm
from .models import Note

class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = '/smart/notes'
    template_name = 'notes/note_delete.html'
    login_url = "/admin"
    
class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    success_url = '/smart/notes'
    form_class = NotesForm
    login_url = "/admin"

class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Note
    success_url = '/smart/notes'
    form_class = NotesForm
    login_url = "/login"
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    
    
class NotesListView(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    login_url = "/login"
    
    def get_queryset(self):
        return self.request.user.notes.all()

class NotesDetailView(LoginRequiredMixin, DetailView):
    model = Note
    context_object_name = 'note'
    template_name = 'notes/notes_detail.html'
    login_url = "/login"

    
    
    
