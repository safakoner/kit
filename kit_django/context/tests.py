#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from django.test    import TestCase

from context        import models


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
CONTEXTS = [
            {
                'is_active'     : True,
                'note'          : "",
                'icon'          : 'fab fa-python',
                'code'          : 'dk',
                'label'         : 'Django Kit',
                'domain'        : 'djangokit',
                'description'   : 'Django Kit - Django Project',
                'image'         : None
            }
            ]

class ContextTest(TestCase):

    def setUp(self):

        models.Context.objects.create(**CONTEXTS[0])

    def test_context(self):

        modelInstance = models.Context.objects.get(code=CONTEXTS[0]['code'])
        self.assertEqual(modelInstance.domain, 'djangokit')
        self.assertEqual(modelInstance.is_active, True)
