from django.views.generic import ListView, DetailView, FormView
from .models import PhotoModel
from .forms import PhotoForm
from django.urls import reverse_lazy
import os
from MyMedia import settings

class PhotoDetailView(DetailView):
    model = PhotoModel
    template_name = 'photo_detail.html'
    context_object_name = 'photo'


class PhotoListView(ListView):
    template_name = 'photo_list.html'
    context_object_name = 'photos'
    model = PhotoModel
    

class PhotoFormView(FormView):
    template_name = 'photo_form.html'
    form_class = PhotoForm
    success_url = '/photos/'

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.save()
        return super().form_valid(form)

