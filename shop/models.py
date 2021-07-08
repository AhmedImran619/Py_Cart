from django.db import models


class Product(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    date_added = models.DateField()
