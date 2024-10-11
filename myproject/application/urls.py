from django.urls import path
from . import views
from .views import NoteDetailView, NoteListView
urlpatterns = [
    path('add/', views.add_note, name="add_note"),
    path('note/', NoteListView.as_view(), name="note_list"),
    path('note_detail/', NoteDetailView.as_view(), name="note_detail"),
]