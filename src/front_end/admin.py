from django.contrib import admin
from .models import Contacts

class ContactAdmin(admin.ModelAdmin):
    list_display       = ('id', 'first_name', 'last_name', 'email','contact_date')
    list_display_links = ('id','first_name')
    # search_fields      = ('name','email','listing')
    list_per_page      = 25



admin.site.register(Contacts,ContactAdmin)   