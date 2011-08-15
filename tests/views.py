from django.test import TestCase
from django.test.client import Client
from hzqna.models import Question, Answer

class ListAuthQuestionsTest(TestCase):
    fixtures = [ 'auth.json', 'question_list.json', ]
    urls = 'hzqna.test_urls'
		
    def setUp(self):
        self.c = Client()
        self.assertTrue(self.c.login(username='developer', password='developer'))
	
    def testListStatusCode(self):
        result = self.c.get('/opened/')
        self.assertEqual(result.status_code, 200)
	
    def testListCountQuestions(self):
        result = self.c.get('/opened/')
	self.assertFalse(len(result.context.get('question_list', []).object_list) == 0)
	
    def testListPage1(self):
        result = self.c.get('/opened/1/')
        self.assertEqual(result.status_code, 200)
	
    def testListPage2(self):
        result = self.c.get('/opened/2/')
        self.assertEqual(result.status_code, 200)
	
		
class ListQuestionsTest(TestCase):
    fixtures = [ 'auth.json', 'question_list.json', ]
    urls = 'hzqna.test_urls'
	
    def setUp(self):
        self.c = Client()		
		
    def testListStatusCode(self):
        result = self.c.get('/opened/')
        self.assertEqual(result.status_code, 200)
	
    def testListCountQuestions(self):
        result = self.c.get('/opened/')
        self.assertFalse(len(result.context.get('question_list', []).object_list) == 0)
	
    def testListPage1(self):
        result = self.c.get('/opened/1/')
        self.assertEqual(result.status_code, 200)
	
    def testListPage2(self):
        result = self.c.get('/opened/2/')
        self.assertEqual(result.status_code, 200)
	
		
class ChangeQuestionOrAnswer(TestCase):
	fixtures = [ 'auth.json', ]
	urls = 'hzqna.test_urls'
	
	def setUp(self):
		self.c = Client()
		self.assertTrue(self.c.login(username='developer', password='developer'), 'login invalid')
		Question.objects.create(author=1, title='Initial test question',
				text='This is initial test question')
	
	def testQuestionPost_get(self):
		self.assertEqual(self.c.get('/post/').status_code, 200)
	
	def testQuestionPost_post(self):
		self.assertEqual(self.c.post('/post/', { 'title': 'Test Question', 'text': 'This is test question' }
			).status_code, 302)
		self.assertEqual(self.c.get('/opened/2/').status_code, 200)
			
	def testPostAnswer(self):
		self.assertEqual(self.c.post('/post/1/', { 'text': 'This is first answer' }).status_code, 302)		
		self.assertTrue(len(Answer.objects.filter(question=1)) > 0, 'no answers')
	
	def testCloseQuestion(self):
		self.assertEqual(self.c.post('/close/1/').status_code, 302)
		self.assertTrue(Question.objects.get(pk=1).is_closed, 'question is still closed')
	
	def testEditQuestion(self):
		self.assertEqual(self.c.post('/edit/q/1/', { 'text': 'Modified question' }).status_code, 202)
		self.assertEqual(Question.objects.get(pk=1).text, 'Modified question', 'Question didn\'t changed')
	
	def testEditAnswer(self):
		Answer.objects.create(author=1, question=1, text='Original answer')
		self.assertEqual(self.c.post('/edit/a/1/', { 'text': 'Modified answer' }).status_code, 202)
	
	def testBestAnswer(self):
		Answer.objects.create(author=1, question=1, text='This is best answer')
		Answer.objects.create(author=1, question=1, text='Bad answer')
		self.assertEqual(self.c.post('/best/1/', {}).status_code, 202)
		self.assertTrue(Answer.objects.get(pk=1).is_best, 'Answer isn\'t a best')
		self.assertTrue(Question.objects.get(pk=1).is_closed, 'Question isn\'t closed')
	
