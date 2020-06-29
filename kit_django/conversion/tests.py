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
from conversion     import models


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
CONVERSION = [
            {
                'is_active'         : True,
                'note'              : "",
                'context'           : None,
                'language'          : 'en-us',
                'code'              : 'firstConversion',
                'label'             : 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.',
                'background_image'  : None,
                'primary_title'     : '# Lorem Ipsum is simply dummy text of the printing and typesetting industry.',
                'secondary_title'   : '## Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.',
                'body'              : 'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using content here, making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).',
                'success_page_body' : 'Thank you for joining. It\'s good to have you!\\nYou\'ll be receiving updates.'
            }
        ]

class ConversionTest(TestCase):

    def setUp(self):

        context, language = getOrCreateContextAndLanguageObjects()

        for data in CONVERSION:

            # if 'context' in data:
            #     data['context']  = context

            if 'language' in data:
                data['language'] = language

            models.Conversion.objects.create(**data)

    def test_conversion(self):

        modelInstance = models.Conversion.objects.get(code=CONVERSION[0]['code'])
        self.assertEqual(modelInstance.label, CONVERSION[0]['label'])
        self.assertEqual(modelInstance.context, None)
