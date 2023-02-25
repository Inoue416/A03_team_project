from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from app.models.user import User

# Register your models here.
class UserAdmin(UserAdmin):
    """AdminページのUserモデルの設定"""
    ordering = ['id']
    list_display = ['id', 'name', 'is_student', 'is_company', 'is_staff']
    fieldsets = (
        (_('Personal Info'), {'fields': ('name', 'email',)}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_superuser',
                )
            }
        ),
        (
            # HACK:命名
            _('dates Info'),
            {
                'fields' :(
                    'last_login',
                    'created_at',
                    'updated_at',
                )
            }
        )
    )
    readonly_fields = ['last_login', 'created_at', 'updated_at']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields' : (
                'name',
                'email',
                'password1',
                'password2',
                'is_student',
                'is_company',
                'is_active',
            )
        }),
    )
    
admin.site.register(User, UserAdmin)