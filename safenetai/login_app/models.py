from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

# Create your models here.

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


#     facebook_id=models.URLField(blank=True)
    phone_number = models.CharField(
        max_length=20, 
        blank=True,
        validators=[RegexValidator(regex=r'^\d+$', message='Entered in digits only.')]
    )
    institution = models.CharField(max_length=100, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username