from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.core.paginator import Paginator, EmptyPage
from hzqna.models import Question, Answer
from hzqna.settings import QUESTIONS_PER_PAGE
from django.http import Http404
from tagging.models import Tag, TaggedItem
from django.shortcuts import get_object_or_404

class ListQuestionsGeneric(ListView):
	def get_queryset(self):
            page = self.kwargs['page'] # or None
            if not page: page = 1
	    tagname = self.kwargs.get('tagname', None)
	    if tagname:
		objects = self.get_tagged(tagname)		
	    else:
		objects = self.queryset_base.all()		
	    paginator = Paginator(objects, QUESTIONS_PER_PAGE)
	    try:
		self.questions = paginator.page(page)
	    except EmptyPage:
		raise Http404        

	def get_context_data(self, **kwargs):
		context = super(ListQuestionsGeneric, self).get_context_data(**kwargs)
		try:
			context['question_list'] = self.questions
		except KeyError:
			raise Http404
		return context

	def get_tagged(self, tagname):
		tag = Tag.objects.get(name=tagname)
		questions = TaggedItem.objects.usage_for_queryset(self.queryset_base.all(), tag)		
		if not len(questions):
			raise Http404
		return questions

		
class ListOpened(ListQuestionsGeneric):
    template_name = "qna/list_opened.html"
    queryset_base = Question.opened
	
	
class ListClosed(ListQuestionsGeneric):
	template_name = 'qna/list_closed.html'
	queryset_base = Question.closed

	
	
	
class ListByUser(ListView):
	def get_queryset(self):
		page = self.kwargs.get('page', 1)
		userid = self.kwargs.get('userid', 0)
		if not userid:
			raise Http404
	        self.results = self.queryset_base.filter(author__id=userid)
	
	def get_context_data(self, **kwargs):
		context = super(ListByUser, self).get_context_data(**kwargs)
		try:
			context[self.ctxvar] = self.results
		except KeyError:
			raise Http404
	
class ListUserQuestions(ListByUser):
	template_name = 'qna/list_user_questions.html'
	queryset_base = Question.objects
	ctxvar = 'question_list'

class ListUserAnswers(ListByUser):
	template_name = 'qna/list_user_answers.html'
	queryset_base = Answer.objects
	ctxvar = 'answer_list'


class ViewQuestion(DetailView):
	context_object_name = 'question'
	template_name = 'qna/view_question.html'	
	model = Question

	def get_context_data(self, **kwargs):
		context = super(ViewQuestion, self).get_context_data(**kwargs)
		context['answers'] = Answer.objects.filter(question__pk=self.kwargs.get('pk', 0))
		return context

