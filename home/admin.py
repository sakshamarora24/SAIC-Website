from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactModel(admin.ModelAdmin):
    list_filter = ('name', 'email', )
    list_display = ('name', 'email', 'message')
