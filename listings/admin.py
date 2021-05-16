from django.contrib import admin

# Register your models here.
from listings.models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor', 'price', 'city')
    list_editable = ('is_published', )
    search_fields = ('id', 'title', 'zipcode', 'price', 'list_date', 'realtor', 'city', 'state')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)