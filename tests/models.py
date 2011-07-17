from django.utils import unittest
from django.test.client import Client
from hzqna.models import Question, Answer
from django.contrib.auth.models import User

class QuestionSimpleTestCase(unittest.TestCase):
    #fixtures = ['question_simple.json']

    def setUp():
        pass

    def testQuestionCreate():
        u = User.objects.get(pk=1)
        q = Question.objects.create(author=u, title='Test question', text='Blablabla')
        self.assertTrue(Question.opened.get(title='Test question'))

    def testQuestionRemove():
        self.testQuestionCreate()
        q = Question.opened.get(title='Test question')
        q.delete()

    def testQuestionClose():
        self.testQuestionCreate()
        q = Question.opened.get(title='Test question')
        q.is_closed = True
        q.save()
        self.assertTrue(Question.closed.get(title='Test question'))



class AnswerSimpleTestCase(unittest.TestCase):
    #fixtures = [ 'question_simple.json', ]
    
    def setUp():
        Question.objects.create(author=User.objects.get(pk=1), title='Test question', text='Blabla')
    
    def testAnswerTheQuestion():
        q = Question.objects.get(title='Test question')
        a = Answer.objects.create(author=User.objects.get(pk=1),
                                  question=q, text='This is test answer')
    
    

