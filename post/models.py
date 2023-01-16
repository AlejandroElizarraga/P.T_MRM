from django.db import models

# Create your models here.
class Post(models.Model):
    ip = models.CharField(max_length=12)

    def __str__(self):
        return self.ip
    
class ipPost(models.Model):
    direccion = models.CharField(max_length=12)