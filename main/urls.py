from django.contrib import admin
from django.urls import path, include
from . import views
import lawboard.views 


urlpatterns = [
    path('', views.home, name="home"),
    path('lawboard/', include('lawboard.urls')),
  
]
