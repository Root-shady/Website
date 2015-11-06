from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    FEMALE = 'F'
    MALE = 'M'
    SEX_CHOICE = ((FEMALE, 'female'),(MALE, 'male'))
    sex = models.CharField(max_length=1, choices=SEX_CHOICE,blank=True)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    last_login = models.DateTimeField(auto_now=True)
# An integer stands for the level of the user(potnetial buyer)
    user_level = models.PositiveIntegerField(default=0)
# Email validation (proved or not)
    status = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username

