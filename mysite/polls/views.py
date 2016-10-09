from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello world. You are the poll app index')
# Create your views here.

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    return HttpResponse("You're voting on question %s". % question_id)
