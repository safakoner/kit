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
from content        import models


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
CONTENT_TYPES = [
                {
                    'is_active'         : True,
                    'note'              : '',
                    'context'           : 'djangokit',
                    'language'          : 'en-us',
                    'code'              : 'benefits',
                    'icon'              : 'fas fa-trophy',
                    'label'             : 'Benefits'
                },
                {
                    'is_active'         : True,
                    'note'              : '',
                    'context'           : 'djangokit',
                    'language'          : 'en-us',
                    'code'              : 'features',
                    'icon'              : 'fas fa-check',
                    'label'             : 'Features'
                },
                {
                    'is_active'         : True,
                    'note'              : '',
                    'context'           : 'djangokit',
                    'language'          : 'en-us',
                    'code'              : 'primaryHeader',
                    'label'             : 'Primary Header'
                },
                {
                    'is_active'         : True,
                    'note'              : '',
                    'context'           : 'djangokit',
                    'language'          : 'en-us',
                    'code'              : 'secondaryHeader',
                    'label'             : 'Secondary Header'
                },
                {
                    'is_active'         : True,
                    'note'              : '',
                    'context'           : 'djangokit',
                    'language'          : 'en-us',
                    'code'              : 'resources',
                    'icon'              : 'fas fa-list',
                    'label'             : 'Resources'
                }
                ]

CONTENTS = [
            {
                'is_active'         : True,
                'note'              : '',
                'context'           : 'djangokit',
                'language'          : 'en-us',
                'code'              : 'primaryHeader',
                'content_type'      : 'primaryHeader',
                'order'             : 1,
                'icon'              : None,
                'image'             : None,
                'title'             : '',
                'body'              : 'Django makes it easier to build better web apps more quickly and with less code. Django Kit takes it one step further and gives you plenty of built-in functionalities.'
            },
            {
                'is_active'         : True,
                'note'              : '',
                'context'           : 'djangokit',
                'language'          : 'en-us',
                'code'              : 'secondaryHeader',
                'content_type'      : 'secondaryHeader',
                'order'             : 2,
                'icon'              : None,
                'image'             : None,
                'title'             : '',
                'body'              : 'You can use built-in apps like conversion and landing page to get your web site up and running in no time. Incorporate additional apps like newsletter, FAQ, testimonials and more. Publish REST API for users and customers, which is provided for all the models in the project. Edit, customize, deploy and enjoy!'
            }
        ]


