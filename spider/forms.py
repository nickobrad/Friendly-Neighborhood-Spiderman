from django import forms
from django.core import validators
from django.db.models import fields
from django.forms.widgets import Widget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Post, Business


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username','password1','password2' ] 

        widgets = {
            'first_name':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"First Name", 'label': 'First Name'}),
            'last_name':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"Second Name", 'label': 'Second Name'}),
            'email':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"Email Address", 'label': 'Email Address'}),
            'username':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"Username", 'label': 'Username'}),
            'password1':forms.PasswordInput(attrs = {'class':'form-control names','type':'password', 'placeholder':"Password", 'label': 'Password'}),
            'password2':forms.PasswordInput(attrs = {'class':'form-control names', 'placeholder':"Confirm Password", 'label': 'Confirm Password'}),
        }

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'details')

        widgets = {
            'title': forms.TextInput(attrs={'class':"form-control post", 'label': 'Title', 'placeholder':"Title", 'aria-label':"Title"}),
            'details' : forms.Textarea(attrs={'class':"form-control post", 'label': 'Details', 'placeholder':"Details", 'aria-label':"Details"}),
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('family_name', 'family_members', 'family_contact', 'profile_photo', 'neighborhood') 

        widgets = {
            'family_name': forms.TextInput(attrs={'class':"form-control profile", 'label': 'Family Name', 'placeholder':"Family Name", 'aria-label':"Family Name"}),
            'family_members': forms.TextInput(attrs={'class':"form-control profile", 'label': 'Number of Family Members', 'placeholder':"Number of Family Members", 'aria-label':"Number of Family Members"}),
            'family_contact': forms.TextInput(attrs={'class':"form-control profile", 'label': 'Family Contact Details', 'placeholder':"Family Contact Details", 'aria-label':"Family Contact Details"}),
            'profile_photo': forms.FileInput(attrs = {'class': 'form-control photo', 'type': 'file'}),
            'neighborhood': forms.Select(attrs={'class':"form-control profile", 'label': 'Neighborhood', 'placeholder':"Neighborhood", 'aria-label':"Neighborhood"}),
        }

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business 
        fields = ('name', 'business_logo', 'business_details', 'contact', 'neighborhood')

        widgets = {
            'name': forms.TextInput(attrs={'class':"form-control hood", 'label': 'Business Name', 'placeholder':"Business Name", 'aria-label':"Business Name"}),
            'business_details': forms.Textarea(attrs={'class':"form-control hood", 'label': 'Business Description', 'placeholder':"Business Description", 'aria-label':"Business Description"}),
            'business_logo': forms.FileInput(attrs = {'class': 'form-control hood', 'type': 'file', 'label': 'Business Logo', 'placeholder':"Business Logo", 'aria-label':"Business Logo"}),
            'contact': forms.TextInput(attrs={'class':"form-control hood", 'label': 'Reference Contact', 'placeholder':"Reference Contact", 'aria-label':"Reference Contact"}),
            'neighborhood': forms.Select(attrs={'class':"form-control hood", 'label': 'Neighborhood', 'placeholder':"Neighborhood", 'aria-label':"Neighborhood"}),
        }

