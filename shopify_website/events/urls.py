from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name="home"),
    path('', views.customerconn, name="customerconn"),
    path('placedCustomers/', views.wholesalersconn, name="wholesalersconn")
]