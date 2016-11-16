from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from qa.models import Question, Answer


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
    if request.method == "POST":
        form = AnswerForm(request.POST)
        form._user = request.user
        if form.is_valid():
            form.save()
            url = question.get_url()
            return redirect(url)
    else:
        form = AnswerForm()

    return render(
        request,
        "question.html",
        {
            "question": question,
            "user": request.user,
            "session": request.session,
            "form": form,
        }
    )

def answer(request):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        form._user = request.user
        if form.is_valid():
            answer = form.save()
            url = answer.question.get_url()
            return redirect(url)
    else:
        form = AnswerForm()

    return render(
        request,
        "answer.html",
        {
            "form": form,
            "button_name": "answer",
            "url_name": "answer",
        }
    )
    
def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        form._user = request.user
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return redirect(url)
    else:
        form = AskForm()

    return render(
        request,
        "ask.html",
        {
            "form": form,
            "button_name": "ask",
            "url_name": "ask"
        }
    )
