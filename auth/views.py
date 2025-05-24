from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

# Vista de registro


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

# Vista de inicio (protegida)


@login_required
def home(request):
    return render(request, 'home.html')

# Vista de login personalizada


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True  # Redirige a usuarios ya autenticados

# Vista de logout


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')
