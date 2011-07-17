from django.db.models import Manager

class OpenQuestionsManager(Manager):
    def get_query_set(self):
        return super(OpenQuestionsManager, self).get_query_set().filter(is_closed=False)

class ClosedQuestionsManager(Manager):
    def get_query_set(self):
        return super(ClosedQuestionsManager, self).get_query_set().filter(is_closed=True)

             
