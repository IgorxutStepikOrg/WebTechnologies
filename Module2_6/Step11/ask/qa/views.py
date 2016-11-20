from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from qa.models import Question, Answer
from qa.forms import AnswerForm, AskForm


def test(request, *args, **kwargs):
    return HttpResponse("OK")


def paginate(request, obj_list):
    paginator = Paginator(
        obj_list,
        10
    )
    page = request.GET.get("page")
    try:
        lst = paginator.page(page)
    except PageNotAnInteger:
        lst = paginator.page(1)
    except EmptyPage:
        lst = paginator.page(paginator.num_pages)

    return lst


def index(request):
    questions = paginate(request, Question.objects.new())

    return render(
        request,
        "list.html",
        {
            "title": "NEW QUESTIONS",
            "questions": questions,
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
        }
    )


def question(request, num):
    try:
        question = Question.objects.get(id=num)
    except Question.DoesNotExist:
        raise Http404
    if request.method == "POST":
        form = AnswerForm(request.POST)
        form._user = request.user
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(question.get_url())
    if request.method == "GET":
        form = AnswerForm()

    return render(
        request,
        "question.html",
        {
            "question": question,
            "form": form,
        }
    )


def answer(request):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        form._user = request.user
        if form.is_valid():
            answer = form.save()
            return HttpResponseRedirect(answer.question.get_url())
    else :
        raise Http404


def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        form._user = request.user
        if form.is_valid():
            question = form.save()
            return HttpResponseRedirect(question.get_url())
    if request.method == "GET":
        form = AskForm()

    return render(
        request,
        "ask.html",
        {
            "title": "ASK QUESTION",
            "form": form,
        }
    )
