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
from projectSettings    import models


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
PROJECT_SETTINGS = [
                    {
                        'is_active'         : True,
                        'note'              : "",
                        'context'           : None,
                        'language'          : 'en-us',
                        'code'              : "",
                        'key'               : 'isWebSiteEnabled',
                        'value'             : '1'
                    },
                    {
                        'is_active'         : True,
                        'note'              : "",
                        'context'           : None,
                        'language'          : 'en-us',
                        'code'              : "",
                        'key'               : 'isRESTAPIEnabled',
                        'value'             : '1'
                    }
                ]

class ProjectSettingsTest(TestCase):

    def setUp(self):

        context, language = getOrCreateContextAndLanguageObjects()

        for data in PROJECT_SETTINGS:

            if 'context' in data:
                data['context']  = context

            if 'language' in data:
                data['language'] = language

            models.ProjectSettings.objects.create(**data)

    def test_projectSettings(self):

        modelInstance = models.ProjectSettings.objects.get(key=PROJECT_SETTINGS[0]['key'])
        self.assertEqual(modelInstance.value, '1')

