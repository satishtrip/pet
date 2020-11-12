from django import forms

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','first_name','last_name','address','age','zip_code','phone','describe_yourself','experience',
                  'hourly_rate','overnight_rate','dog_firstaid_and_or_CPR','member_of_any_organisation','organisation_name',
                  'job_type','gender','pet_preference','date_posted','your_photos_with_pets']




#class Pet_LoverRegisterForm(UserCreationForm):
 #   email = forms.EmailField()

  #  class Meta:
   #     model = Pet_Lover
    #    fields = ['username', 'email', 'password1', 'password2']