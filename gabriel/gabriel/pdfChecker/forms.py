from django import forms
from django.forms import FileInput, DateInput
from gabriel.pdfChecker.models import Pdf


class PdfForm(forms.ModelForm):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

    class Meta:
        model = Pdf
        fields = ['title', 'file']
    