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
from faq            import models


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
FAQ = [
    {
        'is_active'         : True,
        'note'              : '',
        'context'           : 'djangokit',
        'language'          : 'en-us',
        'code'              : "",
        'order'             : 1,
        'question'          : 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.',
        'answer'            : 'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using, making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).',
        'keywords'          : 'some keywords go here'
    },
    {
        'is_active'         : True,
        'note'              : '',
        'context'           : 'djangokit',
        'language'          : 'en-us',
        'code'              : "",
        'order'             : 2,
        'question'          : 'There are many variations of passages of Lorem Ipsum available, but the majority.',
        'answer'            : 'he standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from de Finibus Bonorum et Malorum by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham',
        'keywords'          : 'other keywords go here as well'
    }

]

class FAQTest(TestCase):

    def setUp(self):

        context, language   = getOrCreateContextAndLanguageObjects()

        for data in FAQ:

            if 'context' in data:
                data['context']  = context

            if 'language' in data:
                data['language'] = language

            models.FAQ.objects.create(**data)

    def test_faq(self):

        modelInstance = models.FAQ.objects.get(order=FAQ[0]['order'])
        self.assertEqual(modelInstance.keywords, 'some keywords go here')


