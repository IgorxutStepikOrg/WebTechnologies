from django import forms
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from qa.models import Question, Answer


def empty_validation(var):
    if var is Null or var.strip() == "":
        raise forms.ValidationError("Field is empty", code="validation_error")


class AskForm(forms.Form):

    title = forms.CharField(max_length=255, label="title")
    text = forms.CharField(widget=forms.Textarea, label="text")

    def clean_title(self)
        title = self.cleaned_data["title"]
        empty_validation(title)
        return title

    def clean_text(self)
        text = self.cleaned_data["text"]
        empty_validation(text)
        return text

    def save(self):
        if self._user.is_anonymous():
            self.cleaned_data["author_id"] = 1
        else:
            self.cleaned_data["author"] = self._user
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):

    text = forms.CharField(widget=forms.Textarea, label="text")
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean_text(self)
        text = self.cleaned_data["text"]
        empty_validation(text)
        return text

    def clean_question(self):
        question_id = self.cleaned_data["question"]
        try:
            question = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            question = None
        return question

    def save(self):
        self.cleaned_data["question"] = get_object_or_404(Question, pk=self.cleaned_data["question"])
        if self._user.is_anonymous():
            self.cleaned_data["author_id"] = 1
        else:
            self.cleaned_data["author"] = self._user
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
