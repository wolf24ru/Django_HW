from .models import Phone
from django.contrib import admin

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')
