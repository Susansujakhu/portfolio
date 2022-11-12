from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'resume'
urlpatterns = [
    path('', views.index, name="index"),
    path('downloads/', views.downloads, name="downloads"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)