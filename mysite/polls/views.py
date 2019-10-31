from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Choice, Question
from django.urls import reverse
from django.views import generic


class IndexView(generic.ListView):
    """Index view implemented using generic templating system."""
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    """View for one question implemented using generic templating system."""
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    """Results view implemented using generic templating system."""
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    """A view for the voting page."""
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request,
                      "polls/detail.html",
                      {
                        'question': question,
                        'error_message': "You didn't select a choice.",
                      })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # prevent data from being posted twice in case hits Back button
        return HttpResponseRedirect(reverse('polls:results',
                                            args=(question.id,)))
