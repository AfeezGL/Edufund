from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class AccountAdmin(UserAdmin):
    list_display = ('email', 'date_joined', 'last_login', 'is_admin', 'is_staff', 'is_student', 'is_sponsor',)
    search_fields = ('email',)
    readonly_fields = ('date_joined', 'last_login',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User, AccountAdmin)