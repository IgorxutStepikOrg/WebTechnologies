from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):

    def new(self):
        return self.order_by('-added_at')
    
    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    title = models.CharField(
        default="",
        max_length=255
    )
    text = models.TextField(
        default=""
    )
    added_at = models.DateTimeField(
        auto_now_add=True
    )
    rating = models.IntegerField(
        default=0
    )
    author = models.ForeignKey(
        User,
        related_name="question_author"
    )
    likes = models.ManyToManyField(
        User,
        through='Likes'
    )
    objects = QuestionManager()

    def __unicode__(self):
        return self.text

    
class Likes(models.Model):
    question = models.ForeignKey(
        Question,
        related_name="like_question"
    )
    user = models.ForeignKey(
        User,
        related_name="like_user"
    )
    date = models.DateTimeField(
        auto_now_add=True
    )


class Answer(models.Model):
    text = models.TextField(
        default=""
    )
    added_at = models.DateTimeField(
        auto_now_add=True
    )
    question = models.ForeignKey(
        Question
    )
    author = models.ForeignKey(
        User,
        related_name="answer_author"
    )
    
    def __unicode__(self):
        return self.text
