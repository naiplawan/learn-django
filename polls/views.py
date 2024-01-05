from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse 
from .models import Question
from django.http import Http404

# Create your views here.

## write function to return request object to the browser
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context) # render function takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument

def detail(request, question_id):
    try:
       question = get_object_or_404(Question, pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response %question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)