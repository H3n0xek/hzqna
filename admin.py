from django.contrib import admin
from hzqna.models import Question, Answer


class QuestionAdmin(admin.ModelAdmin):
	date_hierarchy = 'pub_date'

class AnswerAdmin(admin.ModelAdmin):
	date_hierarchy = 'pub_date'

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
