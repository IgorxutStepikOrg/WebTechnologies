from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from qa.models import Question, Answer


class AskForm(forms.Form):

    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

#    def clean(self):
#        return self.cleaned_data

#    def save(self):
#        return Question.objects.create(**self.cleaned_data)

    author = 1

    def clean_title(self) :
        title = self.cleaned_data['title']
        return title

    def clean_text(self) :
        text = self.cleaned_data['text']
        return text

    def save(self) :
        quest = Question.objects.create(title=self.cleaned_data['title'], text=self.cleaned_data['text'], author=self.author)
        return quest

class AnswerForm(forms.Form):

    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean_question(self):
        question_id = self.cleaned_data["question"]
        try:
            question = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            question = None
        return question

    def clean(self):
        return self.cleaned_data

    def save(self):
        return Answer.objects.create(**self.cleaned_data)
