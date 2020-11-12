from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import  PIL as pillow
from PIL import Image
from django.urls import reverse
#from rest_meets_djongo.serializers import DjongoModelSerializer

from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    one_click_purchasing = models.BooleanField(default=False)

    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    first_name = models.CharField(max_length=100,default="")
    last_name = models.CharField(max_length=100,blank=True)
    address = models.CharField(max_length=100,default="")
    age = models.IntegerField(null=True)
    zip_code = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=10, blank=True,null=True)
    describe_yourself = models.TextField(default="")
    experience = models.IntegerField(null=True)
    hourly_rate = models.IntegerField(null=True)
    overnight_rate = models.IntegerField(null=True,blank=True)

    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
    dog_firstaid_and_or_CPR = models.BooleanField(choices=BOOL_CHOICES, blank=True,null=True)

    bol_choices = ((True, 'Yes'), (False, 'No'))
    member_of_any_organisation = models.BooleanField(choices=bol_choices, blank=True,null=True)

    organisation_name = models.CharField(max_length=50, blank=True)

    PETSITTER = 'Pet Sitter'
    WALKER = 'Walker'
    TRAINER = 'Trainer'
    ALL = 'All'
    jo_type = [
        (PETSITTER, 'Pet Sitter'),
        (WALKER, 'Walker'),
        (TRAINER, 'Trainer'),
        (ALL, 'All'),
    ]
    job_type = models.CharField(max_length=10, blank=True, choices=jo_type, default="Pet Sitter", )

    MALE = 'Male'
    FEMALE = 'Female'

    gen_type = [
        (MALE, 'Male  '),
        (FEMALE, 'Female'),
    ]
    gender = models.CharField(max_length=10, blank=True, choices=gen_type, default=MALE, )

    DOG = 'Dog'
    CAT = 'Cat'
    BOTH = 'Dogs & Cat'
    pet_prefer = [
        (DOG, 'Dog'),
        (CAT, 'Cat'),
        (BOTH, 'Both'),
    ]
    pet_preference = models.CharField(max_length=10, blank=True, choices=pet_prefer, default='Dog')
    date_posted = models.DateTimeField(default=timezone.now)
    your_photos_with_pets = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return f'{self.user.username} '

    def get_absolute_url(self):
        return reverse('profile-detail', kwargs={'pk': self.pk})

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)


