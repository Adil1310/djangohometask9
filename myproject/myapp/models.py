from django.db import models

# Create your models here.

class Myusers(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    birthyear = models.IntegerField()
    state = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.fname} {self.lname}'