from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from app.models.user import User
from app.models.student_profile import StudentProfile
from app.models.company_profile import CompanyProfile
from app.models.skills import Skills
from app.models.skill_middle import SkillMiddle
from app.models.universities import Universities
from app.models.grade import Grade
from app.models.department import Department
from app.models.department_middle import DepartmentMiddle
from app.models.follow import Follow
from app.models.markdown_post import MarkdownPost
from app.models.nice import Nice

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

class UniversitiesAdmin(admin.ModelAdmin):
    pass

class NiceAdmin(admin.ModelAdmin):
    pass

class SkillsAdmin(admin.ModelAdmin):
    pass

class SkillMiddleAdmin(admin.ModelAdmin):
    pass

class StudentProfileAdmin(admin.ModelAdmin):
    pass

class CompanyProfileAdmin(admin.ModelAdmin):
    pass

class GradeAdmin(admin.ModelAdmin):
    pass

class DepartmentAdmin(admin.ModelAdmin):
    pass

class DepartmentMiddleAdmin(admin.ModelAdmin):
    pass

class FollowAdmin(admin.ModelAdmin):
    pass

class MarkdownPostAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
admin.site.register(Universities, UniversitiesAdmin)
admin.site.register(Nice, NiceAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(SkillMiddle, SkillMiddleAdmin)
admin.site.register(StudentProfile, StudentProfileAdmin)
admin.site.register(CompanyProfile, CompanyProfileAdmin)
admin.site.register(Grade, GradeAdmin) 
admin.site.register(Department, DepartmentAdmin)
admin.site.register(DepartmentMiddle, DepartmentMiddleAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.register(MarkdownPost, )
