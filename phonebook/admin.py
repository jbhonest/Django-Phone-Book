from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',
                    'phone_number', 'address', 'user')
    search_fields = ('first_name', 'last_name', 'phone_number', 'address')
    list_filter = ('user',)
