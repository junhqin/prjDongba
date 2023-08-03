from django.db import models
from django.forms import ModelForm
# Create your models here.
import os
from django.core.files.storage import FileSystemStorage
from django.conf import settings


class IMG(models.Model):
    img = models.ImageField(upload_to='img')
    name = models.CharField(max_length=20)

