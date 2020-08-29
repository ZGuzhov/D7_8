from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
  
  
class UserProfile(models.Model):  
  
    age = models.IntegerField(null=True, blank=True)  
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()


post_save.connect(create_profile, sender=User)


