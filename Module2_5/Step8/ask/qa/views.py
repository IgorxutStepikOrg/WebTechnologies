from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator

from qa.models import Question, Answer


def test(request, *args, **kwargs):
    return HttpResponse("OK")


def paginate(request, obj_list):
    p = Paginator(
        obj_list,
        10
    )
    page = request.GET.get("page")
    try:
        obj_list = p.page(page)
    except PageNotAnInteger:
        obj_list = p.page(1)
    except EmptyPage:
        obj_list = p.page(p.num_pages)

    return obj_list


def index(request):
    questions = paginate(request, Question.objects.new())

    return render(
        request,
        "list.html",
        {
            "title": "NEW QUESTIONS",
            "questions": questions,
            "user": request.user,
            "session": request.session,
        }
    )


def popular(request):
    questions = paginate(request, Question.objects.popular())

    return render(
        request,
        "list.html",
        {
            "title": "POPULAR QUESTIONS",
            "questions": questions,
            "user": request.user,
            "session": request.session,
        }
    )


def question(request, num):
    try:
        question = Question.objects.get(id=num)
    except Question.DoesNotExist:
        raise Http404

    return render(
        request,
        "question.html",
        {
            "question": question,
            "user": request.user,
            "session": request.session,
        }
    )
