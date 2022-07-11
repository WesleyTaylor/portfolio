from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    template = "home.html"
    context = {}
    return render(request, template, context)

def contact(request):
    template = "contact.html"
    context = {}
    return render(request, template, context)

def about(request):
    template = "about.html"
    context = {}
    return render(request, template, context)

def resume(request):
    template = "resume.html"
    context = {}
    return render(request, template, context)

def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))