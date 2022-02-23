from django.contrib import admin
from .models import products, client

#admin.site.register(products)
@admin.register(products)
class productAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'img', 'brand')
#admin.site.register(client)
@admin.register(client)
class clientAdmin(admin.ModelAdmin):
    pass