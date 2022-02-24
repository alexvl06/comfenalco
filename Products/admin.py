from django.contrib import admin
from .models import *

#admin.site.register(products)
@admin.register(product)
class productAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'img', 'brand')
#admin.site.register(client)
admin.site.register(client)


@admin.register(Post)
class postAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'timestamp')

@admin.register(Solicitude)
class requestAdmin(admin.ModelAdmin):
    list_display = ('user', 'product','quantity','timestamp')
