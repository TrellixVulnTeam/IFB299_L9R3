from django import forms
from CRCApplication.models import *

class CustomerSearch(forms.Form):
    customerId = forms.CharField(required = False, label = 'ID')
    name = forms.CharField(required = False, label = 'Name')
    phone = forms.CharField(required = False, label = 'Phone Number')
    address = forms.CharField(required = False, label = 'Address')
    occupation = forms.CharField(required = False, label = 'Occupation')
    gender = forms.ModelChoiceField(required = False, label = 'Gender', queryset = Customers.objects.values_list('customer_gender', flat = True).distinct(), to_field_name = 'customer_gender')