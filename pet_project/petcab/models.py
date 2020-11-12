from django.db import models
from datetime import datetime
#from django.db import models from django_date_validators.validators import date_is_present_or_future
from datetime import datetime
import datetime
from django import forms
now = datetime.datetime.now()
from django.contrib.auth.models import User
from django.contrib import admin
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.urls import reverse
from django.core.exceptions import ValidationError
from users.models import Profile
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget
from django.utils import timezone



# Create your models here.




class Petcab(models.Model):
    pet_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    depart_at = models.TimeField()
    ride_date = models.DateTimeField(default=datetime.datetime.today().now())
    no_of_travellers = models.IntegerField(validators=[MinValueValidator(2),
                                       MaxValueValidator(4)])
    BOOKED = 'Booked'
    PENDING = 'Pending'

    TICKET_STATUSES = ((BOOKED, 'Booked'),
                       (PENDING, 'Pending'),)
    status = models.CharField(choices=TICKET_STATUSES, max_length=7, default='Pending')
    message = models.CharField(max_length=1000, default="Please Check Again After Some Time")
    phone_no = models.CharField(max_length=10, blank=True, null=True)





    #def clean_ride_date(self):
     #   if self.ride_date.now() < datetime.datetime.today():
      #      raise forms.ValidationError("The date cannot be in the past!")
       # return ride_date



    options = {
        'minDate': (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d 00:00:00'),
        'maxDate': (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%Y-%m-%d 23:59:59'),
        'enabledHours': [8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
    }


    def __str__(self):
        return f'{self.pet_owner} Petcab'

    def get_absolute_url(self,**kwargs):
        return reverse('petcab-detail', kwargs={'pk': self.pk})


#class Booking(models.Model):
 #   booked_by = models.ForeignKey(Petcab,on_delete=models.CASCADE)
  #  BOOKED = 'B'
   # PENDING = 'P'

    #TICKET_STATUSES = ((BOOKED, 'Booked'),
                       #
       # (PENDING, 'Pending'),)
    #status = models.CharField(choices=TICKET_STATUSES, max_length=2)

    #def ____(self):
     #   return self.booked_by



    #per_km_rate = models.IntegerField()




