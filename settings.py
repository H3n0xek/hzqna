from django.conf import settings

QUESTIONS_PER_PAGE = getattr(settings, 'QUESTIONS_PER_PAGE', 25)

