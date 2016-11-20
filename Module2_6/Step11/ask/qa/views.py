from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from qa.models import Question, Answer
from qa.forms import AnswerForm, AskForm


def paginate(request, obj_list):
    paginator = Paginator(
        obj_list,
        10
    )
    page = request.GET.get("page")
    try:
        page = paginator.page(page)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return paginator, page


def test(request, *args, **kwargs):
    return HttpResponse("OK")


def index(request):
    paginator, page = paginate(request, Question.objects.new())
    return render(
        request,
        "list.html",
        {
            "title": "NEW QUESTIONS",
            "page": page,
            "paginator": paginator,
        }
    )


def popular(request):
    paginator, page = paginate(request, Question.objects.popular())

    return render(
        request,
        "list.html",
        {
            "title": "POPULAR QUESTIONS",
            "page": page,
            "paginator": paginator,
        }
    )


def question(request, id):
    question = get_object_or_404(Question, id=id)
    answers = question.answer_set.all()
    if request.method == "GET":
        form = AnswerForm(initial={"question": question.id})

    return render(
        request,
        "question.html",
        {
            "question": question,
            "answers": answers,
            "form": form,
        }
    )


def answer(request):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            answer.author = request.user
            answer.save()
            return redirect(answer.question)
    else :
        raise Http404


def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            question.author = request.user
            question.save()
            return redirect(question)
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
