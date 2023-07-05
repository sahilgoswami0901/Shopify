from django.contrib import admin
from django.urls import path, include
from signup.views import signupconn
from login.views import loginconn
from home import views
from products.views import productsconn

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('events.urls')),
    path('', views.homeconn, name="home"),
    path('products/', productsconn, name="products"),
    # path('products/', views.productsconn, name="products"),
    path('product_details/', views.product_detailsconn, name="product_details"),
    path('cart/', views.cartconn, name="cart"),
    path('signup/', signupconn, name="signup"),
    path('login/', loginconn, name="login"),
    # path('signup/', views.signupconn, name="signup"),
    # path('login/', performLogin),
]