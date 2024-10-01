from django.db import models

# Create your models here.
class Category_db(models.Model):
    Category_Name = models.CharField(max_length=50,null=True,blank=True)
    Description = models.TextField(max_length=50, null=True, blank=True)
    Image = models.ImageField(upload_to="pictures",null=True,blank=True)
class Product_db(models.Model):
    Category_name = models.CharField(max_length=50,null=True,blank=True)
    Product_name = models.CharField(max_length=50,null=True,blank=True)
    Description = models.TextField(max_length=50,null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Brand = models.CharField(max_length=50, null=True, blank=True)
    Product_img1 = models.ImageField(upload_to="product image",null=True,blank=True)
    Product_img2 = models.ImageField(upload_to="product image", null=True, blank=True)
    Product_img3 = models.ImageField(upload_to="product image", null=True, blank=True)
