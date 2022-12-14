from .models import Newsletter, Unregistered_subscriber
from django.contrib import admin


@admin.register(Unregistered_subscriber)
class Unregistered_subscriberModel(admin.ModelAdmin):
    list_display = ('email',)


@admin.register(Newsletter)
class NewsletterModel(admin.ModelAdmin):
    list_filter = ('user', 'isSubscribed')
    list_display = ('user', 'mobile', 'roll_number', 'isSubscribed',)
