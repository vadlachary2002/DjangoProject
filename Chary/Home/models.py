from django.db import models
# Create your models here.

# run these commans after creation of model
# python manage.py makemigrations
# python manage.py migrate

class Contact(models.Model):
  username = models.CharField(max_length=122)
  email = models.EmailField(max_length=122,unique=True)
  password = models.CharField(max_length=122)

  def __str__(self):
      return self.username
  