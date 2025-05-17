from django.urls import path
<<<<<<< HEAD
from .views import home

urlpatterns = [
    path('', home, name='home'),
]
=======
from home.views import HomeListView, MenuListView, PromocionListView

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('menu/', MenuListView.as_view(), name='menu'),
    path('promociones/', PromocionListView.as_view(), name='promociones'),
]
>>>>>>> 41abdc3a90d09158f03cc514a312f4e2a83f6864
