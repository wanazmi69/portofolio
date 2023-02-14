from django.shortcuts import render
import scrapetube
from django.http import JsonResponse


def index(request):

    videos = scrapetube.get_channel("UCkIMvxd6hyQAJ_vRrgwjIEg")

    context = {
        'videos': videos
    }
    return render(request, 'index.html', context)

def project(request):
    return render(request, 'projects.html')




def error_404_view(request, exception):

    return render(request, 'error-page.html')
