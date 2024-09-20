from django.db import models

# Create your models here.
class Register2(models.Model):
    name = models.CharField(max_length=300)
    password = models.IntegerField()
    address = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
class meta:
    db_table="Register2"