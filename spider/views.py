from django.http.response import Http404
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.urls.base import reverse
from .forms import RegistrationForm, PostForm, ProfileUpdateForm, BusinessForm
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile, Business, Post, Neighbourhood
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormMixin
from itertools import chain
import statistics

# Create your views here.
def register(request):

    rgf = RegistrationForm()

    if request.method == 'POST':
        rgf = RegistrationForm(request.POST)
        if rgf.is_valid():
            rgf.save()
            user = rgf.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    return render(request, 'register.html', {'rgf': rgf})

def loginuser(request):
 
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')

@login_required('')
def home(request):

    user = request.user

    posts = Post.objects.all()
    businesses = Business.objects.filter(neighborhood=user.profile.neighborhood).all()
    # businesses = Business.objects.all()
    hoods = Neighbourhood.objects.all()

    mp = Post.objects.last()
    mb = Business.objects.last()

    pf = PostForm()

    if request.method == 'POST':
        pf = PostForm(request.POST)
        if pf.is_valid(): 
            profile = Profile.objects.filter(user = user).first()
            area = profile.neighborhood
            new_post = pf.save(commit = False)
            new_post.hood = area
            new_post.posted_by = Profile.objects.get(user = request.user)
            new_post.save()
            return HttpResponseRedirect(reverse('home')) 
        else:
            pf = PostForm()

    return render(request, 'home.html', {'pf': pf, 'mb': mb, 'mp': mp, 'posts': posts, 'businesses': businesses, 'hoods': hoods})

@login_required('')
def my_profile(request):

    user = request.user

    profile = Profile.objects.get(user = request.user)
    posts = Post.objects.filter(posted_by = profile).all()
    businesses = Business.objects.filter(owner = user).all()

    title = f'{ request.user.username }\'s Profile'

    uf = ProfileUpdateForm()
    bf = BusinessForm()

    if request.method == 'POST':
        bf = BusinessForm(request.POST, request.FILES)
        if bf.is_valid():
            biz = bf.save(commit=False)
            biz.owner = user
            biz.save()
            return redirect('profile')
        else:
            bf = BusinessForm()
 
    return render (request, 'profile.html', {'title': title, 'profile': profile, 'posts': posts, 'uf': uf, 'bf': bf, 'businesses': businesses})

class UpdateProfile(LoginRequiredMixin,UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'update_profile.html'
    context_object_name = 'profile'

class UpdateBusiness(LoginRequiredMixin,UpdateView):
    model = Business
    form_class = BusinessForm
    template_name = 'update_business.html'
    context_object_name = 'business'

@login_required
def search_results(request):  

    if 'search_business' in request.GET and request.GET["search_business"]:
        search_term = request.GET.get("search_business")
        searched_business = Business.search_by_name(search_term)
        message = f"{search_term}"
        title = search_term
        return render(request, 'search.html',{"message": message, "businesses": searched_business, 'title': title})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message": message})

def logout_view(request):
    logout(request)
    return redirect('login')
