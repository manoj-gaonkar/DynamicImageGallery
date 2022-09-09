from django.shortcuts import render, redirect

def gallery(request):
    return render(request, 'gallery/gallery.html')