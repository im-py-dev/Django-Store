from django.urls import path
from . import views


# URLConf
urlpatterns = [
    path('', views.home),
    path('shop/', views.shop),
    path('customers/', views.customers),
]
