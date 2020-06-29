#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from django.test    import TestCase

from language       import models


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
LANGUAGE = [
    {
        'code'  : 'en-us',
        'label' : 'English'
    },
    {
        'code'  : 'es',
        'label' : 'Spanish'
    }

]

class LanguageTest(TestCase):

    def setUp(self):

        for data in LANGUAGE:

            models.Language.objects.create(**data)

    def test_language(self):

        modelInstance = models.Language.objects.get(label=LANGUAGE[0]['label'])
        self.assertEqual(modelInstance.code, LANGUAGE[0]['code'])


