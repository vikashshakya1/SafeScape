from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('about/', views.about, name='About'),
    path('contact-us/', views.contact_us, name='Contact_Us'),
    path('crime-forecasting/', views.crime_forecasting, name='Crime_Forecasting'),
    path('services/', views.services, name='Services'),
    path('Login/',views.Login,name='Login'),
    path('Register/',views.Register, name ="Register"),
    path('CivilianRegistration/',views.CivilianRegister, name = 'CivilianRegister'),
    path('CivilianLogin/',views.Civilianlogin, name = 'CivilianLogin'),
    path('CivilianLogOut/',views.civilian_logout, name = 'CivilianLogOut'),
    path('CivilianProfile/',views.CivilianProfile,name = 'CivilianProfile'),
    path('CivilianDashboard/',views.CivilianDashboard,name = 'CivilianDashboard'),
    path('LawEnforcementLogin/',views.LawEnforcementLogin, name = 'LawEnforcementLogin'),
    path('LawEnforcementRegister/', views.LawEnforcementRegister, name = 'LawEnforcementRegister'),
]
