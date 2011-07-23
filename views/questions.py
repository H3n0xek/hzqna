from django.views.generic.list import ListView
from django.core.paginator import Paginator, EmptyPage
from hzqna.models import Question
from hzqna.settings import QUESTIONS_PER_PAGE
from django.http import Http404
from tagging.models import Tag, TaggedItem

class ListOpened(ListView):
    template_name = "qna/list_opened.html"
    
	def get_queryset(self):
        page = self.kwargs.get('page', 1)
		tagname = self.kwargs.get('tagname', None)
		if tagname:
			objects = self.get_tagged(tagname)		
		else:
			objects = Question.opened.all()		
			
        paginator = Paginator(objects, QUESTIONS_PER_PAGE)
		try:
			self.questions = paginator.page(page)
		except EmptyPage:
			raise Http404           
    
	def get_context_data(self, **kwargs):
		context = super(PublishedDetailView, self).get_context_data(**kwargs)
		try:
			context['question_list'] = self.questions
		except KeyError:
			raise Http404
		return context

	def get_tagged(self, tagname):
		tag = Tag.objects.get(name=tagname)
		questions = TaggedItem.objects.get_by_model(Question, tag)
		if not len(questions):
			raise Http404
		return questions

		

