from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import UpdateBusiness, register, loginuser, home, logout_view, my_profile, search_results,UpdateProfile

urlpatterns = [
    path('register/', register, name = 'register'),  
    path('', loginuser, name = 'login' ),
    path('home', home, name = 'home'),
    path('profile', my_profile, name = 'profile'),
    path('profile/update/<int:pk>', UpdateProfile.as_view(), name = 'updateprofile'),
    path('business/update/<int:pk>', UpdateBusiness.as_view(), name = 'updatebusiness'),
    path('search/', search_results, name = 'search_business'),
    path('logout/', logout_view, name = 'logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
