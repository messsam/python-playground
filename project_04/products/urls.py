from django.urls import path
from . import views # . == the current folder. We used it instead of a direct import to prevent conflicts with other imported libraries in the projct. (namespaces)

urlpatterns = [
    path('', views.index), # The empty string represents the root of this app. (127.0.0.1:8000/products/)
    # You're not actually calling the function, you're passing a reference to it and Django will handle the rest at runtime when the client sends an HTTP request to the server.
    path('new/', views.new)
]