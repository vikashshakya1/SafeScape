from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CivilianRegistrationForm, CivilianLoginForm

# Home and informational pages
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

# Civilian-specific views
def CivilianProfile(request):
    return render(request, 'civilian/CivilianProfile.html')

def CivilianDashboard(request):
    return render(request, 'civilian/CivilianDashboard.html')


def CivilianRegister(request):
    if request.method == 'POST':
        form = CivilianRegistrationForm(request,request.POST)
        if form.is_valid():
            form.save()  # Save the civilian user
            messages.success(request, 'Registration successful. Please log in with your credentials.')
            return redirect('CivilianLogin')  # Fixed redirect to correct name
        else:
            # Show error messages on the registration page
            messages.error(request, 'Please correct the errors below.')
            print(form.errors)  # Display errors for debugging
    else:
        form = CivilianRegistrationForm()

    return render(request, 'civilian/CivilianRegister.html', {'form': form})  # Fixed template name

# def CivilianLogin(request):
#     if request.method == 'POST':
#         form = CivilianLoginForm(request.POST)
#         if form.is_valid():
#             user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
#             if user is not None:
#                 login(request, user)  # Log in the user
#                 return redirect('CivilianDashboard')  # Redirect to dashboard after login
#             else:
#                 messages.error(request, 'Invalid username or password')  # Display login error
#     else:
#         form = CivilianLoginForm()

#     return render(request, 'civilian/CivilianLogin.html', {'form': form})  # Fixed template name

def CivilianLogin(request):
    if request.method == 'POST':
        print("POST request received")
        form = CivilianLoginForm(request,request.POST)
        if form.is_valid():
            print("Form is valid")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            print("User authentication:", user)
            if user is not None:
                login(request, user)
                return redirect('CivilianDashboard')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CivilianLoginForm()

    return render(request, 'civilian/CivilianLogin.html', {'form': form})





def civilian_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')  # Logout success message
    return redirect('CivilianLogin')  # Fixed redirect to correct name

# Law Enforcement-specific views
def LawEnforcementProfile(request):
    return render(request, 'LawEnforcement/LawEnforcementProfile.html')

def LawEnforcementDashboard(request):
    return render(request, 'LawEnforcement/LawEnforcementDashboard.html')

def LawEnforcementLogin(request):
    if request.method == 'POST':
        form = CivilianLoginForm(data=request.POST)  # You may want to replace this with a specific form for law enforcement
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('LawEnforcementDashboard')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = CivilianLoginForm()  # Replace with LawEnforcementLoginForm if needed
    
    return render(request, 'LawEnforcement/LawEnforcementLogin.html', {'form': form})

def LawEnforcementRegister(request):
    if request.method == 'POST':
        # Implement law enforcement registration form
        pass
    else:
        pass
    return render(request, 'LawEnforcement/LawEnforcementSignUp.html')

def LawEnforcementCrimeView(request):
    return render(request, 'LawEnforcement/LawEnforcementCrimeView.html')

# Crime Reporting views
def ReportCrime(request):
    return render(request, 'ReportCrime/ReportCrime.html')

def ReportCriminal(request):
    return render(request, 'ReportCrime/ReportCriminal.html')

def register(request):
    return render(request,'Authentication/register.html')