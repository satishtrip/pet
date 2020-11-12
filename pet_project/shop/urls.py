from django.contrib import admin

from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from . import views

from django.views.generic.base import RedirectView

app_name = 'shop'
urlpatterns = [
    #path(, views.index, name="ShopHome"),
    path("", views.index, name="HomeView"),
    path('aboutshop/', views.aboutshop, name='shop-aboutshop'),
    #path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="shop-TrackingStatus"),
    path("search/", views.search, name="shop-Search"),
    path("products/<int:myid>/", views.productView, name="shop-productView"),
    path("checkout/", views.checkout, name="shop-Checkout"),
    #path("handlerequest/", views.handlerequest, name="HandleRequest"),

    #path('petloverprofile/', views.petloverprofile, name='post-petloverprofile'),
]