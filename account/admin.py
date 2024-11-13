from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Define the fields to be displayed in the list view
    list_display = ('email', 'firstname', 'lastname', 'password_changed' , 'is_active', 'is_staff', 'date_joined')
    list_filter = ('is_active', 'is_staff')
    
    # Add the fields to be displayed in the form view
    fieldsets = (
        (None, {'fields': ('email', 'firstname', 'lastname', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
        ('Additional Information', {'fields': ('address', 'birth', 'phone', 'password_changed')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'firstname', 'lastname', 'password', 'is_active', 'is_staff', 'password_changed')}
        ),
    )
    
    # Customizing the ordering
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions')

    readonly_fields=('password_changed',)

# Register the custom user model with the admin site
admin.site.register(CustomUser, CustomUserAdmin)
