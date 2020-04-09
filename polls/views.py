from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
#se incluyo cuando se creo el htm en templates/polls
from django.template import loader
from .models import Question

# Create your views here.

def index(request):
        #mostrar las últimas 5 preguntas de la encuesta
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        #template = loader.get_template('polls/index.html')
        #el contexto es un diccionario que relaciona los nombres de variables de
        #plantillas con objetos Python
        context = {
                'latest_question_list': latest_question_list,
        }
        #output = ', '.join([q.question_text for q in latest_question_list])
        return render(request, 'polls/index.html', context)

def detail(request, question_id):
        #try:
        question = get_object_or_404(Question, pk=question_id)
        #except Question.DoesNotExist:
                #raise Http404("Question does not exist")
        return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
        response = "You are looking at the results of question %s."
        return HttpResponse(response % question_id)

def vote(request, question_id):
        return HttpResponse("You are voting on question %s." % question_id)
