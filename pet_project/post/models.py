from django.db import models

# Create your models here.
from djongo import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from users.models import Profile




class PetPost(models.Model):
    #petpost_id = models.IntegerField(primary_key=True)
    interests = models.CharField(max_length=150)
    working_style = models.TextField(null=True, blank=True)
    pet_lover = models.ForeignKey(to=Profile, on_delete=models.CASCADE,null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    photo_with_pets = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return f'{self.pet_lover} Petpost'


    def get_absolute_url(self):
        return reverse('petpost-detail', kwargs={'pk': self.pk})




    def get_absolute_url(self):
        return reverse('petpost-detail', kwargs={'pk': self.pk})

    #def get_absolute_url(self):
     #   return reverse('profile-detail', kwargs={'pk': self.pk})

    def photo_with_pets_url(self):
        if self.photo_with_pets and hasattr(self.photo_with_pets, 'url'):
            return self.photo_with_pets.url


