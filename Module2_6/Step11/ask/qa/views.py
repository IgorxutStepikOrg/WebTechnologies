from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.paginator import Paginator

from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm


@csrf_protect
def test(request, *args, **kwargs):
    return HttpResponse('OK')


@csrf_protect
def index(request):
    questions_list = Question.objects.new()
    paginator = Paginator(
        questions_list,
        10
    )
    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(
        request,
        'list.html',
        {
            'title': 'NEW QUESTIONS',
            'questions': questions,
            'user': request.user,
            'session': request.session,
        }
    )

@csrf_protect
def popular(request):
    questions_list = Question.objects.popular()
    paginator = Paginator(
        questions_list,
        10
    )
    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(
        request,
        'list.html',
        {
            'title': 'POPULAR QUESTIONS',
            'questions': questions,
            'user': request.user,
            'session': request.session,
        }
    )


@csrf_protect
def question(request, num):
    try:
        q = Question.objects.get(id=num)
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
        form = AnswerForm(initial={'question': q.id})
    return render(
        request,
        'question.html',
        {
            'question': q,
            'form': form,
            'user': request.user,
            'session': request.session,
        }
    )


@csrf_protect
def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            form._user = request.user
            post = form.save()
            url = post.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(
        request,
        'ask.html',
        {
            'form': form,
            'user': request.user,
            'session': request.session
        }
    )


@csrf_protect
def answer(request):
    if request.method == 'POST': 
        form = AnswerForm(request.POST)
        if form.is_valid():
            form._user = request.user 
            post = form.save()
            url = post.get_url()
            return HttpResponseRedirect(url)
    return HttpResponseRedirect('/')
