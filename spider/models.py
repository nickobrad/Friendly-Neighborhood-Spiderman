from django.db import models
from cloudinary.uploader import upload
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.db.models.fields.reverse_related import ManyToOneRel
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    occupants = models.IntegerField(default= 0)

    def __str__(self) -> str:
        return self.name 
 
    def save_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def update_neighborhood_name(cls, neighborhood_id, new_name):
        hood = cls.objects.filter(id = neighborhood_id).update(name = new_name)
        return hood
    
    @classmethod
    def update_neighborhood_occupants(cls, neighborhood_id, new_number):
        hood = cls.objects.filter(id = neighborhood_id).update(occupants = new_number)
        return hood

    @classmethod
    def find_neighborhood(cls,search_term):
        hood = cls.objects.filter(name__icontains = search_term)
        return hood

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    family_name = models.CharField(max_length=50, null = True, blank = True)
    family_members = models.IntegerField(default = 2, blank = True, null = True)
    family_contact = models.CharField(max_length=50)
    profile_photo = CloudinaryField('image', blank = True, default = '')
    neighborhood = models.ForeignKey(Neighbourhood, null = True, blank = True, on_delete=models.DO_NOTHING, related_name='myhood')
    created = models.DateTimeField(auto_now_add=True) 

    def get_absolute_url(self):
        return reverse('profile')

    def __str__(self) -> str:
        return self.user.username 

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def update_profile(cls, profile_id, new_name):
        profile = cls.objects.filter(id = profile_id).update(family_name = new_name)
        return profile

    @classmethod
    def search_by_username(cls,search_term):
        users = cls.objects.filter(user__username__icontains = search_term)
        return users


class Post(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null=True, blank = True)
    posted_by = models.ForeignKey(Profile, null = True, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title  

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()


class Business(models.Model):
    name = models.CharField(max_length=100)
    business_logo = CloudinaryField('image', default = '/static/images/linkerd.svg')
    business_details = models.TextField(null = True)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    neighborhood = models.ForeignKey(Neighbourhood, null = True, on_delete=models.DO_NOTHING)
    contact = models.EmailField()

    def get_absolute_url(self):
        return reverse('profile')

    def __str__(self) -> str:
        return self.name 
 
    def save_business(self):
        self.save()

    def delete_business(self): 
        self.delete()

    @classmethod
    def update_business_name(cls, business_id, new_name):
        business = cls.objects.filter(id = business_id).update(name = new_name)
        return business

    @classmethod
    def search_by_name(cls,search_term):
        business = cls.objects.filter(name__icontains = search_term)
        return business 