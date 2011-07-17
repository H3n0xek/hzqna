from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from tagging.fields import TagField
from managers import OpenQuestionsManager, ClosedQuestionsManager


class Question(models.Model):
    author = models.ForeignKey(User)
    pub_date = models.DateTimeField(default=datetime.now)
    title = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    tags = TagField(blank=True)
    is_closed = models.BooleanField()
    objects = models.Manager()
    opened = OpenQuestionsManager()
    closed = ClosedQuestionsManager()



class Answer(models.Model):
    author = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    pub_date = models.DateTimeField()
    text = models.TextField()
    is_best = models.BooleanField(default=False)
    
