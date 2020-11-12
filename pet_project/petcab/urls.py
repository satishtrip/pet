from .import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView,CreateView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget

from .models import Petcab
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .views import(
    PetcabDetailView,
    PetcabDeleteView,
    PetcabCreateView,
)


urlpatterns = [
    #path('license/',views.license, name='bbmp-license'),
    path('booking/', views.booking, name='petcab-booking'),
    path('petcab/create/', PetcabCreateView.as_view(), name='petcab-petcab'),
    path('petcab/<int:pk>/', PetcabDetailView.as_view(), name='petcab-detail'),

   # path('booking/<int:pk>/', PetcabDetailView.as_view(), name='petcab-detail'),

    path('petcab/<int:pk>/delete/', PetcabDeleteView.as_view(), name='petcab-delete'),

    #path('license/<int:pk>/', LicenseDetailView.as_view(), name='license-detail'),

    ]