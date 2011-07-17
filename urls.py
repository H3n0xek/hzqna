from django.conf.urls.defaults import *


opened_questions = url(
    regex=r'^opened/(?P<page>\d+)/$',
    view='hzengine.views.list_opened',
    name='opened-questions'
)
closed_questions = url(
    regex=r'^closed/(?P<page>\d+)/$',
    view='hzengine.views.list_closed',
    name='closed-questions'
)
tagged_opened_questions = url(
    regex=r'^tagged_o/(?P<tagname>[^/]+)/(?P<page>\d+)/$',
    view='hzengine.views.list_opened',
    name='tagged-opened-questions'
)
tagged_closed_questions = url(
    regex=r'^tagged_c/(?P<tagname>[^/]+)/(?P<page>\d+)/$',
    view='hzengine.views.list_opened',
    name='tagged-closed-questions'
)
questions_of_user = url(
    regex=r'^user_q/(?P<userid>\d+)/(?P<page>\d+)/$',
    view='hzengine.views.list_user_questions',
    name='questions-of-user'
)
answers_of_user = url(
    regex=r'^user_a/(?P<userid>\d)/(?P<page>\d+)/$',
    view='hzengine.views.list_user_answers',
    name='answers-of-user'
)



urlpatterns = patterns('', opened_questions, closed_questions, tagged_opened_questions,
                       tagged_closed_questions, questions_of_user, answers_of_user
                       )
                      
