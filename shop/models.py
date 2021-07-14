from django.db import models


class Product(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    date_added = models.DateField()
    category = models.CharField(max_length=50, default='')
    sub_category = models.CharField(max_length=50, default='')
    image = models.ImageField(upload_to='shop/images', default='')
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
