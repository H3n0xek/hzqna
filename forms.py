from django import forms
from hzqna.models import Question, Answer

class PostQuestionForm(forms.ModelForm):
	model = Question
	exclude = ('pub_date', 'author', 'is_closed')
	
class PostAnswerForm(forms.ModelForm):
	model = Answer
	exclude = ('author', 'question', 'pub_date', 'is_best')

