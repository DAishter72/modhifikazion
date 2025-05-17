from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

def home (request):
    return render(request, 'home.html')

class loginView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')
