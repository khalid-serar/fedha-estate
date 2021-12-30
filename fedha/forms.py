from .models import Business, Neighbourhood, Profile, Post
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# The signup form
class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=300, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class NewNeighbourHood(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ('user','occupants_count')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'profile_picture', 'bio']

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('user', 'neighbourhood')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'neighbourhood')   