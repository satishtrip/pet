from django.contrib import admin

from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .views import(
    PetPostListView,
    PetPostDetailView,
    PetPostCreateView,
    PetPostUpdateView,
    PetPostDeleteView,
    UserPetPostListView,
    ProfileDetailView,
    ProfileListView
)
#from users.views import ProfileDetailView,
from .import views
from django.views.generic.base import RedirectView
urlpatterns = [
    #path('', Pet_LoverListView.as_view(), name='post-home'),
    #path('admin/', admin.site.urls),
    path('home/', PetPostListView.as_view(), name='post-home'),
    path('home/profile/', views.ProfileListView.as_view()),
    path('user/<str:username>', UserPetPostListView.as_view(), name='user-posts'),
    path('home/', views.home, name='post-home'),
    path('about/', views.about, name='post-about'),
    path('petpost/<int:pk>/', PetPostDetailView.as_view(), name='petpost-detail'),
    path('petpost/create/', PetPostCreateView.as_view(), name='petpost-create'),
    path('post/<int:pk>/update/', PetPostUpdateView.as_view(), name='petpost-update'),
    path('petpost/<int:pk>/delete/', PetPostDeleteView.as_view(), name='petpost-delete'),
    path('home/profile/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('user/<str:username>', UserPetPostListView.as_view(), name='user-posts'),
    #path('profile/<int:pk>', ProfileDetailView.as_view()),
    #path('petpost/', views.PetPostListView.as_view()),

    #path('post/create/', PetPostCreate.as_view(), name='post-petpost'),
    #path('becomesitter/', views.becomesitter, name='post-becomesitter'),
   # path('cab/', views.cab, name='post-cab'),
   # path('yourbooking/',views.yourbooking, name='post-yourbooking'),
    #path('cakes/',views.cakes, name='post-cakes'),
    #path('petloverprofile/', views.petloverprofile, name='post-petloverprofile'),
]