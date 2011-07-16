from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Question(models.Model):
    author = models.ForeignKey(User)
    pub_date = models.DateTimeField(default=datetime.now)

