from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from djongo import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.forms.models import model_to_dict
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import UserPassesTestMixin

from .models import License
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,)
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from django.http import HttpResponse
from django.views.generic import View

#from pet_project.utils import render_to_pdf
#created in step 4

#from .forms import LicenseApplyForm
# Create your views here.
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa

def licenseapplication(request):
    model = License
    context = {
        'posts': License.objects.all()
    }
    return render(request, 'bbmp/licenseapplication.html', context)

def render_to_pdf(request,template_src, context_dict):
    template = get_template(template_src)
    model = License
    data = {
        'posts': License.objects.all()
    }
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(request,result.getvalue(), content_type='application/pdf')
    return None

#@login_required()
class LicenseCreateView(SuccessMessageMixin,CreateView):
    model = License
    fields = ['first_name','last_name','pet_name','pet_colour','pet_breed','pet_age','address','phone','pet_gender','pet_type','application_preference',
                  'old_license','vaccination_record','address_proof']
    success_url = '/licenseapplication'
    def form_valid(self, form):
        form.instance.user = self.request.user
       # success_message =  "Application Submitted Successfully, We will contact you for further updates!"
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return"Application Submitted Successfully, Keep Checking Your Status, We will contact you for further updates!"



@method_decorator(login_required, name="dispatch")
class LicenseDetailView(DetailView):
    model = License
    def test_func(self):
        license = self.get_object()
        if self.request.user == license.user:
            return True
        return False


@method_decorator(login_required, name="dispatch")
class LicenseListView(ListView):
    model = License

    def test_func(self):
        license = self.get_object()
        if self.request.user == license.user:
            return True
        return False
    template_name = 'users/profile_list.html'
    ordering = ['-date_posted']
    paginate_by = 3
    def get_queryset(self):
        si = self.request.GET.get("si")
        if si == None:
            si = ""
        return License.objects.filter(Q(first_name__icontains = si) | Q(address__icontains=si) | Q(job_type__icontains=si) | Q(pet_preference__icontains=si)).order_by("-id");




def render_to_pdf(request,template_src, context_dict={}):
    model = License

    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(request,result.getvalue(), content_type='application/pdf')
    return None







# Opens up page as PDF
@method_decorator(login_required, name="dispatch")
class pdf_template(View):
    model = License
    template_name = 'bbmp/pdf_template'

    def get(request,self,  *args, **kwargs):
        model = License
        data = {
            'posts': License.objects.filter()
        }
        pdf = render_to_pdf(request,'bbmp/pdf_template.html', data)
        return HttpResponse(request,pdf, content_type='application/pdf')










# Automaticly downloads to PDF file
@method_decorator(login_required, name="dispatch")
class DownloadPDF(View):
    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('app/pdf_template.html', data)

        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Invoice_%s.pdf" % ("12341231")
        content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response

