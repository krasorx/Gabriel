import datetime
from tabnanny import verbose
from django.db import models
from django.core.validators import FileExtensionValidator

class Pdf(models.Model):
    title = models.CharField(max_length=50,default='titulo')
    file = models.FileField(upload_to='pdfs/',default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Pdf"
