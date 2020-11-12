from django.shortcuts import render,redirect
from django.db import models
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponse
from django.contrib.auth.models import User
from PIL import Image
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
#from.models import Pet_Lover
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from users.models import Profile
#from rest_meets_djongo.serializers import DjongoModelSerializer
from.models import PetPost
from django.views.generic.detail import DetailView
from django.db.models import Q
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
import string
#from django.views.generic.list import ListView
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


from django.core.paginator import Paginator
from bbmp.models import License
from petcab.models import Petcab
#from bbmp.forms import LicenseApplyForm
#from .forms import BecomesitterForm, ProfileUpdateForm









@login_required
def home(request):

    context = {
        'posts': PetPost.objects.all()
    }
    return render(request, 'post/home.html', context)






@method_decorator(login_required, name="dispatch")
class PetPostCreateView(LoginRequiredMixin, CreateView):
    model = PetPost
    fields = ["interests", "working_style", "photo_with_pets"]
    def form_valid(self, form):
        form.instance.pet_lover = self.request.user.profile
        return super().form_valid(form)





#class PetPostListView(ListView):
    #model = PetPost
    #template_name = 'post/home.html'
    #def get_queryset(self):
     #   si = self.request.GET.get("si")
   #     if si == None:
  #          si = ""
 #       return PetPost.objects.filter(Q(pet_lover = self.request.user.profile)).filter(Q(interests__icontains = si) | Q(working_style__icontains = si)).order_by("-id");


class PetPostListView(ListView):
    model = PetPost
    template_name = 'post/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3
    def get_queryset(self):
        si = self.request.GET.get("si")
        if si == None:
            si = ""
        return PetPost.objects.filter(
            Q(interests__icontains=si) | Q(working_style=si)).order_by("-id");

#    objects.filter(
 #       Q(name__icontains=si) | Q(address__icontains=si) | Q(gender__icontains=si) | Q(status__icontains=si)).order_by(
  #      "-id");


class UserPetPostListView(ListView):
    model = PetPost
    template_name = 'post/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return PetPost.objects.filter(pet_lover=user).order_by('-date_posted')


class PetPostUpdateView(UpdateView):
    model = PetPost
    fields = ["interests", "working_style", "photo_with_pets"]

    def form_valid(self, form):
        form.instance.pet_lover = self.request.user.profile
        return super().form_valid(form)


    def test_func(self):
        petpost = self.get_object()
        if self.request.user == petpost.pet_lover:
            return True
        return False








@method_decorator(login_required, name="dispatch")
class PetPostDetailView(DetailView):
    model = PetPost


class PetPostDeleteView(DeleteView):
   model = PetPost
   success_url = '/home/'

   def test_func(self):
       petpost = self.get_object()
       if self.request.user == petpost.pet_lover:
           return True
       return False





@method_decorator(login_required, name="dispatch")
class ProfileDetailView(DetailView):
    model = Profile
    template_name = "post/profile_detail.html"




@method_decorator(login_required, name="dispatch")
class ProfileListView(ListView):
    model = Profile
    template_name = 'users/profile_list.html'
    ordering = ['-date_posted']
    paginate_by = 3
    def get_queryset(self):
        si = self.request.GET.get("si")
        if si == None:
            si = ""
        return Profile.objects.filter(Q(first_name__icontains = si) | Q(address__icontains=si) | Q(job_type__icontains=si) | Q(pet_preference__icontains=si)).order_by("-id");





def about(request):
    return render(request, 'post/about.html', {'title': 'About'})








# Create your views here.

























#def cab(request):
 #   return render(request, 'post/cab.html', {'title': 'Book a ride for yourself and your furry friend'})






























#def cakes(request):
 #   context = {
  #      'prod': Products.objects.all()
   # }
    #return render(request,'post/cakes.html',context)