ITEMS = [
    {
        'is_active'         : True,
        'note'              : '',
        'context'           : 'djangokit',
        'language'          : 'en-us',
        'code'              : 'ridiculouslyFast',
        'content_type'      : 'benefits',
        'order'             : 1,
        'icon'              : 'fas fa-bolt fa-3x',
        'image'             : None,
        'title'             : 'Ridiculously Fast',
        'body'              : 'Django was designed to help developers take applications from concept to completion as quickly as possible.',
        'url'               : ''
    },
    {
        'is_active'         : True,
        'note'              : '',
        'context'           : 'djangokit',
        'language'          : 'en-us',
        'code'              : 'reassuringlySecure',
        'content_type'      : 'benefits',
        'order'             : 2,
        'icon'              : 'fas fa-lock fa-3x',
        'image'             : None,
        'title'             : 'Reassuringly Secure',
        'body'              : 'Django takes security seriously and helps developers avoid many common security mistakes.',
        'url'               : ''
    },
    {
        'is_active'         : True,
        'note'              : '',
        'context'           : 'djangokit',
        'language'          : 'en-us',
        'code'              : 'exceedinglyScalable',
        'content_type'      : 'benefits',
        'order'             : 3,
        'icon'              : 'fas fa-tachometer-alt fa-3x',
        'image'             : None,
        'title'             : 'Exceedingly Scalable',
        'body'              : 'Some of the busiest sites on the Web leverage Django’s ability to quickly and flexibly scale.',
        'url'               : ''
    },
    {
        'is_active'         : True,
        'note'              : '',
        'context'           : 'djangokit',
        'language'          : 'en-us',
        'code'              : 'builtinFunctionalities',
        'content_type'      : 'benefits',
        'order'             : 4,
        'icon'              : 'fas fa-magic fa-3x',
        'image'             : None,
        'title'             : 'Built-in Functionalities',
        'body'              : 'Plenty of built-in functionalities that you\'ll enjoy.',
        'url'               : ''
    },
    {
        'is_active'         : True,
        'note'              : '',
        'context'           : 'djangokit',
        'language'          : 'en-us',
        'code'              : 'builtInLandingPage',
        'content_type'      : 'features',
        'order'             : 1,
        'icon'              : 'fas fa-desktop',
        'image'             : None,
        'title'             : 'Built-in Landing Page',
        'body'              : 'Use built-in landing-page to inform visitors about the features and benefits of the products and services you offer.',
        'url'               : ''
    },
    {
        'is_active'         : True,
        'note'              : '',
        'context'           : 'djangokit',
        'language'          : 'en-us',
        'code'              : 'builtInConversionApp',
        'content_type'      : 'features',
        'order'             : 2,
        'icon'              : 'fas fa-award',
        'image'             : None,
        'title'             : 'Built-in Conversion App',
        'body'              : 'You can use built-in conversion app to stimulate interest of potential customers for the products and services you offer.',
        'url'               : ''
    },
    {
        'is_active'         : True,
        'note'              : '',
        'context'           : 'djangokit',
        'language'          : 'en-us',
        'code'              : 'responsiveWebApps',
        'content_type'      : 'features',
        'order'             : 3,
        'icon'              : 'fas fa-mobile',
        'image'             : None,
        'title'             : 'Responsive Web Apps',
        'body'              : 'All built-in web apps are designed ground up to be responsive.',
        'url'               : ''
    },
    {
        'is_active'         : True,
        'note'              : '',
        'context'           : 'djangokit',
        'language'          : 'en-us',
        'code'              : 'builtInUserAccount',
        'content_type'      : 'features',
        'order'             : 4,
        'icon'              : 'fas fa-users',
        'image'             : None,
        'title'             : 'Built-in User Account',
        'body'              : 'E-mail based user account provides much needed flexibility for membership based applications.',
        'url'               : ''
    },
    {
        'is_active'         : True,
        'note'              : '',
        'context'           : 'djangokit',
        'language'          : 'en-us',
        'code'              : 'builtInContext',
        'content_type'      : 'features',
        'order'             : 5,
        'icon'              : 'fas fa-id-card',
        'image'             : None,
        'title'             : 'Built-in Context',
        'body'              : 'You can use context app to serve multiple web sites in one Django project instance while preserving server resources.',
        'url'               : ''
    },
    {
        'is_active'         : True,
        'note'              : '',
        'context'           : 'djangokit',
        'language'          : 'en-us',
        'code'              : 'restAPICore',
        'content_type'      : 'features',
        'order'             : 6,
        'icon'              : 'fas fa-code',
        'image'             : None,
        'title'             : 'REST API Core',
        'body'              : 'Kit offers core functionalities for REST API implementation.',
        'url'               : ''
    },
    {
        'is_active'         : True,
        'note'              : '',
        'context'           : 'djangokit',
        'language'          : 'en-us',
        'code'              : 'builtInRESTAPI',
        'content_type'      : 'features',
        'order'             : 7,
        'icon'              : 'fas fa-plug',
        'image'             : None,
        'title'             : 'Built-in REST API',
        'body'              : 'Publish built-in REST API, which is available for all the models, to allow your users and customers to interact with their data.',
        'url'               : ''
    },
    {
        'is_active'         : True,
        'note'              : '',
        'context'           : 'djangokit',
        'language'          : 'en-us',
        'code'              : 'builtInSimpleAPIAccount',
        'content_type'      : 'features',
        'order'             : 8,
        'icon'              : 'fas fa-link',
        'image'             : None,
        'title'             : 'Simple API Account',
        'body'              : 'You can provide simple API account without creating user accounts, super convenient when you want to offer free services.',
        'url'               : ''
    },
    {
        'is_active'         : True,
        'note'              : '',
        'context'           : 'djangokit',
        'language'          : 'en-us',
        'code'              : 'builtInCaptcha',
        'content_type'      : 'features',
        'order'             : 9,
        'icon'              : 'fas fa-qrcode',
        'image'             : None,
        'title'             : 'Built-in CAPTCHA',
        'body'              : 'Every form in the kit is protected by built-in captcha, so say goodbye to automated spams!',
        'url'               : ''
    },
    {
        'is_active'         : True,
        'note'              : '',
        'context'           : 'djangokit',
        'language'          : 'en-us',
        'code'              : 'builtInForms',
        'content_type'      : 'features',
        'order'             : 10,
        'icon'              : 'fas fa-bars',
        'image'             : None,
        'title'             : 'Built-in Forms',
        'body'              : 'You can utilize built-in forms such as contact, newsletter, etc.',
        'url'               : ''
    },
    {
        'is_active'         : True,
        'note'              : '',
        'context'           : 'djangokit',
        'language'          : 'en-us',
        'code'              : 'contactsAreStored',
        'content_type'      : 'features',
        'order'             : 11,
        'icon'              : 'fas fa-envelope',
        'image'             : None,
        'title'             : 'Contacts are Stored',
        'body'              : 'Contact form stores the information besides sending you an e-mail about any request you receive.',
        'url'               : ''
    },
    {
        'is_active'         : True,
        'note'              : '',
        'context'           : 'djangokit',
        'language'          : 'en-us',
        'code'              : 'builtInModels',
        'content_type'      : 'features',
        'order'             : 12,
        'icon'              : 'fas fa-database',
        'image'             : None,
        'title'             : 'Built-in Models',
        'body'              : 'You can utilize plenty of built-in models in your custom apps based on your needs.',
        'url'               : ''
    },
    {
        'is_active'         : True,
        'note'              : '',
        'context'           : 'djangokit',
        'language'          : 'en-us',
        'code'              : 'builtInContactApp',
        'content_type'      : 'features',
        'order'             : 13,
        'icon'              : 'fas fa-envelope-open',
        'image'             : None,
        'title'             : 'Built-in Contact App',
        'body'              : 'Use the app to provide a contact form for your web site. Additionally you can incorporate Address, Email, Phone and Social Media models.',
        'url'               : ''
    },
    {
        'is_active'         : True,
        'note'              : '',
        'context'           : 'djangokit',
        'language'          : 'en-us',
        'code'              : 'builtInErrorPages',
        'content_type'      : 'features',
        'order'             : 14,
        'icon'              : 'fas fa-exclamation-triangle',
        'image'             : None,
        'title'             : 'Built-in Error Pages',
        'body'              : 'Kit provides built-in error pages, like 400, 403, 404, etc., which of course you can customize.',
        'url'               : ''
    },
    {
        'is_active'         : True,
        'note'              : '',
        'context'           : 'djangokit',
        'language'          : 'en-us',
        'code'              : 'builtInFAQ',
        'content_type'      : 'features',
        'order'             : 15,
        'icon'              : 'fas fa-question',
        'image'             : None,
        'title'             : 'Built-in FAQ App',
        'body'              : 'Use the app to add FAQ section to your web site.',
        'url'               : ''
    },
    {
        'is_active'         : True,
        'note'              : '',
        'context'           : 'djangokit',
        'language'          : 'en-us',
        'code'              : 'builtInNewsletter',
        'content_type'      : 'features',
        'order'             : 16,
        'icon'              : 'fas fa-mail-bulk',
        'image'             : None,
        'title'             : 'Built-in Newsletter App',
        'body'              : 'Use the app to keep track of and inform your audience.',
        'url'               : ''
    },
    {
        'is_active'         : True,
        'note'              : '',
        'context'           : 'djangokit',
        'language'          : 'en-us',
        'code'              : 'builtInPrivacyNotice',
        'content_type'      : 'features',
        'order'             : 17,
        'icon'              : 'fas fa-user-shield',
        'image'             : None,
        'title'             : 'Built-in Privacy Notice App',
        'body'              : 'Use the app to provide privacy notice to visitors.',
        'url'               : ''
    },
    {
        'is_active'         : True,
        'note'              : '',
        'context'           : 'djangokit',
        'language'          : 'en-us',
        'code'              : 'builtInTermsOfUse',
        'content_type'      : 'features',
        'order'             : 18,
        'icon'              : 'fas fa-handshake',
        'image'             : None,
        'title'             : 'Built-in Terms of Use App',
        'body'              : 'Use the app to inform visitors about terms of use.',
        'url'               : ''
    },
    {
        'is_active'         : True,
        'note'              : '',
        'context'           : 'djangokit',
        'language'          : 'en-us',
        'code'              : 'builtInTestimonial',
        'content_type'      : 'features',
        'order'             : 19,
        'icon'              : 'fas fa-quote-right',
        'image'             : None,
        'title'             : 'Built-in Testimonial App',
        'body'              : 'Use the app to provide testimonials.',
        'url'               : ''
    },
    {
        'is_active'         : True,
        'note'              : '',
        'context'           : 'djangokit',
        'language'          : 'en-us',
        'code'              : 'builtInVisitorCount',
        'content_type'      : 'features',
        'order'             : 20,
        'icon'              : 'fas fa-stopwatch-20',
        'image'             : None,
        'title'             : 'Built-in Visitor Count App',
        'body'              : 'Keep track of visitor count for each URL that your application provides.',
        'url'               : ''
    }

]


