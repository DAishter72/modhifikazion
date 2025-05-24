from django.urls import path
from django.urls import include
from auth.views import SignUpView, CustomLoginView, CustomLogoutView


urlpatterns = [
    path('auth/', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
