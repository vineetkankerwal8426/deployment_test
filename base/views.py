from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView
# from django.http import HttpResponses
# Create your views here.


class HomePageView(TemplateView):
    template_name='home.html'

class aboutPageView(TemplateView):
    template_name='about.html'