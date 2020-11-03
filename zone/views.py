from django.shortcuts import render, redirect, get_object_or_404
from .models import Neighborhood, Profile, Business, Post 
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, BusinessForm,UpdateProfileForm, NeighborHoodForm, PostForm

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

def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile', user.username)
    else:
        form = UpdateProfileForm()
    return render(request, 'create_profile.html', {'form': form})

def profile(request, username):
    return render(request, 'profile.html')

def neighborhoods(request):
    all_hoods = Neighbourhood.objects.all()
    all_hoods = all_hoods[::-1]
    context = {
        'all_hoods': all_hoods,
    }
    return render(request, 'neighborhoods.html', context)

