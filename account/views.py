from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages

# Create your views here.
def login(request):
    return render(request, 'account/registration/login.html')