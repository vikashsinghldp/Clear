from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=200)
    email=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    message=models.CharField(max_length=50)
