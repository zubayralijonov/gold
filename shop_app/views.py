from django.shortcuts import render, redirect

from . models import User, UserAccount

from . forms import UserAccountForm

from django.contrib.auth import authenticate

# Create your views here.

def index_page(request):
    news = UserAccount.objects.all()
    return render(request, 'index.html', context={'news': news})

def gold_main_page(request):
    news2 = UserAccount.objects.all()
    return render(request, 'gold_main_page.html', context={'news2':news2})

def gold_ring_page(request):
    news2 = UserAccount.objects.all()
    return render(request, 'gold_ring_page.html', context={'news2':news2})

def gold_set_page(request):
    news2 = UserAccount.objects.all()
    return render(request, 'gold_set_page.html', context={'news2':news2})

def gold_braslet_page(request):
    news2 = UserAccount.objects.all()
    return render(request, 'gold_braslet_page.html', context={'news2':news2})
