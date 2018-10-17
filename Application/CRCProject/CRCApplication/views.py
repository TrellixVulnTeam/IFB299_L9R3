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
# def customer_search(request):        
#     if request.method == 'GET':      
#         output =  request.GET.get('customer_search')      
#         try:
#             status = Add_prod.objects.filter(customer_id__icontains = output1) 
#         return render(request,"employee_homescreen.html",{"search":status}) #OR IS IT MEANT TO BE CRCApplication/employee_homescreen.html
#     else:
#         return render(request,"employee_homescreen.html",{})

# def Vehicle_entered(request):        
#     if request.method == 'GET':       
#         output =  request.GET.get('Vehicle_entered')       
#         try:
#             status = Add_prod.objects.filter(customer_id__icontains=output2) 
#         return render(request,"employee_homescreen.html",{"search":status}) # this here could need to be the databse table name..??
#     else:
#         return render(request,"employee_homescreen.html",{})

#Attempt 1 came from https://stackoverflow.com/questions/38006125/how-to-implement-search-function-in-django



#ATTEMPT 2 came from https://www.youtube.com/watch?v=eyAIAZr5Q3w

#Vehicle query
# def Vehicle_Query(request):
#     V_query = request.GET.get ("Vehicle_entered")
#     queryset_list = ()
#     if V_query:
#         queryset_list = queryset_list.filter(
#             Q(customer_id__icontains=V_query) |
#             Q(customer_name__icontains=V_query) |
#             Q(customer_phone__icontains=V_query) |
#             Q(customer_address__icontains=V_query) |
#             Q(customer_birthday__icontains=V_query) |
#             Q(customer_occupation__icontains=V_query) |
#             Q(customer_gender__icontains=V_query)
#             ).distinct
#     return queryset_list
#         #test to make sure this works then the code to put it in a table should be below.

# #Customer Query
# C_query = request.GET.get ("customer_search")
# if C_query:
#     queryset_list = queryset_list.filter(
#         Q(car_id__icontains=C_query) |
#         Q(car_makename__icontains=C_query) |
#         Q(car_model__icontains=C_query) |
#         Q(car_series__icontains=C_query) |
#         Q(car_seriesyear__icontains=C_query) |
#         Q(car_pricenew__icontains=C_query) |
#         Q(car_enginesize__icontains=C_query) |
#         Q(car_fuelsystem__icontains=C_query) |
#         Q(car_tankcapacity__icontains=C_query) |
#         Q(car_power__icontains=C_query) |
#         Q(car_seatingcapacity__icontains=C_query) |
#         Q(car_standardtransmission__icontains=C_query) |
#         Q(car_bodytype__icontains =C_query) |
#         Q(car_drive__icontains=C_query) |
#         Q(car_wheelbase__icontains=C_query)
#         ).distinct
#     return queryset_list



# If everything works then implement the following code so that instead of the output being a list it will be a table.

# {% if queryset_list %}
# <tr>
#     <th> customer ID </th>
#     <th> Name </th>
#     <th> Phone </th>
#     <th> Address </th>
#     <th> D.O.B </th>
#     <th> Occupation </th>
#     <th> Gender </th>
# </tr>
# <tr>
#     <td> </td>
#     <td> </td>
#     <td> </td>
#     <td> </td>
#     <td> </td>
#     <td> </td>
#     <td> </td>
# </tr>

# {% endif %}

# {% if queryset_list %}
# <tr>
#     <th> Car ID </th>
#     <th> Make </th>
#     <th> Model </th>
#     <th> Series </th>
#     <th> Series Year </th>
#     <th> Price </th>
#     <th> Engine Size </th>
#     <th> Fuel System </th>
#     <th> Tank Capacity </th>
#     <th> Power </th>
#     <th> Seating Capacity </th>
#     <th> Transmission Type </th>
#     <th> Body Type </th>
#     <th> Drive </th>
#     <th> Wheel Base </th>
# </tr>
# <tr>
#     <td> </td>
#     <td> </td>
#     <td> </td>
#     <td> </td>
#     <td> </td>
#     <td> </td>
#     <td> </td>
#     <td> </td>
#     <td> </td>
#     <td> </td>
#     <td> </td>
#     <td> </td>
#     <td> </td>
#     <td> </td>
#     <td> </td>
# </tr>
# {% endif %}