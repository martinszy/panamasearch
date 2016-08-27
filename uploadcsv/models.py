from __future__ import unicode_literals

from django.db import models
from django import forms

# Create your models here.
class Namelist(models.Model):
    upload_date = models.DateField(auto_now=True)
    done_date = models.DateField(null=True)
    namefile = models.FileField(upload_to="names/")
    textlist = models.TextField(null=True,blank=True)
    donefile = models.TextField(null=True)
    status = models.TextField()

class NamelistForm(forms.ModelForm):
    class Meta:
        model = Namelist
        fields = ['namefile', 'textlist']
