from django.contrib import admin
from .models import Contacts

class ContactAdmin(admin.ModelAdmin):
    list_display       = ('id', 'name', 'email','contact_date')
    list_display_links = ('id','name')
    list_editable      = ('email', )
    list_filter        = ('contact_date', )
    search_fields      = ('last_name','email')
    list_per_page      = 25

    def name (self,obj):
        return f"{obj.first_name} {obj.last_name}"

admin.site.register(Contacts,ContactAdmin)
# admin.site.site_header = "Wakali  Kwanza"   