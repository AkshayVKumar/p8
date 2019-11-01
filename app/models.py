from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Model_img(models.Model):
    img=models.ImageField(upload_to='images/')
    
class User_data(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    webpage=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='user')

    def __str__(self):
        return self.user.username
    