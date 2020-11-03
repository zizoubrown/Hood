from django.shortcuts import render, redirect, get_object_or_404
from .models import Neighbourhood, Profile, Business, Post 
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, BusinessForm,UpdateProfileForm, NeighbourHoodForm, PostForm

# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})