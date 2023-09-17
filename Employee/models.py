from django.db import models

# Create your models here.
class Emp(models.Model):
    Employee_name = models.CharField(max_length=100)
    Employee_address=models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Start_Date = models.DateTimeField(auto_now=False,auto_now_add=False)
    End_Date = models.DateTimeField(auto_now=False,auto_now_add=False)
    Salary = models.DecimalField(max_digits=10, decimal_places=2)
    Login_time=models.TimeField(auto_now=False,auto_now_add=False)