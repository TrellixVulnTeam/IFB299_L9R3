from django.shortcuts import render#, get_object_or_404, redirect
from django.views import View
from django.http import HttpResponse, HttpRequest#, Http404
from django.contrib.auth.models import User
from CRCApplication.forms import *
from CRCApplication.models import *
from django.views.generic import TemplateView, FormView

#from urllib import quote_plus

from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.db.models import Q
from django.views.generic.detail import DetailView

def home_page(request):
    return render(request, 'CRCApplication/home_page.html')



class CustomerCar(FormView):
    def get(self, request):
        form = CCarSearch(self.request.GET or None)
        context = {'form':form}

        if form.is_valid():
            makename = self.request.GET.get('makename')
            model = self.request.GET.get('model')
            seriesyear = self.request.GET.get('seriesyear')
            enginesize = self.request.GET.get('enginesize')
            fuelsystem = self.request.GET.get('fuelsystem')
            seatingcapacity = self.request.GET.get('seatingcapacity')
            standardtransmission = self.request.GET.get('standardtransmission')
            bodytype = self.request.GET.get('bodytype')

            results = Cars.objects.filter(Q(car_makename__icontains = makename) & Q(car_model__icontains = model) & Q(car_seriesyear__icontains = seriesyear) & Q(car_enginesize__icontains = enginesize) & Q(car_fuelsystem__icontains = fuelsystem) & Q(car_seatingcapacity__icontains = seatingcapacity) & Q(car_standardtransmission__icontains = standardtransmission) & Q(car_bodytype__icontains = bodytype))
            carMake = Cars.objects.filter(Q(car_makename__icontains = makename) & Q(car_model__icontains = model) & Q(car_seriesyear__icontains = seriesyear) & Q(car_enginesize__icontains = enginesize) & Q(car_fuelsystem__icontains = fuelsystem) & Q(car_seatingcapacity__icontains = seatingcapacity) & Q(car_standardtransmission__icontains = standardtransmission) & Q(car_bodytype__icontains = bodytype)).values_list('car_makename')
            context = {'form':form, 'results': results} 
            return render (request, 'CRCApplication/CCAR_results.html', context)
        else:
            return render(request, 'CRCApplication/CCAR_results.html', context)


def about(request):
    return render(request, 'CRCApplication/about.html')

def contact(request):
    return render(request, 'CRCApplication/contact.html')


class CustomerResults(FormView):
    def get(self, request):
        form = CustomerSearch(self.request.GET or None)
        context = {'form': form}

        if form.is_valid():
            customerId = self.request.GET.get('customerId')
            name = self.request.GET.get('name')
            phone = self.request.GET.get('phone')
            address = self.request.GET.get('address')
            occupation = self.request.GET.get('occupation')
            gender = self.request.GET.get('gender')

            results = Customers.objects.filter(Q(customer_id__icontains = customerId) & Q(customer_name__icontains = name) & Q(customer_phone__icontains = phone) & Q(customer_address__icontains = address) & Q(customer_occupation__icontains = occupation) & Q(customer_gender__icontains = gender))
            customerIds = Customers.objects.filter(Q(customer_id__icontains = customerId) & Q(customer_name__icontains = name) & Q(customer_phone__icontains = phone) & Q(customer_address__icontains = address) & Q(customer_occupation__icontains = occupation) & Q(customer_gender__icontains = gender)).values_list('customer_id')
            
            context = {'form': form, 'results': results}
            return render(request, 'CRCApplication/customer_results.html', context)
        else:
            return render(request, 'CRCApplication/customer_results.html', context)

def employee_homescreen(request):
    args = {'user': request.user}
    return render(request, 'CRCApplication/employee_homescreen.html', args)


class EmployeeCar(FormView):
    def get(self, request):
        form = ECarSearch(self.request.GET or None)
        context = {'form': form}

        if form.is_valid():
            carId = self.request.GET.get('carId')
            makename = self.request.GET.get('makename')
            model = self.request.GET.get('model')
            series = self.request.GET.get('series')
            seriesyear = self.request.GET.get('seriesyear')
            pricenew = self.request.GET.get('pricenew')
            enginesize = self.request.GET.get('enginesize')
            fuelsystem = self.request.GET.get('fuelsystem')
            tankcapacity = self.request.GET.get('tankcapacity')
            power = self.request.GET.get('power')
            seatingcapacity = self.request.GET.get('seatingcapacity')
            standardtransmission = self.request.GET.get('standardtransmission')
            bodytype = self.request.GET.get('bodytype')
            drive = self.request.GET.get('drive')
            wheelbase = self.request.GET.get('wheelbase')


            results = Cars.objects.filter(Q(car_id__icontains = carId) & Q(car_makename__icontains = makename) & Q(car_model__icontains = model) & Q(car_series__icontains = series) & Q(car_seriesyear__icontains = seriesyear) & Q(car_pricenew__icontains = pricenew) & Q(car_enginesize__icontains = enginesize) & Q(car_fuelsystem__icontains = fuelsystem) & Q(car_tankcapacity__icontains = tankcapacity) & Q(car_power__icontains = power) & Q(car_seatingcapacity__icontains = seatingcapacity) & Q(car_standardtransmission__icontains = standardtransmission) & Q(car_bodytype__icontains = bodytype) & Q(car_drive__icontains = drive) & Q(car_wheelbase__icontains = wheelbase))
            carMake = Cars.objects.filter(Q(car_id__icontains = carId) & Q(car_makename__icontains = makename) & Q(car_model__icontains = model) & Q(car_series__icontains = series) & Q(car_seriesyear__icontains = seriesyear) & Q(car_pricenew__icontains = pricenew) & Q(car_enginesize__icontains = enginesize) & Q(car_fuelsystem__icontains = fuelsystem) & Q(car_tankcapacity__icontains = tankcapacity) & Q(car_power__icontains = power) & Q(car_seatingcapacity__icontains = seatingcapacity) & Q(car_standardtransmission__icontains = standardtransmission) & Q(car_bodytype__icontains = bodytype) & Q(car_drive__icontains = drive) & Q(car_wheelbase__icontains = wheelbase)).values_list('car_id')
            
            context = {'form': form, 'results': results} 
            return render (request, 'CRCApplication/ECAR_results.html', context)
        else:
            return render(request, 'CRCApplication/ECAR_results.html', context)

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