class ContentTest(TestCase):

    def setUp(self):

        context, language = getOrCreateContextAndLanguageObjects()

        DATA = []
        DATA.extend(CONTENT_TYPES)
        DATA.extend(CONTENTS)
        DATA.extend(ITEMS)

        for data in DATA:

            if 'context' in data:
                data['context']  = context

            if 'language' in data:
                data['language'] = language

        for data in CONTENT_TYPES:
            models.ContentType.objects.create(**data)

        for data in CONTENTS:

            if 'content_type' in data and isinstance(data['content_type'], str):
                data['content_type'] = models.ContentType.objects.get(code=data['content_type'])

            models.Content.objects.create(**data)

        for data in ITEMS:

            if 'content_type' in data and isinstance(data['content_type'], str):
                data['content_type'] = models.ContentType.objects.get(code=data['content_type'])

            models.Item.objects.create(**data)

    def test_contentType(self):

        modelInstance = models.ContentType.objects.get(code=CONTENT_TYPES[0]['code'])
        self.assertEqual(modelInstance.label, 'Benefits')

    def test_content(self):

        modelInstance = models.Content.objects.get(code=CONTENTS[0]['code'])
        self.assertEqual(modelInstance.body, 'Django makes it easier to build better web apps more quickly and with less code. Django Kit takes it one step further and gives you plenty of built-in functionalities.')

    def test_item(self):

        modelInstance = models.Item.objects.get(code=ITEMS[9]['code'])
        self.assertEqual(modelInstance.title, 'REST API Core')

        modelInstance = models.Item.objects.get(code=ITEMS[10]['code'])
        self.assertEqual(modelInstance.title, 'Built-in REST API')
        self.assertEqual(modelInstance.order, 7)

        count = models.Item.objects.filter(content_type__code__exact='features').count()
        self.assertEqual(count, 20)
