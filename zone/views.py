from django.shortcuts import render, redirect, get_object_or_404
from .models import Neighbourhood, Profile, Business, Post 
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')