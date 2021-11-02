from django.contrib import admin

class PhoneAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
# Register your models here.
