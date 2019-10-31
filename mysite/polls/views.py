from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.shortcuts import render


def index(request):
    """Display latest 5 questions."""
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    """A view for the question being asked."""
    return HttpResponse(f"You're looking at question {question_id}")


def results(request, question_id):
    """A view to see answers so far on the poll."""
    response = f"You're looking at the results for question {question_id}"
    return HttpResponse(response)


def vote(request, question_id):
    """A view for the voting page."""
    return HttpResponse(f"You're voting on question {question_id}")
