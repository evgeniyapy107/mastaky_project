from django.shortcuts import render
from . import models


def painting_index(request):
    all_paintings = models.Painting.objects.all()
    context = {
        'all_paintings': all_paintings
    }
    return render(request, 'painting_index.html', context)


def painting_detail(request, painting_id):
    painting = models.Painting.objects.get(pk=painting_id)
    about_painting = models.AboutPainting.objects.get(painting=painting)
    context = {
        'painting': painting,
        'about_painting': about_painting
    }

    return render(request, 'painting_detail.html', context)

