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
