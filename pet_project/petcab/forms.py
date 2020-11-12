from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from django.forms.fields import DateField
from django import forms
from .models import Petcab

from datetime import datetime
import datetime
from datetimewidget.widgets import DateTimeWidget
#import django.forms.extras.widgets
from bootstrap_datepicker_plus import DatePickerInput
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
class DateInput(forms.DateInput):
    input_type = 'date'

import datetime
class TimeInput(forms.TimeInput):
    input_type = 'time'

class PetcabForm(forms.ModelForm):





    class Meta:
        model = Petcab
        fields = ( 'name','source',
    'destination',
    'depart_at',
    'ride_date',
    'no_of_travellers',
    'phone_no',)

        widgets = {
            'depart_at': TimePickerInput(),
            'ride_date': DatePickerInput(
                options={
                    'minDate': (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d 00:06:00'),
                    'maxDate': (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%Y-%m-%d 21:59:59'),
                    'enabledHours': [6,7,8, 9, 10, 11, 12, 13, 14, 15, 16, 17,18,19,20,21,22],
                }
            ),

                 }
