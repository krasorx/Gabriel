import logging
import os
from datetime import datetime, timedelta
from decimal import Decimal
from fileinput import filename
from io import BytesIO
from urllib import response
from wsgiref.util import FileWrapper

import pandas as pd
import xlwings as xw
from gabriel.settings import BASE_DIR
from gabriel.pdfChecker.models import Pdf
from django.conf import settings
from django.contrib.staticfiles import finders
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template, render_to_string
from xhtml2pdf import pisa
from PyPDF2 import PdfFileReader
from io import BytesIO

def is_pdf_full_permissions(document: str) -> bool:
    ret = True
    try:
        with open(document, 'rb') as f:
            pdf_reader = PdfFileReader(f)
            if not pdf_reader.getIsEncrypted():
                ret = False
    except:
        ret = False
    return ret

def is_signed_pdf(archivo: bytes) -> bool:
    ret = False
    try:
        with BytesIO(archivo) as f:
            pdf_reader = PdfFileReader(f)
            ret = len(pdf_reader.getFields()) > 0
    except:
        ret = False
    return ret

def checkPdf(pdf_instance: Pdf) -> None:
    if is_pdf_full_permissions(pdf_instance):
        print(f'{pdf_instance} tiene todos los permisos')
    else:
        print(f'{pdf_instance} no tiene todos los permisos')

    with open(pdf_instance.file.path, 'rb') as f:
        pdf_bytes = f.read()
        if is_signed_pdf(pdf_bytes):
            print('El PDF esta firmado digitalmente')
        else:
            print('El PDF esta NO firmado digitalmente')
    return False


