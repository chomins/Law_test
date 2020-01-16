from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
import operator


def home(request):
    posts=LawBoard.objects.all()
    posts.reverse()
    posts = posts[0:3]

    return render(request, 'home.html', {'latest':posts})


