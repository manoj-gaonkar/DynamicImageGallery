from django.shortcuts import render, redirect
from .forms import ImagesForm
from .models import Images
from django.contrib.auth.models import User
import os

def gallery(request):
    form = ImagesForm()
    print(request.user.id)
    if request.method == "POST":
        form = ImagesForm(request.POST,request.FILES)
        if form.is_valid():
            current = form.save(commit=False)
            current.user = request.user
            current.save()
            return redirect('gallery')
    else:
        imageobj = Images.objects.filter(user = request.user.id)
        data ={
            'form': form,
            'imageobj': imageobj,
        }
    return render(request, 'gallery/gallery.html',data)


def delete(request,pk):
    deleteobj = Images.objects.get(id=pk)
    if len(deleteobj.image) > 0:
        os.remove(deleteobj.image.path)
    deleteobj.delete()
    return redirect('gallery')