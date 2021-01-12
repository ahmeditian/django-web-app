from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username

class UserFeedbackInfo(models.Model):
    subject = models.CharField(blank=False, max_length=30, null=True)
    message = models.TextField(blank=False, null=True)
    attachment = models.ImageField(upload_to='feedback_attachments', blank=True)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE, related_name='feedback')

    def __str__(self):
        return self.user.username
