#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from django.db                  import models

from context.models             import Context
from core.models                import Model
from projectSettings.common     import LANGUAGE_CODE
from language.models            import Language


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ DJANGO MODEL CLASS ] - Django model class.
class Address(Model):
    #
    # ------------------------------------------------------------------------------------------------
    # CLASSES
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief [ DJANGO MODEL META CLASS ] - Meta class of django.db.models.Model class.
    class Meta:

        ## [ str ] - Verbose name of the model class.
        verbose_name        = 'Address'

        ## [ str ] - Verbose plural name of the model class.
        verbose_name_plural = 'Address'

        ## [ tuple ] - Ordering of the model class.
        ordering            = ('label',)

    #
    # ------------------------------------------------------------------------------------------------
    # FIELDS
    # ------------------------------------------------------------------------------------------------
    ## [ django.db.models.CharField ] - Icon.
    icon                    = models.CharField(max_length=200, blank=True, null=True,
                                               help_text='Font Awesome icon with "i" tag')

    ## [ django.db.models.CharField ] - Label.
    label                   = models.CharField(max_length=200, blank=True, null=True,
                                               help_text='Label')

    ## [ django.db.models.CharField ] - Address line 1.
    address_line_1          = models.CharField(max_length=500,
                                               help_text='Unit number, street number, street name')

    ## [ django.db.models.CharField ] - Address line 2.
    address_line_2          = models.CharField(max_length=500, blank=True, null=True,
                                               help_text='District, etc.')

    ## [ django.db.models.CharField ] - Postal code.
    postal_code             = models.CharField(max_length=20, blank=True, null=True,
                                               help_text='Postal code')

    ## [ django.db.models.CharField ] - City.
    city                    = models.CharField(max_length=200,
                                               help_text='City')

    ## [ django.db.models.CharField ] - State.
    state                   = models.CharField(max_length=200, blank=True, null=True,
                                               help_text='State, province')

    ## [ django.db.models.CharField ] - Country.
    country                 = models.CharField(max_length=200,
                                               help_text='Country')

    ## [ django.db.models.URLField ] - URL.
    url                     = models.URLField(help_text='URL', blank=True, null=True)

    #
    # ------------------------------------------------------------------------------------------------
    # BUILT-IN METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief String representation.
    #
    #  @exception N/A
    #
    #  @return str - String representation.
    def __str__(self):

        return Model.__dict__['_str'](self, '{}{}'.format('{} - '.format(self.label) if self.label else '',
                                                          self.address))

    #
    # ------------------------------------------------------------------------------------------------
    # PROPERTY METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Get one line address.
    #
    #  @exception N/A
    #
    #  @return str - Address.
    @property
    def address(self):

        address = self.address_line_1

        if self.address_line_2:
            address = '{} {}'.format(address,
                                     self.address_line_2)

        address = '{} {},'.format(address,
                                 self.city)

        if self.state:
            address = '{} {}'.format(address,
                                     self.state)

        if self.postal_code:
            address = '{} {}'.format(address,
                                     self.postal_code)

        address = '{}, {}'.format(address,
                                  self.country)

        return address

#
#
#
## @brief [ DJANGO MODEL CLASS ] - Django model class.
class Contact(Model):
    #
    # ------------------------------------------------------------------------------------------------
    # CLASSES
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief [ DJANGO MODEL META CLASS ] - Meta class of django.db.models.Model class.
    class Meta:

        ## [ str ] - Verbose name of the model class.
        verbose_name        = 'Contact'

        ## [ str ] - Verbose plural name of the model class.
        verbose_name_plural = 'Contact'

        ## [ tuple ] - Ordering of the model class.
        ordering            = ('date_time',)

    #
    # ------------------------------------------------------------------------------------------------
    # FIELDS
    # ------------------------------------------------------------------------------------------------
    ## [ django.db.models.BooleanField ] - Whether this contact is processed.
    is_processed            = models.BooleanField(default=False,
                                                  help_text='Whether this contact has been processed')

    ## [ django.db.models.DateTimeField ] - Date and time.
    date_time               = models.DateTimeField(auto_now_add=True,
                                                   help_text='Date of contact')

    ## [ django.db.models.CharField ] - Name.
    name                    = models.CharField(max_length=200,
                                               help_text='First and last name')

    ## [ django.db.models.CharField ] -Company.
    company                 = models.CharField(max_length=200, blank=True,
                                               help_text='Company name')

    ## [ django.db.models.EmailField ] - Email.
    email                   = models.EmailField(max_length=200,
                                                help_text='Email address')

    ## [ django.db.models.CharField ] - Subject.
    subject                 = models.CharField(max_length=200,
                                               help_text='Subject')

    ## [ django.db.models.TextField ] - Message.
    message                 = models.TextField(blank=False,
                                               help_text='Message')

    #
    # ------------------------------------------------------------------------------------------------
    # BUILT-IN METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief String representation.
    #
    #  @exception N/A
    #
    #  @return str - String representation.
    def __str__(self):

        return Model.__dict__['_str'](self,
                                      '{} - {} {} - {} - {}{}'.format(self.date_time.strftime('%Y/%m/%d - %H:%M'),
                                                                      self.name,
                                                                      ' - {}'.format(self.company) if self.company else '',
                                                                      self.email,
                                                                      self.subject,
                                                                      '' if self.is_processed else ' - PENDING'))

    #
    # ------------------------------------------------------------------------------------------------
    # CLASS METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Add contact.
    #
    #  @param cleanedData [ dict | None | in  ] - Cleaned data.
    #
    #  @exception N/A
    #
    #  @return contact.models.Contact - Django model class instance.
    @classmethod
    def addContact(cls, cleanedData):

        capthca       = cleanedData.pop('capthca'          , None)
        contextDomain = cleanedData.pop('context_domain'   , None)
        languageCode  = cleanedData.pop('language_code'    , LANGUAGE_CODE)

        if contextDomain:
            contextInstance = Context.objects.filter(domain=contextDomain)
            if contextInstance:
                cleanedData['context'] = contextInstance[0]
            else:
                cleanedData['context'] = None

        if languageCode:
            languageInstance = Language.objects.filter(code=languageCode)
            if languageInstance:
                cleanedData['language'] = languageInstance[0]
            else:
                cleanedData['language'] = None

        return Contact.objects.create(**cleanedData)

