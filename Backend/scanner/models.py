from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Scan(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='scan')
    file_name = models.TextField()
    image = models.ImageField()
    date_created = models.DateField()


