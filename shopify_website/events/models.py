from django.db import models

class customer(models.Model):
	Customer_Name = models.CharField(max_length=100)
	Customer_Address = models.CharField(max_length=200)
	Customer_Email = models.CharField(max_length=100)
	Customer_Phone_no = models.BigIntegerField()
	Date_of_Birth = models.DateField()
	Gender = models.CharField(max_length=10)