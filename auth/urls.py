from django.urls import path
from django.urls import include
from auth.views import SignUpView, loginView


urlpatterns = [
    path('auth/', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', loginView.as_view(), name='login'),
]
