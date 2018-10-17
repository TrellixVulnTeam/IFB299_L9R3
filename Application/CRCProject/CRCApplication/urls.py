from django.conf.urls import url, include
from CRCApplication import views
from CRCApplication.views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^home/$', views.home_page, name='home_page'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^customer_results/$', CustomerResults.as_view(), name='customer_results'),
    url(r'^employee_homescreen/$', views.employee_homescreen, name='employee_homescreen'),
    url(r'^FAQ/$', views.FAQ, name='FAQ'),
    url(r'^reports/$', views.reports, name='reports'),
    url(r'^stores/$', views.stores, name='stores'),
    url(r'^vehicles/$', views.vehicles, name='vehicles'),
    url(r'^sign_in/$', LoginView.as_view(template_name='CRCApplication/sign_in.html'), name='sign_in'),
    url(r'^logout/$', LogoutView.as_view(template_name='CRCApplication/logout.html'), name='logout'),
]