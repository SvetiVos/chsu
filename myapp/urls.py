from django.urls import path
from . import views

urlpatterns = [
    path('index.html', views.index, name='index'),
    path('news.html', views.news, name='news'),
    path('soloists.html', views.soloists, name='soloists'),
    path('foto.html', views.foto, name='foto'),
    path('video.html', views.video, name='video'),
    path('contact.html', views.contact, name='contact'),
]