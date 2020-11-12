from django.shortcuts import render,redirect
from django.db import models
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from djongo import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget
from.models import Petcab
from .forms import PetcabForm


from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    CreateView,)









def booking(request):
    context = {
        'posts': Petcab.objects.all(),


    }
    return render(request, 'petcab/booking.html', context)

class PetcabCreateView(SuccessMessageMixin,CreateView):
    model = Petcab
    form_class = PetcabForm

    success_url = '/booking'

    def form_valid(self, form):
        form.instance.pet_owner = self.request.user
        # success_message =  "Application Submitted Successfully, We will contact you for further updates!"
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Your pet car has been booked !"

#def petcab(request):
@method_decorator(login_required, name="dispatch")
class PetcabDeleteView(DeleteView):
   model = Petcab
   success_url = '/booking'

   def test_func(self):
       petcab = self.get_object()
       if self.request.user == petcab.pet_owner:
           return True
       return False




@method_decorator(login_required, name="dispatch")
class PetcabDetailView(DetailView):
    model = Petcab
    def test_func(self):
        petcab = self.get_object()
        if self.request.user == petcab.pet_owner:
            return True
        return False






 #   return render(request, 'petcab/petcab_form.html', {'title': 'Book a ride for yourself and your furry friend'})


class PetcabList(ListView):

    template_name = 'petcab/booking.html'

    def get_queryset(self):
        self.pet_owner = get_object_or_404(User, name=self.kwargs['pet_owner'])
        return Petcab.objects.filter(pet_owner=self.pet_owner)



