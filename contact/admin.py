from django.contrib import admin
from contact import models
# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'email' , 'create_date', 'description'
    ordering = '-id',
    list_filter = 'create_date',
    search_fields = 'id', 'first_name', 'last_name', 'phone', 'email' , 'create_date', 'description',
    list_per_page = 10
    list_max_show_all = 200
    list_editable = 'first_name', 'last_name',
    list_display_links = 'id', 'phone',
