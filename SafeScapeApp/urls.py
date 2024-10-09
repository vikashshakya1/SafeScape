from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    
     path('admin/', admin.site.urls),
    

    # Home and informational pages
    path('', views.index, name='Home'),
    path('about/', views.about, name='About'),
    path('contact-us/', views.contact_us, name='Contact_Us'),
    path('crime-forecasting/', views.crime_forecasting, name='Crime_Forecasting'),
    path('services/', views.services, name='Services'),

    # Civilian login and registration paths
    path('civilian/login/', views.CivilianLogin, name='CivilianLogin'),
    path('civilian/register/', views.CivilianRegister, name='CivilianRegister'),

    # Civilian-specific paths
    path('civilian/profile/', views.CivilianProfile, name='CivilianProfile'),
    path('civilian/dashboard/', views.CivilianDashboard, name='CivilianDashboard'),
    path('civilian/logout/', views.civilian_logout, name='CivilianLogout'),

    # Law Enforcement paths
    path('law-enforcement/login/', views.LawEnforcementLogin, name='LawEnforcementLogin'),
    path('law-enforcement/register/', views.LawEnforcementRegister, name='LawEnforcementRegister'),
    path('law-enforcement/profile/', views.LawEnforcementProfile, name='LawEnforcementProfile'),
    path('law-enforcement/dashboard/', views.LawEnforcementDashboard, name='LawEnforcementDashboard'),
    path('law-enforcement/crime-view/', views.LawEnforcementCrimeView, name='LawEnforcementCrimeView'),

    # Crime Reporting paths
    path('report-crime/', views.ReportCrime, name='ReportCrime'),
    path('report-criminal/', views.ReportCriminal, name='ReportCriminal'),
    
    
    #register option page 
    path('register',views.register,name="register")
]
