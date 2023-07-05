from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(home.urls)),
    path('products/', include(home.urls.products)),
    path('product_details/', include(home.urls.product_details)),
    path('cart/', include(home.urls.cart)),
    path('signup/', include(home.urls.signup)),
    path('login/', include(home.urls.login)),
]