#
#
#
## @brief [ DJANGO MODEL CLASS ] - Django model class.
class Email(Model):
    #
    # ------------------------------------------------------------------------------------------------
    # CLASSES
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief [ DJANGO MODEL META CLASS ] - Meta class of django.db.models.Model class.
    class Meta:

        ## [ str ] - Verbose name of the model class.
        verbose_name        = 'Email'

        ## [ str ] - Verbose plural name of the model class.
        verbose_name_plural = 'Email'

        ## [ tuple ] - Ordering of the model class.
        ordering            = ('label',)

    #
    # ------------------------------------------------------------------------------------------------
    # FIELDS
    # ------------------------------------------------------------------------------------------------
    ## [ django.db.models.CharField ] - Icon.
    icon                    = models.CharField(max_length=200, blank=True, null=True,
                                               help_text='Font Awesome icon with "i" tag')

    ## [ django.db.models.CharField ] - Label.
    label                   = models.CharField(max_length=200,
                                               help_text='Label')

    ## [ django.db.models.EmailField ] - Email.
    email                   = models.EmailField(max_length=400,
                                                help_text='Email address')

    ## [ django.db.models.URLField ] - URL.
    url                     = models.URLField(help_text='URL', blank=True, null=True)

    #
    # ------------------------------------------------------------------------------------------------
    # BUILT-IN METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief String representation.
    #
    #  @exception N/A
    #
    #  @return str - String representation.
    def __str__(self):

        return Model.__dict__['_str'](self,
                                      '{} - {}'.format(self.label,
                                                       self.email))

#
#
#
## @brief [ DJANGO MODEL CLASS ] - Django model class.
class Phone(Model):
    #
    # ------------------------------------------------------------------------------------------------
    # CLASSES
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief [ DJANGO MODEL META CLASS ] - Meta class of django.db.models.Model class.
    class Meta:

        ## [ str ] - Verbose name of the model class.
        verbose_name        = 'Phone'

        ## [ str ] - Verbose plural name of the model class.
        verbose_name_plural = 'Phone'

        ## [ tuple ] - Ordering of the model class.
        ordering            = ('label',)

    #
    # ------------------------------------------------------------------------------------------------
    # FIELDS
    # ------------------------------------------------------------------------------------------------
    ## [ django.db.models.CharField ] - Icon.
    icon                    = models.CharField(max_length=200, blank=True, null=True,
                                               help_text='Font Awesome icon with "i" tag')

    ## [ django.db.models.CharField ] - Label.
    label                   = models.CharField(max_length=200,
                                               help_text='Label')

    ## [ django.db.models.CharField ] - Country code.
    country_code            = models.CharField(max_length=20, blank=True, null=True,
                                               help_text='Country code')

    ## [ django.db.models.CharField ] -Area code.
    area_code               = models.CharField(max_length=10,
                                               help_text='Area code')

    ## [ django.db.models.CharField ] - Phone number.
    phone_number            = models.CharField(max_length=20,
                                               help_text='Phone number')

    #
    # ------------------------------------------------------------------------------------------------
    # BUILT-IN METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief String representation.
    #
    #  @exception N/A
    #
    #  @return str - String representation.
    def __str__(self):

        return Model.__dict__['_str'](self,
                                      '{} - {} {} {}'.format(self.label,
                                                             self.country_code,
                                                             self.area_code,
                                                             self.phone_number,))

#
#
#
## @brief [ DJANGO MODEL CLASS ] - Django model class.
class SocialMedia(Model):
    #
    # ------------------------------------------------------------------------------------------------
    # CLASSES
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief [ DJANGO MODEL META CLASS ] - Meta class of django.db.models.Model class.
    class Meta:

        ## [ str ] - Verbose name of the model class.
        verbose_name        = 'Social Media'

        ## [ str ] - Verbose plural name of the model class.
        verbose_name_plural = 'Social Media'

        ## [ tuple ] - Ordering of the model class.
        ordering            = ('label',)

    #
    # ------------------------------------------------------------------------------------------------
    # FIELDS
    # ------------------------------------------------------------------------------------------------
    ## [ django.db.models.CharField ] - Icon.
    icon                    = models.CharField(max_length=200, blank=True, null=True,
                                               help_text='Font Awesome icon with "i" tag')

    ## [ django.db.models.CharField ] - Label.
    label                   = models.CharField(max_length=200,
                                               help_text='Label')

    ## [ django.db.models.URLField ] - URL.
    url                     = models.URLField(help_text='URL')

    #
    # ------------------------------------------------------------------------------------------------
    # BUILT-IN METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief String representation.
    #
    #  @exception N/A
    #
    #  @return str - String representation.
    def __str__(self):

        return Model.__dict__['_str'](self,
                                      '{} - {}'.format(self.label,
                                                       self.url))
