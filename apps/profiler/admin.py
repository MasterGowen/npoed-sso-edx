from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from social.apps.django_app.default.models import Code


@admin.register(get_user_model())
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        ('extra userinfo',
         {'fields': (
                    'second_name',
                    'date_of_birth',
                    'gender',
                    'icon_profile',
                    )
         }, ),
        ('location',
         {'fields': (
                    'time_zone',
                    'phone',
                    'country',
                    'city',
                    'post_address',
                    )
         }, ),
        ('education',
         {'fields': (
                    'university',
                    'university_group',
                    'education',
                    )
         }, ),
        ('permissions',
         {'fields': (
                    'role',
                    )
         }, ),
    )


@admin.register(Code)
class CodeAdmin(admin.ModelAdmin):
    list_display = ('email', 'code', 'verified', )
