from django.db import models
from myapp.models import Myusers
# Create your models here.

class Hometown(models.Model):
    name = models.ForeignKey(Myusers, on_delete=models.CASCADE, related_name='hometown_fname')
    townname = models.CharField(max_length=50)
        
    def __str__(self):
        return f'{self.name} {self.townname}' 