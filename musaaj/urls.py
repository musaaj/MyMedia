from django.urls import path
from .views import PhotoFormView, PhotoListView, PhotoDetailView, HomeView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('add/', PhotoFormView.as_view(), name='photo-add'),
    path('photos/', PhotoListView.as_view(), name='photos'),
    path('photo/<int:pk>/', PhotoDetailView.as_view(), name='photo')
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
