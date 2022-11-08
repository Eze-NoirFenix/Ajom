from django.shortcuts import render

def gallery(request):

    return render(request, 'gallery/gallery.html')

def gallery_vertical(request):

    return render(request, 'gallery/gallery-vertical.html')

def gallery_widescreen(request):

    return render(request, 'gallery/gallery-widescreen.html')