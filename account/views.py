from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from detail_board.models import *

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
               

                return redirect('login')
        else:
            return render(request, 'signup.html', {'error': 'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'signup.html')
    return render(request, 'home.html')


def logout(request):
    auth.logout(request)
    return render(request,'login.html')

def mypage(request, pk):
    mypage = User.objects.get(pk=pk)
    lawboard = User.objects.get(username= request.user.username)
    scrapped_lawboard = lawboard.LawBoard_scrap.all()
    
    scrapped_family=request.user.family_scrap.all()
    scrapped_traffic=request.user.traffic_scrap.all()
    scrapped_government=request.user.government_scrap.all()
    scrapped_army=request.user.army_scrap.all()
    scrapped_labor=request.user.labor_scrap.all()
    scrapped_financial=request.user.financial_scrap.all()
    scrapped_trade=request.user.trade_scrap.all()
    scrapped_leisure=request.user.leisure_scrap.all()
    scrapped_lawsuit=request.user.lawsuit_scrap.all()
    scrapped_welfare=request.user.welfare_scrap.all()
    scrapped_estate=request.user.estate_scrap.all()
    scrapped_business=request.user.business_scrap.all()
    scrapped_crime=request.user.crime_scrap.all()
    scrapped_client=request.user.client_scrap.all()
    scrapped_information=request.user.information_scrap.all()
    scrapped_startup=request.user.startup_scrap.all()
    scrapped_eco=request.user.eco_scrap.all()
    
    
 


    return render(request, 'mypage.html', {'mypage':mypage , 'scrapped_lawboard': scrapped_lawboard})



