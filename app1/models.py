from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import User
import sys
from PIL import Image
from io import BytesIO
from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
import PIL
import os
from django.conf import settings


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    image = models.ImageField(
        upload_to='images', default='image not available')

    thumbnails = models.ImageField(upload_to='thumbnail', blank=True)

    categ = models.ForeignKey(
        'category', on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
  
        
        
        

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    review_body = models.TextField()
    created = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, default=True)


class Cart(models.Model):

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    qty = models.IntegerField(default=1)
    total = models.IntegerField(blank=True, null=True)


choice = (
    ("WAITING FOR SHIPPING", "waiting for shipping"),
    ("PRODUCT ON THE WAY", "product on the way"),
    ("OUT OF DELIVERY", "out of delivery"),

    ("DELIVERED", "delivered"),
)


class Buyproduct(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, blank=True, null=True)
    qty = models.IntegerField(default=1)
    address = models.TextField(blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    purchased_time = models.DateTimeField(auto_now_add=True)
    totalprice = models.IntegerField(blank=True, null=True)
    order_updated = models.DateTimeField(auto_now=True)
    orderstatus = models.CharField(max_length=50,
                                   choices=choice,
                                   default="WAITING FOR SHIPPING")
    invoice_created = models.BooleanField(blank=True, null=True, default=False)
    file = models.FileField(upload_to='pdffile', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.totalprice = int(self.qty) * int(self.product.price)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product.name

class thumbnail(models.Model):
    image=models.ImageField(upload_to='images')
    thumnails=models.ImageField(upload_to='thumbnails',blank=True, null=True)
    
   
         
       
               



