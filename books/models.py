from django.db import models

# Create your models here.

#---books model-----#

class Books(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    categories = (
        ('M', 'Maths'),
        ('C', 'Chemistry'),
        ('P', 'Pysics'),
    ) 
    category = models.CharField(max_length=10, choices=categories)
    reference_no = models.BigIntegerField()
    CREATED_ON      =models.DateTimeField(auto_now_add=True,null=True)
    UPDATED_ON      =models.DateTimeField(auto_now_add=True,null=True)