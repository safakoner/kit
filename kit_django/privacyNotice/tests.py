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
from privacyNotice  import models




#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
PRIVACY_NOTICE = [
    {
        'is_active'         : True,
        'note'              : "",
        'context'           : 'djangokit',
        'language'          : 'en-us',
        'code'              : "",
        'order'             : 1,
        'primary_title'     : 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.',
        'secondary_title'   : 'Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.',
        'body'              : 'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using, making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).'
    },
    {
        'is_active'         : True,
        'note'              : "",
        'context'           : 'djangokit',
        'language'          : 'en-us',
        'code'              : "",
        'order'             : 2,
        'primary_title'     : 'It is a long established fact that a reader will be distracted by the readable.',
        'secondary_title'   : 'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium.',
        'body'              : 'Content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using, content here, making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).'
    }

]

class PrivacyNoticeTest(TestCase):

    def setUp(self):

        context, language = getOrCreateContextAndLanguageObjects()

        for data in PRIVACY_NOTICE:

            if 'context' in data:
                data['context']  = context

            if 'language' in data:
                data['language'] = language

            models.PrivacyNotice.objects.create(**data)

    def test_privacyNotice(self):

        modelInstance = models.PrivacyNotice.objects.get(order=PRIVACY_NOTICE[0]['order'])
        self.assertEqual(modelInstance.primary_title, 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.')

