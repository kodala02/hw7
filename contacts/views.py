from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Contact

class ContactListView(ListView):
    model = Contact
    template_name = 'contact_list.html'
    context_object_name = 'contacts'

class ContactDetailView(DetailView):
    model = Contact
    template_name = 'contact_detail.html'
    context_object_name = 'contact'
