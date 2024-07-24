from django.shortcuts import render
from django.http import Http404
from django.views.generic import DetailView, ListView, CreateView

from .forms import NotesForm
from .models import Note

class NotesCreateView(CreateView):
    model = Note
    success_url = '/smart/notes'
    form_class = NotesForm
    
class NotesListView(ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'

class NotesDetailView(DetailView):
    model = Note
    context_object_name = 'note'
    template_name = 'notes/notes_detail.html'
    
    
