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
from contact        import models




#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------

ADDRESS = {
                'is_active'         : True,
                'note'              : '',
                'context'           : 'djangokit',
                'language'          : 'en-us',
                'code'              : 'headquarter',
                'icon'              : 'fas fa-map-marker-alt',
                'label'             : 'Headquarter',
                'address_line_1'    : '400 319 W Hastings St.',
                'address_line_2'    : '',
                'postal_code'       : 'V6B 1H6',
                'city'              : 'Vancouver',
                'state'             : 'BC',
                'country'           : 'Canada',
                'url'               : 'https://www.google.com/maps/place/319+W+Hastings+St,+Vancouver,+BC+V6B+1H6/data=!4m2!3m1!1s0x54867179af0a5e81:0xc32666c533a3a55c?sa=X&ved=2ahUKEwjZj7b_45HqAhWxHTQIHf9vCqoQ8gEwAHoECAsQAQ'
          }

CONTACT = {
                'is_active'         : True,
                'note'              : '',
                'context'           : 'djangokit',
                'language'          : 'en-us',
                'code'              : '',
                'is_processed'      : False,
                'name'              : 'Alexandre Dumas',
                'company'           : 'Monte Cristo',
                'email'             : 'a.dumas@cristo.com',
                'subject'           : 'Licensing',
                'message'           : 'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using, making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).'
          }

EMAIL = {
                'is_active' : True,
                'note'      : '',
                'context'   : 'djangokit',
                'language'  : 'en-us',
                'code'      : 'sales',
                'icon'      : 'fas fa-credit-card',
                'label'     : 'Sales',
                'email'     : 'sales@domain.com',
                'url'       : ''
        }

PHONE = {
                'is_active'     : True,
                'note'          : '',
                'context'       : 'djangokit',
                'language'      : 'en-us',
                'code'          : 'headquarter',
                'icon'          : 'fas fa-landmark',
                'label'         : 'Headquarter',
                'country_code'  : '+1',
                'area_code'     : '604',
                'phone_number'  : '111 2233'
        }

SOCIAL_MEDIA = {
                'is_active'     : True,
                'note'          : '',
                'context'       : 'djangokit',
                'language'      : 'en-us',
                'code'          : 'twitter',
                'icon'          : 'fab fa-twitter',
                'label'         : 'Twitter',
                'url'           : 'https://twitter.com/safakoner'
               }

class ContactTest(TestCase):

    def setUp(self):

        context, language   = getOrCreateContextAndLanguageObjects()

        for data in [ADDRESS, CONTACT, EMAIL, PHONE, SOCIAL_MEDIA]:

            if 'context' in data:
                data['context']  = context

            if 'language' in data:
                data['language'] = language

        models.Address.objects.create(**ADDRESS)
        models.Contact.objects.create(**CONTACT)
        models.Email.objects.create(**EMAIL)
        models.Phone.objects.create(**PHONE)
        models.SocialMedia.objects.create(**SOCIAL_MEDIA)

    def test_address(self):

        modelInstance = models.Address.objects.get(address_line_1=ADDRESS['address_line_1'])
        self.assertEqual(modelInstance.address_line_1, '400 319 W Hastings St.')

    def test_contact(self):

        modelInstance = models.Contact.objects.get(name=CONTACT['name'], is_processed=False)
        self.assertEqual(modelInstance.company, 'Monte Cristo')

    def test_email(self):

        modelInstance = models.Email.objects.get(code='sales')
        self.assertEqual(modelInstance.email, 'sales@domain.com')

    def test_phone(self):

        modelInstance = models.Phone.objects.get(code='headquarter')
        self.assertEqual(modelInstance.phone_number, '111 2233')

    def test_socialMedia(self):

        modelInstance = models.SocialMedia.objects.get(code='twitter')
        self.assertEqual(modelInstance.url, 'https://twitter.com/safakoner')




