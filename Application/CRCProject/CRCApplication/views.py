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



#Attempt 1....
def customer_search(request):        
    if request.method == 'GET':      
        output =  request.GET.get('customer_search')      
        try:
            status = Add_prod.objects.filter(output__icontains = output1) 
        return render(request,"employee_homescreen.html",{"search":status}) #OR IS IT MEANT TO BE CRCApplication/employee_homescreen.html
    else:
        return render(request,"employee_homescreen.html",{})

def Vehicle_entered(request):        
    if request.method == 'GET':       
        output =  request.GET.get('Vehicle_entered')       
        try:
            status = Add_prod.objects.filter(output__icontains=output2) 
        return render(request,"employee_homescreen.html",{"search":status}) # this here could need to be the databse table name..??
    else:
        return render(request,"employee_homescreen.html",{})



#ATTEMPT 2
