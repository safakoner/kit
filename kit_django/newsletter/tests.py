#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from django.test    import TestCase

from core.tests     import getOrCreateContextAndLanguageObjects
from newsletter     import models


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
NEWSLETTER = [
            {
                'is_active'         : True,
                'note'              : "",
                'context'           : 'djangokit',
                'language'          : 'en-us',
                'code'              : "",
                'name'              : 'Jules Verne',
                'email'             : 'jverne@thousandleagues.com'
            },
            {
                'is_active'         : True,
                'note'              : "",
                'context'           : 'djangokit',
                'language'          : 'en-us',
                'code'              : "",
                'name'              : 'Alexandre Dumas',
                'email'             : 'a.dumas@cristo.com'
            }
        ]

class NewsletterTest(TestCase):

    def setUp(self):

        context, language = getOrCreateContextAndLanguageObjects()

        for data in NEWSLETTER:

            if 'context' in data:
                data['context']  = context

            if 'language' in data:
                data['language'] = language

            models.Newsletter.objects.create(**data)

    def test_newsletter(self):

        modelInstance = models.Newsletter.objects.get(name=NEWSLETTER[0]['name'])
        self.assertEqual(modelInstance.email, 'jverne@thousandleagues.com')


