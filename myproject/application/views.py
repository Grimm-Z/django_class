from django.shortcuts import render, redirect
from .forms import NoteForm
from .models import Note
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

class NoteListView(ListView):
    model = Note
    template_name = 'notes/note_list.html'

class NoteDetailView(DetailView):
    model = Note
    template_name = 'notes/note_detail.html'

def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note-list')
    else:
        form = NoteForm()
    return render(request, 'notes/add_note.html', {'form': form})    