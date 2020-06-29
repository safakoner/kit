#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
import  uuid

from    django.db               import models

from    context.models          import Context
from    core.models             import Model
from    projectSettings.common  import LANGUAGE_CODE
from    language.models         import Language


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ DJANGO MODEL CLASS ] - Django model class.
class Newsletter(Model):
    #
    # ------------------------------------------------------------------------------------------------
    # CLASSES
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief [ DJANGO MODEL META CLASS ] - Meta class of django.db.models.Model class.
    class Meta:

        ## [ str ] - Verbose name of the model class.
        verbose_name        = 'Newsletter'

        ## [ str ] - Verbose plural name of the model class.
        verbose_name_plural = 'Newsletter'

        ## [ tuple ] - Ordering of the model class.
        ordering            = ('email',)

    #
    # ------------------------------------------------------------------------------------------------
    # FIELDS
    # ------------------------------------------------------------------------------------------------
    ## [ django.db.models.CharField ] - Name of the person.
    name                    = models.CharField(max_length=200, blank=True, null=True,
                                               help_text='First and last name')

    ## [ django.db.models.EmailField ] - Email address of the person.
    email                   = models.EmailField(max_length=200,
                                                help_text='Email')

    ## [ django.db.models.DateTimeField ] - Sign up date.
    date_time               = models.DateTimeField(auto_now_add=True,
                                                   help_text='Date and time of subscription')

    ## [ django.db.models.UUIDField ] - Subscriber ID.
    subscriber_id           = models.UUIDField(default=uuid.uuid4, editable=False,
                                               help_text='Subscriber ID')

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
                                      '{}{} - {}'.format(self.email,
                                                         ' - {}'.format(self.name) if self.name else '',
                                                         self.date_time.strftime('%Y/%m/%d - %H:%M')))

    #
    # ------------------------------------------------------------------------------------------------
    # CLASS METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Add subscriber.
    #
    #  @param cleanedData [ dict | None | in  ] - Cleaned data.
    #
    #  @exception N/A
    #
    #  @return newsletter.models.Newsletter - Django model class instance.
    @classmethod
    def addSubscriber(cls, cleanedData):

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

        newsletterInstance, created = Newsletter.objects.get_or_create(email=cleanedData['email'],
                                                                       context=cleanedData['context'])

        if cleanedData['name']:
            newsletterInstance.name  = cleanedData['name']

        newsletterInstance.is_active = True
        newsletterInstance.language  = cleanedData['language']

        newsletterInstance.save()

        return newsletterInstance