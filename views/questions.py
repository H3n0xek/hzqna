from django.views.generic.list import ListView
from django.core.paginator import Paginator
from hzqna.models import Question
from hzqna.settings import QUESTIONS_PER_PAGE

class ListOpened(ListView):
    template_name = "qna/list_opened.html"
    
    def get_queryset(self):
        page = self.kwargs.get('page', 1)
        objects = Question.opened.all()
        paginator = Paginator(objects, QUESTIONS_PER_PAGE)


            
        
    
