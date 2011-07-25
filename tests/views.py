from django.test import TestCase
from django.test.client import Client


class ListAuthQuestionsTest(TestCase):
	fixtures = [ 'question_list.json', ]
	urls = 'hzqna.test_urls'
		
	def setUp(self):
		self.c = Client()
		self.assertTrue(self.c.login(username='developer', password='developer'))
	
	def testListStatusCode(self):
		result = self.c.get('/opened/')
		self.assertEqual(result.status_code, 200)
	
	def testListCountQuestions(self):
		result = self.c.get('/opened/')
		self.assertFalse(len(self.context.get('question_list', [])), 0)
	
	def testListPage1(self):
		result = self.c.get('/opened/1/')
		self.assertEqual(result.status_code, 200)
	
	def testListPage2(self):
		result = self.c.get('/opened/2/')
		self.assertEqual(result.status_code, 200)
	
	def testTemplating(self):
		result = self.c.get('/opened/1/')
		self.assertContains(result, 'Question one')

		
		
class ListQuestionsTest(TestCase):
	fixtures = [ 'question_list.json', ]
	urls = 'hzqna.test_urls'
	
	def setUp(self):
		self.c = Client()		
		
	def testListStatusCode(self):
		result = self.c.get('/opened/')
		self.assertEqual(result.status_code, 200)
	
	def testListCountQuestions(self):
		result = self.c.get('/opened/')
		self.assertFalse(len(self.context.get('question_list', [])), 0)
	
	def testListPage1(self):
		result = self.c.get('/opened/1/')
		self.assertEqual(result.status_code, 200)
	
	def testListPage2(self):
		result = self.c.get('/opened/2/')
		self.assertEqual(result.status_code, 200)
	
	def testTemplating(self):
		result = self.c.get('/opened/1/')
		self.assertContains(result, 'Question one')