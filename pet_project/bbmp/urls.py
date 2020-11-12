
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView,CreateView
from .views import(
    pdf_template,
    LicenseDetailView,
    LicenseCreateView,
)
from .models import License
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .import views

urlpatterns = [
    #path('license/',views.license, name='bbmp-license'),
    path('licenseapplication/', views.licenseapplication, name='bbmp-licenseapplication'),
    path('license/create/', LicenseCreateView.as_view(), name='bbmp-license'),
    path('pdf_view/', views.pdf_template.as_view(), name="pdf_template"),
    path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),

    path('license/<int:pk>/', LicenseDetailView.as_view(), name='license-detail'),

    ]