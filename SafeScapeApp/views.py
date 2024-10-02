from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CivilianRegistrationForm, CivilianLoginForm

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

# def CivilianRegister(request):
#     return render(request, 'civilian/CivilanRegistration.html')

# def Civilianlogin(request):
#     return render(request, 'civilian/CivilanLogin.html')

def CivilianProfile(request):
    return render(request, 'civilian\CivilianProfile.html')

def CivilianDashboard(request):
    return render(render,'civilian\CiviilanDashboard.html')

def LawEnforcementLogin(request):
    return render(request,'LawEnforcement/LawEnforcementLogin.html')

def LawEnforcementRegister(request):
    return render(request,'LawEnforcement/LawEnforcementSignUp.html')


def CivilianRegister(request):
    if request.method == 'POST':
        form = CivilianRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('CivilianLogin')
    else:
        form = CivilianRegistrationForm()
    return render(request, 'civilian\CivilanRegistration.html', {'form': form})

def Civilianlogin(request):
    if request.method == 'POST':
        form = CivilianLoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('CivilianProfile')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = CivilianLoginForm()
    return render(request, 'Authentication/civilian_login.html', {'form': form})

def civilian_logout(request):
    logout(request)
    return redirect('civilian\CivilanLogin.html')

