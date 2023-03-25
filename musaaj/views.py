from django.views.generic import ListView, DetailView, FormView, TemplateView
from .models import PhotoModel, VideoModel, AudioModel
from .forms import PhotoForm, VideoForm, AudioForm
from django.urls import reverse_lazy

class HomeView(TemplateView):
    template_name = 'media.html'
    context_object_name = 'media'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = PhotoModel.objects.all()[:5]
        context['videos'] = VideoModel.objects.all()[:5]
        context['audios'] = AudioModel.objects.all()[:5]
        return context


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


class VideoFormView(FormView):
    template_name = 'video_form.html'
    form_class = VideoForm
    success_url = '/videos/'

    def form_valid(self, form):
        video = form.save(commit=False)
        video.save()
        return super().form_valid(form)


class VideoListView(ListView):
    template_name = 'video_list.html'
    context_object_name = 'videos'
    model = VideoModel


class AudioFormView(FormView):
    template_name = 'audio_form.html'
    form_class = AudioForm
    success_url = '/'

    def form_valid(self, form):
        audio = form.save(commit=False)
        audio.save()
        return super().form_valid(form)

