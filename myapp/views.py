from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def news(request):
    return render(request, 'news.html')

def soloists(request):
    return render(request, 'soloists.html')

def foto(request):
    return render(request, 'foto.html')

def video(request):
    return render(request, 'video.html')

def contact(request):
    return render(request, 'contact.html')

