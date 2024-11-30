from django.contrib import admin
from .models import User, UserActionLog

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "phone_number", "telegram_id", "username", "created_at")

@admin.register(UserActionLog)
class UserActionLogAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "action_type", "created_at")
