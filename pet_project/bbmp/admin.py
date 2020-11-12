from django.contrib import admin
from .models import License

#admin.site.register(License)
class LicenseAdmin(admin.ModelAdmin):
    list_display = ('id','user','first_name','last_name','pet_name','pet_colour','pet_breed','pet_age','address','phone','pet_gender','pet_type','application_preference',
                  'old_license','vaccination_record','address_proof','status','message','date_applied')
    list_editable = ('status','message')
    list_filter = ['date_applied',]
admin.site.register(License, LicenseAdmin)