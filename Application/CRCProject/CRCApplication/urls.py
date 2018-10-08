from django.conf.urls import url
from CRCApplication import views 

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^customer_results/$', views.customer_results, name='customer_results'),
    url(r'^employee_homescreen/$', views.employee_homescreen, name='employee_homescreen'),
    url(r'^FAQ/$', views.FAQ, name='FAQ'),
    url(r'^reports/$', views.reports, name='reports'),
    url(r'^sign_in/$', views.sign_in, name='sign_in'),
    url(r'^stores/$', views.stores, name='stores'),
    url(r'^vehicles/$', views.vehicles, name='vehicles'),
]