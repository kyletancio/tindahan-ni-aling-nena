from django.db import models

# Create your models here. 

class Products(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=1000)
    qty = models.IntegerField()
    price = models.DecimalField( max_digits = 10, decimal_places = 2)
    add_date = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


