from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def projects(request):
    return HttpResponse("These are all our projects")

def project(request, pk):
    return HttpResponse("Project: " + pk)
