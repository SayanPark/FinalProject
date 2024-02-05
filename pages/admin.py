from django.contrib import admin
from . import models


# Register your models here.
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'date', 'seen']
    readonly_fields = ['name', 'email', 'date', 'message']


admin.site.register(models.ContactUs, ContactUsAdmin)
