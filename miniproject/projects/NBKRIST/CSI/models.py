from django.db import models
from PIL import Image
from datetime import datetime
from django import forms

# Create your models here.
class Photo(models.Model):
    Image=models.ImageField(upload_to="static/images/")
    description=models.CharField(max_length=100)
    def __str__(self):
        return self.description
class Year(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    def __str__(self):
        return self.name
class individualeventspics(models.Model):
    year=models.ForeignKey(Year, on_delete=models.SET_NULL,null=True)
    image=models.ImageField(upload_to="static/images/")
    description=models.TextField()
    def __str__(self):
        return self.description
class academicyear20_21(models.Model):
    year=models.ForeignKey(Year, on_delete=models.SET_NULL,null=True)
    image=models.ImageField(upload_to="static/images/")
    eventnumber=models.CharField(max_length=10)
    eventdescription=models.CharField(max_length=1000,default="events")
    name=models.CharField(max_length=30)
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.eventnumber
class winners(models.Model):
    eventno=models.ForeignKey(academicyear20_21,on_delete=models.SET_NULL,null=True)
    winnername1=models.CharField(max_length=30,default="name")
    winnername2=models.CharField(max_length=30,default="name")
    winnername3=models.CharField(max_length=30,default="name")
    yearofstudy1=models.CharField(max_length=20,default="YEAR")
    yearofstudy2=models.CharField(max_length=20,default="YEAR")
    yearofstudy3=models.CharField(max_length=20,default="YEAR")
    section1=models.CharField(max_length=10,default="Section")
    section2=models.CharField(max_length=10,default="Section")
    section3=models.CharField(max_length=10,default="Section")
class Contact(models.Model):
    name=models.CharField(max_length=30,blank=False)
    content=models.TextField(blank=False)
    email=models.EmailField(max_length=100,blank=False)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return 'Message from'+ self.name

class registrationforevents(models.Model):
    name=models.CharField(max_length=30,blank=False)
    email=models.EmailField(max_length=250,blank=False)
    rollnumber=models.CharField(max_length=50,default="18kb1a05",blank=False)
    year=models.CharField(max_length=20,blank=False)
    section=models.CharField(max_length=20,blank=False)
    dateandtime=models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.name+" of "+self.year+" has registered "
