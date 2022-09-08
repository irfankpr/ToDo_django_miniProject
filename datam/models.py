from django.db import models


# Create your models here.

class todo(models.Model):
    username = models.CharField(max_length=50,blank=False)
    task = models.CharField(max_length=300,blank=False,null=False)
    task_status = models.BooleanField(default=False)



