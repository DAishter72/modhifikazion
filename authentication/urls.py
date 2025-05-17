from django.urls import path
from .views import SignUpView, home, loginView
from django.urls import include

urlpatterns = [
    path('auth/', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', loginView.as_view(), name='login'),
]