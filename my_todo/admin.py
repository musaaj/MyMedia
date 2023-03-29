from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    fieldsets=(
            (None, {'fields': ('phone_number', 'first_name', 'last_name')}),
            ('Permissions', {'fields': (
                        'is_staff',
                        'is_active',
                        'is_superuser',
                        'groups',
                        'user_permissions'
                    )
                }
            ),
        )
    add_fieldsets=(
            (
                None,
                {
                    'class': ('wide',),
                    'fields': ('phone_number', 'password1', 'password2')
                }
            ),
        )
    list_display=('phone_number', 'first_name', 'last_name')
    list_filter=('is_staff', 'is_superuser')
    search_fields = ('first_name', 'last_name',)
    ordering=('first_name',)
    filter_horizontal=('groups','user_permissions')

admin.site.register(User, UserAdmin)
