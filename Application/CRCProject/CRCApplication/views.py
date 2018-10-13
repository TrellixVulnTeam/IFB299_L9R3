from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User

def home_page(request):
    return render(request, 'CRCApplication/home_page.html')

def about(request):
    return render(request, 'CRCApplication/about.html')

def contact(request):
    return render(request, 'CRCApplication/contact.html')

def customer_results(request):
    return render(request, 'CRCApplication/customer_results.html')

def employee_homescreen(request):
    args = {'user': request.user}
    print(args)
    return render(request, 'CRCApplication/employee_homescreen.html', args)

def FAQ(request):
    return render(request, 'CRCApplication/FAQ.html')

def reports(request):
    return render(request, 'CRCApplication/reports.html')

def sign_in(request):
    return render(request, 'CRCApplication/sign_in.html')

def stores(request):
    return render(request, 'CRCApplication/stores.html')

def vehicles(request):
    return render(request, 'CRCApplication/vehicles.html')