from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name=models.CharField( max_length=50)
    desc=models.TextField()
    price=models.IntegerField()
    image=models.ImageField(upload_to='images',default='image not available')
    categ=models.ForeignKey('category',on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering=['-created']
    

class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Review(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    review_body=models.TextField()
    created=models.DateTimeField(auto_now=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,default=True)
    
class Cart(models.Model):
    
    product=models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    qty=models.IntegerField(default=1)

class Buyproduct(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    qty=models.IntegerField( default=1)
    address=models.TextField(blank=True,null=True)
    pincode=models.IntegerField(blank=True,null=True)
    