from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    mob_no = models.CharField(max_length=12, null=True, blank=True, unique=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('o', 'Others'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    image = models.ImageField(default='profiles/default.jpg', upload_to="profiles/", null=True, blank=True)
    joined_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} Profile'

class Address(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    isprimary = models.BooleanField(default=False)
    addline = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    pincode = models.PositiveIntegerField()
    def __str__(self):
        return self.city
    
# Create your models here.
