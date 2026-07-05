from django.contrib import admin
from .models import Product, Offer # i.e. from the models.py file in this folder.

# Register the models you need to manage in the admin app/section here.

class ProductAdmin(admin.ModelAdmin): # Inheriting a class with all common functionality for managing models in the admin area.
    list_display = ('name', 'price', 'stock')

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')

admin.site.register(Product, ProductAdmin) # Pass both to the admin app.
admin.site.register(Offer, OfferAdmin)