from django.db import models

# Create your models here.

class Employee(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100,null=False)
    company=models.CharField(max_length=50,null=False)
    email_id=models.EmailField(unique=True)
    department=models.CharField(max_length=50,null=False)
    dateOfJoining=models.DateTimeField()
    status=models.CharField(max_length=50)
    projectDomain=models.CharField(max_length=60,null=False)
