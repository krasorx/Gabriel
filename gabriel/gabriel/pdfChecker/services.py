import logging
import os
from datetime import datetime, timedelta
from decimal import Decimal
from fileinput import filename
from io import BytesIO
from urllib import response
from wsgiref.util import FileWrapper
from .models import Pdf
import pandas as pd
import xlwings as xw
from gabriel.settings import BASE_DIR
from gabriel.pdfChecker.models import Pdf
from django.conf import settings
from django.contrib.staticfiles import finders
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template, render_to_string
from xhtml2pdf import pisa
from PyPDF4 import PdfFileReader
from io import BytesIO

def is_pdf_full_permissions(document: str) -> bool:
    try:
        with open(document, 'rb') as f:
            pdf_reader = PdfFileReader(f)
            return not pdf_reader.getIsEncrypted()
    except FileNotFoundError:
        return False
    except Exception as e:
        # Handle specific exceptions, e.g., PyPDF4.PdfReadError, etc.
        print(f"Error while checking PDF permissions: {e}")
        return False

def is_signed_pdf(archivo: bytes) -> bool:
    try:
        with BytesIO(archivo) as f:
            pdf_reader = PdfFileReader(f)
            return len(pdf_reader.getFields()) > 0
    except Exception as e:
        print(f"Error while checking if PDF is signed: {e}")
        return False

def checkPdf(pdf_instance: Pdf) -> dict:
    pdf_state = {
        "name": pdf_instance.title,
        "is_signed": False,
        "is_unlocked": False,
    }
    if is_pdf_full_permissions(pdf_instance.file.path):
        pdf_state["is_unlocked"] = True
    else:
        print(f'{pdf_instance} no tiene todos los permisos')

    with open(pdf_instance.file.path, 'rb') as f:
        pdf_bytes = f.read()
        if is_signed_pdf(pdf_bytes):
            pdf_state["is_signed"] = True
        else:
            print('El PDF esta NO firmado digitalmente')
    return pdf_state


