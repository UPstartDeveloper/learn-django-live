from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    """A view for the index page."""
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, question_id):
    """A view for the question being asked."""
    return HttpResponse(f"You're looking at question {question_id}")


def results(request, question_id):
    """A view to see answers so far on the poll."""
    response = f"You're looking at the results for {question_id}"
    return HttpResponse(response)


def vote(request, question_id):
    """A view for the voting page."""
    return HttpResponse(f"You're voting on question {question_id}")
