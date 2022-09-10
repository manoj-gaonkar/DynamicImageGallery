from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserForm
from django.contrib.auth import login as UserLogin, logout as LogoutUser, authenticate
from django.contrib.auth.models import User
from django.contrib import  messages

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'account created for {username}')
            UserLogin(request,user)
            return redirect('gallery')
        else:
            data ={
                'form': form,
            }
            return render(request, 'users/signup.html',data)
    else:
        form = UserForm()
        data = {
            'form': form,
        }
        return render(request, 'users/signup.html',data)


def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password= password)
        data = {
            'form': form,
        }
        if user is not None:
            UserLogin(request,user)
            return redirect('gallery')
        else:
            return render(request,'users/login.html',data)
    else:
        data={
            "form": form,
        }
        return render(request,'users/login.html',data)




def logout(request):
    LogoutUser(request)
    return redirect('gallery')