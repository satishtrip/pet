from django.contrib import admin

# Register your models here.
from django.contrib import admin
from post.models import PetPost
from .models import PetPost
admin.site.register(PetPost)
