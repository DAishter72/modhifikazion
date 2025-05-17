from django.urls import path
from home.views import HomeListView, MenuListView, PromocionListView

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('menu/', MenuListView.as_view(), name='menu'),
    path('promociones/', PromocionListView.as_view(), name='promociones'),
]
