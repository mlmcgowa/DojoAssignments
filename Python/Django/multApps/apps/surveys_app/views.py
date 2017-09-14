from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse, redirect

def index(request):
    return HttpResponse("placeholder to later display all the list of surveys")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new survey")

def create(request):
    return redirect('/surveys_app')

def show(request, survey_id):
    return HttpResponse("placeholder to display survey {}".format(survey_id))

def edit(request, survey_id):
    return HttpResponse("placeholder to edit survey {}".format(survey_id))

def delete(request, survey_id):
    return redirect('/surveys_app')
