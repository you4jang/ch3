# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Question


def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        return render(request, 'polls/detail.html', {'question': question})
    except Question.DoesNotExist:
        raise Http404('Question 오브젝트를 찾을 수 없음.')


def vote(request, question_id):
    pass


def result(request, question_id):
    pass
