from django.conf.urls.defaults import *
from hzqna.views import ListOpened, ListClosed, ListUserQuestions, ListUserAnswers, ViewQuestion
from hzqna.views.post import PostQuestion

opened_questions = url(
    regex=r'^opened/((?P<page>\d+)/$)|($)',
    view=ListOpened.as_view(),
    name='opened-questions'
)
closed_questions = url(
    regex=r'^closed/((?P<page>\d+)/$)|($)',
    view=ListClosed.as_view(),
    name='closed-questions'
)
tagged_opened_questions = url(
    regex=r'^tagged_o/(?P<tagname>[^/]+)/((?P<page>\d+)/$)|($)',
    view=ListOpened.as_view(),
    name='tagged-opened-questions'
)
tagged_closed_questions = url(
    regex=r'^tagged_c/(?P<tagname>[^/]+)/((?P<page>\d+)/$)|($)',
    view=ListClosed.as_view(),
    name='tagged-closed-questions'
)
questions_of_user = url(
    regex=r'^user_q/(?P<userid>\d+)/((?P<page>\d+)/$)|($)',
    view=ListUserQuestions.as_view(),
    name='questions-of-user'
)
answers_of_user = url(
    regex=r'^user_a/(?P<userid>\d)/((?P<page>\d+)/$)|($)',
    view=ListUserAnswers.as_view(),
    name='answers-of-user'
)
view_question = url(
    regex=r'^show/(?P<pk>\d+)/$',
    view=ViewQuestion.as_view(),
    name='view-question'
)
post_question = url(
	regex=r'^post/$',
	view=PostQuestion.as_view(),
	name='post-question'
)
#post_answer = url(
#	regex=r'^post/(?P<question_id>\d+)/$',
#	view=PostAnswer.as_view(),
#	name='post-answer'
#)
#best_answer = url(
#	regex=r'^best/(?P<answer_id>\d+)/$',
#	view=BestAnswer.as_view(),
#	name='best-answer'
#)
#edit_question = url(
#	regex=r'^edit/q/(?P<question_id>\d+)/$',
#	view=EditQuestion.as_view(),
#	name='edit-question'
#)
#edit_answer = url(
#	regex=r'^edit/a/(?P<answer_id>\d+)/$',
#	view=EditAnswer.as_view(),
#	name='edit-answer'
#)
#close_question = url(
#	regex=r'^close/(?P<question_id>\d+)/$',
#	view=CloseQuestion.as_view(),
#	name='close-question'
#)


urlpatterns = patterns('', opened_questions, closed_questions, tagged_opened_questions,
                       tagged_closed_questions, questions_of_user, answers_of_user, view_question,
					   post_question
                       )
                      
