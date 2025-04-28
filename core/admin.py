from django.contrib import admin

# Register your models here.
from .models import  Contact, Blog, Furnitures, Subscribe
admin.site.register(Contact)
admin.site.register(Blog)
admin.site.register(Furnitures)
admin.site.register(Subscribe)