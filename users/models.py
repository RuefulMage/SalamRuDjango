from django.db import models
from django.utils.timezone import now

class User(models.Model):
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=10, default="en")
    telegram_id = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(default=now)

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.username or f"User {self.telegram_id}"


class UserActionLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_action_logs")
    message = models.TextField(blank=True, null=True)
    action_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=now)

    class Meta:
        db_table = "user_action_logs"

    def __str__(self):
        return f"{self.action_type} by {self.user}"
