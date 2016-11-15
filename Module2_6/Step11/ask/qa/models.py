from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):

    def new(self):
        return self.order_by('-added_at')
    
    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):

    title = models.CharField(
        blank=False,
        default="",
        max_length=255
    )
    text = models.TextField(
        blank=False,
        default=""
    )
    added_at = models.DateTimeField(
        auto_now_add=True,
        blank=False
    )
    rating = models.IntegerField(
        blank=False,
        default=0
    )
    author = models.ForeignKey(
        User,
        blank=False,
        related_name="question_author"
    )
    likes = models.ManyToManyField(
        User,
        blank=True,
        through='Likes'
    )
    objects = QuestionManager()
    
    def get_url(self):
        return "/question/{0}/".format(self.id)

    def __unicode__(self):
        return self.text


class Likes(models.Model):
    question = models.ForeignKey(
        Question,
        blank=False,
        related_name="like_question"
    )
    user = models.ForeignKey(
        User,
        blank=False,
        related_name="like_user"
    )
    date = models.DateTimeField(
        auto_now_add=True,
        blank=False
    )


class Answer(models.Model):
    text = models.TextField(
        blank=False,
        default=""
    )
    added_at = models.DateTimeField(
        auto_now_add=True,
        blank=False
    )
    question = models.ForeignKey(
        Question,
        blank=False
    )
    author = models.ForeignKey(
        User,
        blank=False,
        related_name="answer_author"
    )
    
    def __unicode__(self):
        return self.text
