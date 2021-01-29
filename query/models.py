from django.db import models

# Create your models here.
class querydata(models.Model):
    querydata_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email_id=models.EmailField()
    mobile_number=models.IntegerField()
    query=models.CharField(max_length=300)
    contacted_via=models.CharField(max_length=50,blank=True)
    follow_up=models.CharField(max_length=100,blank=True)

class customerdata(models.Model):
    customer=models.CharField(max_length=100)




