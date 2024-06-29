from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the dog index.")

def detail(request, question_id):
    response = "You're on the details page of the question %s."
    return HttpResponse(response % question_id)

def results(request, question_id):
    response = "You're on the results page of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're on the voting page of the question %s." % question_id)
