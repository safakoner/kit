#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from django.test        import TestCase

from core.tests         import getOrCreateContextAndLanguageObjects
from simpleAPIAccount   import models


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
SIMPLE_API_ACCOUNT = [
                    {
                        'is_active'         : True,
                        'note'              : "",
                        'context'           : 'djangokit',
                        'language'          : 'en-us',
                        'code'              : "wildcardAPIAccess",
                        'label'             : 'Wildcard API Access',
                        'email'             : "",
                        'expiration_date'   : None
                    }
                ]

class SimpleAPIAccountTest(TestCase):

    def setUp(self):

        context, language = getOrCreateContextAndLanguageObjects()

        for data in SIMPLE_API_ACCOUNT:

            if 'context' in data:
                data['context']  = context

            if 'language' in data:
                data['language'] = language

            models.SimpleAPIAccount.objects.create(**data)

    def test_simpleAPIAccount(self):

        modelInstance = models.SimpleAPIAccount.objects.get(code=SIMPLE_API_ACCOUNT[0]['code'])
        self.assertEqual(modelInstance.label, SIMPLE_API_ACCOUNT[0]['label'])
        self.assertEqual(modelInstance.expiration_date, SIMPLE_API_ACCOUNT[0]['expiration_date'])

