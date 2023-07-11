import datetime
from tabnanny import verbose
from django.db import models
from django.core.validators import FileExtensionValidator

class Pdf(models.Model):
    Pdf = models.FileField(
        verbose_name="Pdf",
        validators=[FileExtensionValidator(allowed_extensions=["pdf"])],
    )

    def __str__(self):
        return self.Pdf.name

    class Meta:
        verbose_name = "Pdf"
