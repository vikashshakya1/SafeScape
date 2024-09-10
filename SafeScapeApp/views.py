from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def crime_forecasting(request):
    return render(request, 'crime-forecasting.html')
    

def services(request):
    return render(request, 'services.html')

def Login(request):
    return render(request, 'Authentication/Login.html')

def Register(request):
    return render(request, 'Authentication/Register.html')

def CivilianRegister(request):
    return render(request, 'civilian/CivilanRegistration.html')

def Civilianlogin(request):
    return render(request, 'civilian/CivilanLogin.html')

def LawEnforcementLogin(request):
    return render(request,'LawEnforcement/LawEnforcementLogin.html')

def LawEnforcementRegister(request):
    return render(request,'LawEnforcement/LawEnforcementSignUp.html')
