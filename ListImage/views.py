from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HelloMask(TemplateView):
    template_name = 'mask.html'