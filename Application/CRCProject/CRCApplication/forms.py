from django import forms
from CRCApplication.models import *

class CustomerSearch(forms.Form):
    customerId = forms.CharField(required = False, label = 'ID')
    name = forms.CharField(required = False, label = 'Name')
    phone = forms.CharField(required = False, label = 'Phone Number')
    address = forms.CharField(required = False, label = 'Address')
    occupation = forms.CharField(required = False, label = 'Occupation')
    gender = forms.ModelChoiceField(required = False, label = 'Gender', queryset = Customers.objects.values_list('customer_gender', flat = True).distinct(), to_field_name = 'customer_gender')

class ECarSearch(forms.Form):
    carId = forms.CharField(required = False, label = 'Car ID')
    makename = forms.CharField(required = False, label = 'Make')
    model = forms.CharField(required = False, label = 'Model')
    series = forms.CharField(required = False, label = 'Series')
    seriesyear = forms.CharField(required = False, label = 'Series Year')
    pricenew = forms.CharField(required = False, label = 'Price of Car New')
    enginesize = forms.CharField(required = False, label = 'Engine Size')
    fuelsystem = forms.CharField(required = False, label = 'Fuel System')
    tankcapacity = forms.CharField(required = False, label = 'Tank Capacity')
    power = forms.CharField(required = False, label = 'Power')
    seatingcapacity = forms.CharField(required = False, label = 'Seating Capacity')
    standardtransmission = forms.CharField(required = False, label = 'Transmission')
    bodytype = forms.CharField(required = False, label = 'Body Type')
    drive = forms.CharField(required = False, label = 'Drive')
    wheelbase = forms.CharField(required = False, label = 'Wheel Base')


class CCarSearch(forms.Form):
    makename = forms.CharField(required = False, label = 'Make')
    model = forms.CharField(required = False, label = 'Model')
    seriesyear = forms.CharField(required = False, label = 'Series Year')
    enginesize = forms.CharField(required = False, label = 'Engine Size')
    fuelsystem = forms.CharField(required = False, label = 'Fuel System')
    seatingcapacity = forms.CharField(required = False, label = 'Seating Capacity')
    standardtransmission = forms.CharField(required = False, label = 'Transmission')
    bodytype = forms.CharField(required = False, label = 'Body Type')
