import logging
from xmlrpc.client import DateTime
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.db.models import Sum
from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from gabriel.pdfChecker.forms import PdfForm
from gabriel.pdfChecker import services
from decimal import Decimal
from datetime import date,datetime, timedelta
from django.db.models import Q
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class UploadPdfView(View):
    logging.debug("UploadPdfView -- GET")
    def get(self, request):
        upload_pdf_form = PdfForm()
        return render(
            request=request,
            template_name="pdfChecker/index.html",
            context={"upload_pdf_form": upload_pdf_form},
        )

    def post(self, request):
        print("UploadPdfView -- POST")
        upload_pdf_form = PdfForm(
            data=request.POST or None, files=request.FILES or None
        )
        if upload_pdf_form.is_valid():
            print(f'Datos limpios pdf {upload_pdf_form.cleaned_data}')
            pdf_instance = upload_pdf_form.save()
            print(f'a ver que wea tiene esto: {pdf_instance}')
            pdf_state = services.checkPdf(pdf_instance)
            messages.success(request, "PDF subido con éxito.")
            return render(
                request,
                template_name="pdfChecker/index.html",
                context={
                    "upload_pdf_form": PdfForm(),
                    "pdf_state": pdf_state,
                },
            )
        else:
            messages.error(request, "Error al cargar el PDF.")
        return HttpResponseRedirect("/")