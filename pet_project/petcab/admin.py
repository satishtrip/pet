from django.contrib.auth.models import User
from django.contrib import admin
from .models import Petcab
#rom petcab.models import Booking



class PetcabAdmin(admin.ModelAdmin):
    list_display = ('id','name','source',
    'destination',
    'depart_at',
    'ride_date',
    'no_of_travellers',
    'phone_no',
     'status',
      'message'       )
    list_editable = ('status','message')
    list_filter = ['ride_date',]
admin.site.register(Petcab, PetcabAdmin)
#admin.site.register(Booking)
