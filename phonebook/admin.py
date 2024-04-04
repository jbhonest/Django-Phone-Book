from django.contrib import admin
from .models import Contact, MembershipPlan, UserProfile


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',
                    'phone_number', 'address', 'photo', 'user')
    search_fields = ('first_name', 'last_name', 'phone_number', 'address')
    list_filter = ('user',)


@admin.register(MembershipPlan)
class MembershipPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_limit')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'membership_plan', 'contacts_created')
