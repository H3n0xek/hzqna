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
    is_closed = models.BooleanField(default=False)
    objects = models.Manager()
    opened = OpenQuestionsManager()
    closed = ClosedQuestionsManager()

    def __unicode__(self):
	return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('view-question', [str(self.id)])


class Answer(models.Model):
    author = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    pub_date = models.DateTimeField(default=datetime.now)
    text = models.TextField()
    is_best = models.BooleanField(default=False)

    def __unicode__(self):
	return "%s: %s" % (self.author, self.question.title)


