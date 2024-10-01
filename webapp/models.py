from django.db import models

# Create your models here.
class contact_db(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Message = models.TextField(max_length=500,null=True,blank=True)
class Register_db(models.Model):
    Username = models.CharField(max_length=50,null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Password = models.CharField(max_length=50,null=True,blank=True)

class cart_db(models.Model):
    User_Name = models.CharField(max_length=100,null=True,blank=True)
    Product_Name = models.CharField(max_length=100,null=True,blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Total_Price = models.IntegerField(null=True, blank=True)

class proceed_db(models.Model):
    First_Name = models.CharField(max_length=100,null=True,blank=True)
    Last_Name = models.CharField(max_length=100,null=True,blank=True)
    Country = models.CharField(max_length=100,null=True,blank=True)
    Address = models.CharField(max_length=100,null=True,blank=True)
    Town = models.CharField(max_length=100,null=True,blank=True)
    State = models.CharField(max_length=100,null=True,blank=True)
    Pincode = models.IntegerField(null=True,blank=True)
    Phone = models.IntegerField(null=True,blank=True)
    Email = models.EmailField(null=True,blank=True)
    total_price = models.IntegerField(null=True,blank=True)
