from django.contrib import admin
from .models import Profile
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','image','first_name','last_name','address','age','zip_code','phone','describe_yourself','experience',
                  'hourly_rate','overnight_rate','dog_firstaid_and_or_CPR','member_of_any_organisation','organisation_name',
                  'job_type','gender','pet_preference','date_posted','your_photos_with_pets'      )
    #list_editable = ('status','message')
    list_filter = ['job_type',]
admin.site.register(Profile, ProfileAdmin)
#admin.site.register(Profile)
