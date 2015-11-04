from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=128)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    FEMALE = 'F'
    MALE = 'M'
    SEX_CHOICE = ((FEMALE, 'female'),(MALE, 'male'))
    sex = models.CharField(max_length=1, choices=SEX_CHOICE,blank=True)

    joined_date = models.DateTimeField(editable=False)
    last_login = models.DateTimeField()
# An integer stands for the level of the user(potnetial buyer)
    user_level = models.PositiveIntegerField(default=0)
# Email validation (proved or not)
    status = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
# On save, update timestamps 
        if not self.user_id:
            self.joined_date = timezone.now()
        self.last_login = timezone.now()
        super(User, self).save(*args, **kwargs)
