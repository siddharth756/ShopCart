from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
    page_url = models.CharField(max_length=255,default="{% url 'mobiles' %}")

    def __str__(self):
        return self.name

class TopProduct(models.Model):
    pid = models.IntegerField(default=1)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='product/',null=True,blank=True)
    image_url = models.CharField(max_length=255,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='product/',null=True,blank=True)
    image_url = models.CharField(max_length=255,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    items = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=1000)
    address2 = models.CharField(max_length=1000,null=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    total = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    