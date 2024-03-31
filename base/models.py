from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# to tell django that will be using this user model instead of the default one we to the setting.py and add AUTH_USER_MODEL='base.User'
class User(AbstractUser):
    name = models.CharField(max_length=200, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False, blank=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.username}"


class SensorData(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    temp = models.IntegerField(null=True)
    humid = models.IntegerField(null=True)
    moisture = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.host}"


class Message(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    body = models.TextField()

    class Meta:
        ordering = ["-created", "-updated"]

    def __str__(self):
        return f"{self.body}"


class PrivateMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE,related_name="messages_sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")
    group_id = models.IntegerField(null=True)
    body = models.TextField(null=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = [
            "-created",
            "-updated",
        ]

    def __str__(self):
        return f"{self.body}"
