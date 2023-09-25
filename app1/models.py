from django.db import models

# Create your models here.
class product(models.Model):
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
    

class category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name