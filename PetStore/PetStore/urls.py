"""PetStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from Products.views import CreateProduct, UpdateProduct, DeleteProduct, ListProduct, about, buying

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about', about),
    path('', ListProduct.as_view(), name= 'home'),
    path('buying', buying.as_view(), name='confirmar_compra'),
    path('master', CreateProduct.as_view(), name = 'add_product'),
    path('master/<int:pk>', UpdateProduct.as_view(), name = 'edit_product'),
    path('delete_product/<int:pk>', DeleteProduct.as_view(), name = 'delete_product')
    ]
