from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from models import Entry


class EntryDetailView(DetailView):
    model = Entry


class EntryListView(ListView):
    model = Entry
    context_object_name = 'entry_list'
