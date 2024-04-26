from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name 


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    descripiton = models.TextField()
    image = models.FileField(upload_to="Product") 


    def __str__(self) -> str:
        return self.product_name 
    
