from codecs import getencoder
from distutils.command.upload import upload
from time import timezone
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
import datetime
import os

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/categor/',default='')
    description=models.TextField(max_length=500,default='')
    status=models.BooleanField(default=1)   
    

    def __str__(self):                     #object creation
        return self.name

class SubCategory(models.Model):
    sname = models.CharField(max_length=50)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def __str__(self):                     #object creation
        return self.sname

#featured brands
class Brands(models.Model):
    bname=models.CharField(max_length=50)
    bimage=models.ImageField(upload_to='uploads/brands/')

    def __str__(self):                     #object creation
        return self.bname    

class Product(models.Model): 
    pname = models.CharField(max_length=50,unique=True)
    price = models.IntegerField(default=0)
    offer = models.IntegerField(default='')
    # related_name for multiple foriegn keys
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, related_name='category')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, default=1, related_name='subcategory')
    description = models.CharField(max_length=500, default='')
    image = models.ImageField(upload_to='uploads/products/')
    brand=models.ForeignKey(Brands, on_delete=models.CASCADE, default=1)
    status=models.BooleanField(default=1)
    quantity=models.IntegerField(default=1)

    


#Customer
class Customer(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=12)
    email=models.EmailField()
    password=models.CharField(max_length=16)
    gender=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    zipcode=models.IntegerField()

    def __str__(self):
        return self.name



class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE,related_name='product')
    product_qty=models.IntegerField(null=False,blank=False)
    
    @property
    def total_cost(self):
        sum = self.product_qty*self.product.price
        return sum
   
           
        