from django.urls import path
from gabriel.pdfChecker import views

urlpatterns = [
    path("", views.UploadPdfView.as_view(), name="index"),
]