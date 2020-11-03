from django.shortcuts import render, redirect, get_object_or_404
from .models import Neighbourhood, Profile, Business, Post 
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request, 'index.html')