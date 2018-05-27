from django.contrib import admin

# Register your models here.
from .models import Guest


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'rsvp', 'additions', 'message')