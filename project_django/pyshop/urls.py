"""
URL configuration for pyshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include
import products.urls

urlpatterns = [
    path('admin/', admin.site.urls), # The default administrative graphical app that comes with django applications.
    path('products/', include('products.urls')) # Any HTTP requests with URLS starting with 'products/...', send them to 'urls' module in the 'products' app/package.
]

# Whenever you create an app the beautiful Django page starts appearing, and it's only your defined apps and paths.
# It is like the default constructor in Java. Either do not define any, or explicitly define it.