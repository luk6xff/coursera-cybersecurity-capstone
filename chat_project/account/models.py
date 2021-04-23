from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'


class Message(models.Model):
    #  sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="sender", null=True)
    #  receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="receiver", null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender", null=True)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver", null=True)
    message = models.CharField(max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return self.message