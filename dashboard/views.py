from django.shortcuts import render

from django.views.generic import TemplateView

class dashboard(TemplateView):

    template_name = 'dashboard.html'
    

# Create your views here.
