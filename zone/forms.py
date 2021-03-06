from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Neighborhood, Profile, Post, Business


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    email = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'neighborhood')


class NeighborHoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude = ('admin',)


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('user', 'neighborhood')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'hood')