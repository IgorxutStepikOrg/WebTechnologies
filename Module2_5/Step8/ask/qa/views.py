from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.paginator import Paginator

from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm


def test(request, *args, **kwargs):
    return HttpResponse("OK")


def index(request):
    questions_list = Question.objects.new()
    paginator = Paginator(
        questions_list,
        10
    )
    page = request.GET.get("page")
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

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
    questions_list = Question.objects.popular()
    paginator = Paginator(
        questions_list,
        10
    )
    page = request.GET.get("page")
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

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
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            form._user = request.user
            _ = form.save()
            url = q.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm(initial={"question": question.id})

    return render(
        request,
        "question.html",
        {
            "question": question,
            "form": form,
            "user": request.user,
            "session": request.session,
        }
    )
