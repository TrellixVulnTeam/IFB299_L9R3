from django import forms
from CRCApplication.models import *

class CustomerSearch(forms.Form):
    customerId = forms.CharField(required = False, label = 'ID')
    name = forms.CharField(required = False, label = 'Name')
    phone = forms.CharField(required = False, label = 'Phone Number')
    address = forms.CharField(required = False, label = 'Address')
    occupation = forms.ModelChoiceField(required = False, label = 'Occupation', queryset = Customers.objects.values_list('customer_occupation', flat = True).distinct(), to_field_name = 'customer_occupation')
    gender = forms.ModelChoiceField(required = False, label = 'Gender', queryset = Customers.objects.values_list('customer_gender', flat = True).distinct(), to_field_name = 'customer_gender')

class ECarSearch(forms.Form):
    carId = forms.CharField(required = False, label = 'Car ID')
    makename = forms.ModelChoiceField(required = False, label = 'Make', queryset = Cars.objects.values_list('car_makename', flat = True).distinct(), to_field_name = 'car_makename')
    model = forms.ModelChoiceField(required = False, label = 'Model', queryset = Cars.objects.values_list('car_model', flat = True).distinct(), to_field_name = 'car_model')
    series = forms.ModelChoiceField(required = False, label = 'Series', queryset = Cars.objects.values_list('car_series', flat = True).distinct(), to_field_name = 'car_series')
    seriesyear = forms.ModelChoiceField(required = False, label = 'Series Year', queryset = Cars.objects.values_list('car_seriesyear', flat = True).distinct(), to_field_name = 'car_seriesyear')
    pricenew = forms.ModelChoiceField(required = False, label = 'Price of Car New', queryset = Cars.objects.values_list('car_pricenew', flat = True).distinct(), to_field_name = 'car_pricenew')
    enginesize = forms.ModelChoiceField(required = False, label = 'Engine Size', queryset = Cars.objects.values_list('car_enginesize', flat = True).distinct(), to_field_name = 'car_enginesize')
    fuelsystem = forms.ModelChoiceField(required = False, label = 'Fuel System', queryset = Cars.objects.values_list('car_fuelsystem', flat = True).distinct(), to_field_name = 'car_fuelsystem')
    tankcapacity = forms.ModelChoiceField(required = False, label = 'Tank Capacity', queryset = Cars.objects.values_list('car_tankcapacity', flat = True).distinct(), to_field_name = 'car_tankcapacity')
    power = forms.ModelChoiceField(required = False, label = 'Power', queryset = Cars.objects.values_list('car_power', flat = True).distinct(), to_field_name = 'car_power')
    seatingcapacity = forms.ModelChoiceField(required = False, label = 'Seating Capacity', queryset = Cars.objects.values_list('car_seatingcapacity', flat = True).distinct(), to_field_name = 'car_seatingcapacity')
    standardtransmission = forms.ModelChoiceField(required = False, label = 'Transmission', queryset = Cars.objects.values_list('car_standardtransmission', flat = True).distinct(), to_field_name = 'car_standardtransmission')
    bodytype = forms.ModelChoiceField(required = False, label = 'Body Type', queryset = Cars.objects.values_list('car_bodytype', flat = True).distinct(), to_field_name = 'car_bodytype')
    drive = forms.ModelChoiceField(required = False, label = 'Drive', queryset = Cars.objects.values_list('car_drive', flat = True).distinct(), to_field_name = 'car_drive')
    wheelbase = forms.ModelChoiceField(required = False, label = 'Wheel Base', queryset = Cars.objects.values_list('car_wheelbase', flat = True).distinct(), to_field_name = 'car_wheelbase')


class CCarSearch(forms.Form):
    makename = forms.ModelChoiceField(required = False, label = 'Make', queryset = Cars.objects.values_list('car_makename', flat = True).distinct(), to_field_name = 'car_makename')
    model = forms.ModelChoiceField(required = False, label = 'Model', queryset = Cars.objects.values_list('car_model', flat = True).distinct(), to_field_name = 'car_model')
    seriesyear = forms.ModelChoiceField(required = False, label = 'Series Year', queryset = Cars.objects.values_list('car_seriesyear', flat = True).distinct(), to_field_name = 'car_seriesyear')
    enginesize = forms.ModelChoiceField(required = False, label = 'Engine Size', queryset = Cars.objects.values_list('car_enginesize', flat = True).distinct(), to_field_name = 'car_enginesize')
    fuelsystem = forms.ModelChoiceField(required = False, label = 'Fuel System', queryset = Cars.objects.values_list('car_fuelsystem', flat = True).distinct(), to_field_name = 'car_fuelsystem')
    seatingcapacity = forms.ModelChoiceField(required = False, label = 'Seating Capacity', queryset = Cars.objects.values_list('car_seatingcapacity', flat = True).distinct(), to_field_name = 'car_seatingcapacity')
    standardtransmission = forms.ModelChoiceField(required = False, label = 'Transmission', queryset = Cars.objects.values_list('car_standardtransmission', flat = True).distinct(), to_field_name = 'car_standardtransmission')
    bodytype = forms.ModelChoiceField(required = False, label = 'Body Type', queryset = Cars.objects.values_list('car_bodytype', flat = True).distinct(), to_field_name = 'car_bodytype')

class StoreSearch(forms.Form):
    storeId = forms.CharField(required = False, label = 'Store ID')
    storeName = forms.CharField(required = False, label = 'Store Name')
    storeAddress = forms.CharField(required = False, label = 'Address')
    storePhone = forms.CharField(required = False, label = 'Phone')
    storeCity = forms.ModelChoiceField(required = False, label = 'City', queryset = Stores.objects.values_list('store_city', flat = True).distinct(), to_field_name = 'store_city')
    storeStateName = forms.ModelChoiceField(required = False, label = 'State', queryset = Stores.objects.values_list('store_state_name', flat = True).distinct(), to_field_name = 'store_state_name')