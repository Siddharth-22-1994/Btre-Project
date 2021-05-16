from django.contrib import admin

# Register your models here.
from realtors.models import Realtor
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email')
    list_per_page = 20
admin.site.register(Realtor, RealtorAdmin)