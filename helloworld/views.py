from django.shortcuts import render
from django.http import HttpResponse
import logging

def index(request):
    logging.getLogger("error_logger").error("Hi I am here");
    return HttpResponse("Hello World. First Django Project. ThePythonDjango.Com")
