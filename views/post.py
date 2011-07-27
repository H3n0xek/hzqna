from django.views.generic.edit import CreateView
from hzqna.forms import PostQuestionForm

class PostQuestion(CreateView):	
	form_class = PostQuestionForm
	
	def get_form_kwargs(self, **kwargs):
		kargs = super(PostQuestion, self).get_form_kwargs(**kwargs)
		kargs['initial']['author'] = self.request.user
		return kargs

	def get_success_url(self):
		# TODO: use django.messages here
		return super(PostQuestion, self).get_success_url()
	
