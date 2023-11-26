from django.db import models
# Create your models here.


class Contact(models.Model):
  username = models.CharField(max_length=122)
  email = models.EmailField(max_length=122,unique=True)
  password = models.CharField(max_length=122)
