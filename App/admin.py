from django.contrib import admin
from .models import *


# Register your models here.
class AdminPortfolio(admin.ModelAdmin):
    list_display = ['name', 'title', 'description']

class AdminContact(admin.ModelAdmin):
    list_display = ['name', 'email', 'description']


admin.site.register(Portfolio, AdminPortfolio)
admin.site.register(Contact, AdminContact)
admin.site.register(Image)
