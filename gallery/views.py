from django.shortcuts import render
from .models import Image


def gallery(request):
    images = Image.objects.all()
    return render(request, 'gallery/gallery.html', {'images': images})
