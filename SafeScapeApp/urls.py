from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('about/', views.about, name='About'),
    path('contact-us/', views.contact_us, name='Contact_Us'),
    path('crime-forecasting/', views.crime_forecasting, name='Crime_Forecasting'),
    path('services/', views.services, name='Services'),
]
