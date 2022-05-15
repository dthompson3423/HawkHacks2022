from django.shortcuts import render
from .models import Video

# Create your views here.
def index(request):
    videos = Video.objects.all()
    return render(request, 'Videos/index.html', context={'videos': videos})

    