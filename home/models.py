from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from django.db.models.enums import Choices
from django.forms import ModelForm

# Create your models here.
class Setting(models.Model):
    place = models.ImageField(blank=True, null=True, upload_to='images/')
    fusce = models.ImageField(blank=True, null=True, upload_to='images/')
    beautiful1 = models.ImageField(blank=True, null=True, upload_to='images/')
    beautiful2 = models.ImageField(blank=True, null=True, upload_to='images/')
    beautiful3 = models.ImageField(blank=True, null=True, upload_to='images/')
    beautiful4 = models.ImageField(blank=True, null=True, upload_to='images/')

class ContactMessage(models.Model):
    STATUS =(
        ('New','New'),
        ('Read','Read'),
        ('pending','pending'),
        ('Closed','Closed'),
    )
    name = models.CharField(max_length=100,blank=True, null=True)
    email = models.CharField(max_length=100,blank=True, null=True)
    message = models.CharField(max_length=300,blank=True,null=True)
    notes = models.CharField(max_length=100,blank=True)
    status = models.CharField(choices=STATUS, default='New', max_length=10)
    created_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name','email','message']

class Images(models.Model):
    STATUS=(
        ('uploaded','uploaded'),
        ('new','new'),
    )
    page2_img1 = models.ImageField(blank=True, null=True,upload_to='images/')
    page2_img2 = models.ImageField(blank=True, null=True,upload_to='images/')
    page3_img1 = models.ImageField(blank=True, null=True,upload_to='images/')
    page3_img2 = models.ImageField(blank=True, null=True,upload_to='images/')
    page3_img3 = models.ImageField(blank=True, null=True,upload_to='images/')
    page3_img4 = models.ImageField(blank=True, null=True,upload_to='images/')