from django.contrib import admin
from .models import *


# Register your models here.
class AdminPortfolio(admin.ModelAdmin):
    list_display = ['name', 'title', 'description']


class AdminContact(admin.ModelAdmin):
    list_display = ['name', 'email', 'description']


class AdminImage(admin.ModelAdmin):
    list_display = ['name', 'image1', 'image2', 'image3']


class AdminPdf(admin.ModelAdmin):
    list_display = ['name', 'pdf']


class AdminSkill(admin.ModelAdmin):
    list_display = ['Skill1', 'Skill2', 'Skill3', 'Skill4', 'Skill5']


admin.site.register(Portfolio, AdminPortfolio)
admin.site.register(Contact, AdminContact)
admin.site.register(Image, AdminImage)
admin.site.register(Pdf, AdminPdf)
admin.site.register(Work)
admin.site.register(Skills,AdminSkill)
