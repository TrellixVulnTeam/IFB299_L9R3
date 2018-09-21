from django.conf.urls import url
from CRCApplication import views 

urlpatterns = [
    url(r'^$', views.index),
]