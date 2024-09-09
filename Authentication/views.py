from django.views import View
from django.shortcuts import render, redirect

# Create your views here.

class RegistrationView(View):
    def get(self, request):
        return render(request, 'Authenticatio/register.html')