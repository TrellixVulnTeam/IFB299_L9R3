from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpRequest

def index(request):
    return render(request, 'CRCApplication/signin.html')