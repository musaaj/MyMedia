from django.urls import path
from .views import(
        PhotoFormView,
        PhotoListView,
        PhotoDetailView,
        HomeView,
        VideoFormView,
        VideoListView,
        AudioFormView
)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('add_photo/', PhotoFormView.as_view(), name='add_photo'),
    path('photos/', PhotoListView.as_view(), name='photos'),
    path('photo/<int:pk>/', PhotoDetailView.as_view(), name='photo'),
    path('add_video/', VideoFormView.as_view(), name='add_video'),
    path('videos/', VideoListView.as_view(), name='videos'),
    path('add_audio/', AudioFormView.as_view(), name='add_audio')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
