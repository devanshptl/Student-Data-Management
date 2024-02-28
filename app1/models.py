from django.db import models


# Create your models here.
class Home(models.Model):
    name = models.CharField(max_length=255)
    roll_no = models.IntegerField()
    department = models.CharField(
        max_length=50,
    )
    year = models.CharField(
        max_length=25,
    )
   