
from django.db import models
from django.urls import reverse
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from users.models import Profile
from django.core.validators import FileExtensionValidator
#from .forms import LicenseApplyForm
#from .views import LicenseView
# Create your models here.

class License(models.Model):
   # models.ForeignKey(to=Profile, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    pet_name =  models.CharField(max_length=100)
    pet_colour = models.CharField(max_length=100)
    pet_breed = models.CharField(max_length=100)
    pet_age = models.FloatField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10, blank=True,null=True)
    date_applied = models.DateTimeField(default=timezone.now)


    RECEIVED = 'Received'
    INVALID = 'Invalid'
    OUTFORDELIVERY = 'Out for delivery'

    TICKET_STATUSES = ((  RECEIVED, 'Received'),
                   (INVALID, 'Invalid'),
                    (OUTFORDELIVERY, 'Out for delivery'),)



    status = models.CharField(choices=TICKET_STATUSES, max_length=16, default='Received')
    message = models.CharField(max_length=1000, default="Information Received, Kindly Check Again After Sometime for further updates!")


    MALE = 'Male'
    FEMALE = 'Female'

    pet_gen = [
        (MALE, 'Male  '),
        (FEMALE, 'Female'),
    ]
    pet_gender = models.CharField(max_length=10, blank=True, choices=pet_gen, default=MALE, )

    DOG= 'Dog'
    CAT = 'Cat'
    pettype_sel = (
        (DOG, "Dog"),
        (CAT, "Cat"),
    )


    pet_type = models.CharField(max_length=3, blank=True,choices=pettype_sel,default = DOG, )

    RENEW = 'Renew'
    NEW = 'New'

    appl_prefer = [
        (RENEW, 'Renew'),
        (NEW, 'New'),

    ]
    application_preference = models.CharField(max_length=5, blank=True, choices=appl_prefer, default=NEW, )

    old_license = models.FileField(upload_to='media',blank=True,validators=[FileExtensionValidator(['pdf'])])
    vaccination_record = models.FileField(upload_to='media',validators=[FileExtensionValidator(['pdf'])])

    address_proof =  models.FileField(upload_to='media',validators=[FileExtensionValidator(['pdf'])])

    def __str__(self):
        return self.first_name

    #def get_absolute_url(self,user_id ):
     #   return reverse('bbmp-license', kwargs={'user_id': self.pk})


    def get_absolute_url(self):
        return reverse('license-detail', kwargs={'pk': self.pk})



    #def get_absolute_url(self):
     #   return reverse('pdf_template', kwargs={'pk': self.pk})

