#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from django.db          import models
from django.apps        import apps

from core.randomValue   import createRandomFileName

from context.apps       import ContextConfig
from context.options    import DEFAULT_CONTEXT


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief Get random file name for testimonial image.
#
#  @param instance [ appModel.models.Testimonial | None | in  ] - Testimonial model class instance.
#  @param fileName [ str                         | None | in  ] - File name.
#
#  @exception N/A
#
#  @return str - File path.
def getContextImageImageFieldUploadTo(instance, fileName):

    fileRelativePath = '{}/{}'.format(ContextConfig.name,
                                      createRandomFileName(fileName))

    return fileRelativePath

#
## @brief [ DJANGO MODEL CLASS ] - Django model class.
class Context(models.Model):
    #
    # ------------------------------------------------------------------------------------------------
    # CLASSES
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief [ DJANGO MODEL META CLASS ] - Meta class of django.db.models.Model class.
    class Meta:

        ## [ str ] - Verbose name of the model class.
        verbose_name        = 'Context'

        ## [ str ] - Verbose plural name of the model class.
        verbose_name_plural = 'Context'

        ## [ tuple ] - Ordering of the model class.
        ordering            = ('label',)

    #
    # ------------------------------------------------------------------------------------------------
    # FIELDS
    # ------------------------------------------------------------------------------------------------
    ## [ django.db.models.BooleanField ] - Whether this instance is active.
    is_active               = models.BooleanField(default=True,
                                                  help_text='Whether this instance is active')

    ## [ django.db.models.TextField ] - Note.
    note                    = models.TextField(blank=True, null=True,
                                               help_text='Note')

    ## [ django.db.models.CharField ] - Icon.
    icon                    = models.CharField(max_length=200, blank=True, null=True,
                                               help_text='Font Awesome icon with "i" tag')

    ## [ django.db.models.CharField ] - Code.
    code                    = models.CharField(max_length=200,
                                               help_text='Code')

    ## [ django.db.models.CharField ] - Label.
    label                   = models.CharField(max_length=200,
                                               help_text='Label')

    ## [ django.db.models.CharField ] - Domain.
    domain                  = models.CharField(max_length=400, blank=True, null=True,
                                               help_text='Domain')

    ## [ django.db.models.TextField ] - Description.
    description             = models.TextField(blank=True, null=True,
                                               help_text='Description')

    ## [ django.db.models.ImageField ] - Image.
    image                   = models.ImageField(upload_to=getContextImageImageFieldUploadTo, blank=True,
                                                help_text='Image')

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

        return '{} - {}'.format(self.label, self.code)

    #
    # ------------------------------------------------------------------------------------------------
    # STATIC METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Create default context.
    #
    #  @exception N/A
    #
    #  @return context.models.Context - Django model instance.
    @staticmethod
    def createDefaultContext():

        return Context.objects.create(**DEFAULT_CONTEXT)

    #
    # ------------------------------------------------------------------------------------------------
    # CLASS METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Get context for given `domain`
    #
    #  @param domain [ str | None | in  ] - Domain of the context to be obtained.
    #
    #  @exception N/A
    #
    #  @return context.models.Context - Django model class instance.
    @classmethod
    def getByDomain(cls, domain):

        contextInstance = Context.objects.filter(domain=domain)
        if contextInstance:
            return contextInstance[0]

        return None

    #
    ## @brief Get all dependencies of the context of given `domain`.
    #
    #  @param domain       [ str | None | in  ] - Domain of the context to be obtained.
    #  @param languageCode [ str | None | in  ] - Language code of the context to be obtained.
    #
    #  @exception N/A
    #
    #  @return dict - Processed context data with dependencies.
    @classmethod
    def getProcessedContextDataWithDependencies(cls, domain, languageCode='en-us'):

        Address         = apps.get_model('contact'      , 'Address')
        Email           = apps.get_model('contact'      , 'Email')
        Phone           = apps.get_model('contact'      , 'Phone')
        SocialMedia     = apps.get_model('contact'      , 'SocialMedia')

        Content         = apps.get_model('content'      , 'Content')
        ContentType     = apps.get_model('content'      , 'ContentType')
        Item            = apps.get_model('content'      , 'Item')
        FAQ             = apps.get_model('faq'          , 'FAQ')
        PrivacyNotice   = apps.get_model('privacyNotice', 'PrivacyNotice')
        TermsOfUse      = apps.get_model('termsOfUse'   , 'TermsOfUse')
        Testimonial     = apps.get_model('testimonial'  , 'Testimonial')

        contextData = cls.objects.filter(domain=domain) \
                        .prefetch_related(models.Prefetch('contact_address_related',
                                                          queryset=Address.objects.filter(is_active=True,
                                                                                          language__code=languageCode),
                                                          to_attr='contextAddresses'
                                                          ),
                                          models.Prefetch('contact_email_related',
                                                          queryset=Email.objects.filter(is_active=True,
                                                                                        language__code=languageCode),
                                                          to_attr='contextEmails'
                                                          ),
                                          models.Prefetch('contact_phone_related',
                                                          queryset=Phone.objects.filter(is_active=True,
                                                                                        language__code=languageCode),
                                                          to_attr='contextPhones'
                                                          ),
                                          models.Prefetch('contact_socialmedia_related',
                                                          queryset=SocialMedia.objects.filter(is_active=True,
                                                                                              language__code=languageCode),
                                                          to_attr='contextSocialMedias'
                                                          ),
                                          models.Prefetch('content_content_related',
                                                          queryset=Content.objects.filter(is_active=True,
                                                                                          language__code=languageCode),
                                                          to_attr='contextContents'
                                                          ),
                                          models.Prefetch('content_contenttype_related',
                                                          queryset=ContentType.objects.filter(is_active=True,
                                                                                              language__code=languageCode),
                                                          to_attr='contextContentTypes'
                                                          ),
                                          models.Prefetch('content_item_related',
                                                          queryset=Item.objects.filter(is_active=True,
                                                                                       language__code=languageCode),
                                                          to_attr='contextItems'
                                                          ),
                                          models.Prefetch('faq_faq_related',
                                                          queryset=FAQ.objects.filter(is_active=True,
                                                                                      language__code=languageCode),
                                                          to_attr='contextFAQs'
                                                          ),
                                          models.Prefetch('privacynotice_privacynotice_related',
                                                          queryset=PrivacyNotice.objects.filter(is_active=True,
                                                                                                language__code=languageCode),
                                                          to_attr='contextPrivacyNotices'
                                                          ),
                                          models.Prefetch('termsofuse_termsofuse_related',
                                                          queryset=TermsOfUse.objects.filter(is_active=True,
                                                                                             language__code=languageCode),
                                                          to_attr='contextTermsOfUses'
                                                          ),
                                          models.Prefetch('testimonial_testimonial_related',
                                                          queryset=Testimonial.objects.filter(is_active=True,
                                                                                              language__code=languageCode),
                                                          to_attr='contextTestimonials'
                                                          ),

                                          )

        contextData = contextData[0]

        #

        data = {'context'       : contextData,
                'addresses'     : contextData.contextAddresses,
                'emails'        : contextData.contextEmails,
                'phones'        : contextData.contextPhones,
                'socialMedias'  : contextData.contextSocialMedias,
                'faq'           : contextData.contextFAQs,
                'privacyNotices': contextData.contextPrivacyNotices,
                'termsOfUses'   : contextData.contextTermsOfUses,
                'testimonials'  : contextData.contextTestimonials[:5]
                }

        #

        itemContentTypes    = []
        contentContentTypes = []

        #

        items = {}
        for item in contextData.contextItems:

            if not item.content_type.label in items:
                items[item.content_type.label] = []

            items[item.content_type.label].append(item)

            if not item.content_type in itemContentTypes:
                itemContentTypes.append(item.content_type)

        data['items'] = items

        #

        contents = {}
        for content in contextData.contextContents:

            if not content.content_type.code in contents:
                contents[content.content_type.code] = []

            contents[content.content_type.code].append(content)

            if not content.content_type in contentContentTypes:
                contentContentTypes.append(content.content_type)

        #

        data['contents']            = contents
        data['itemContentTypes']    = itemContentTypes
        data['contentContentTypes'] = contentContentTypes
        data['contentTypes']        = list(set(itemContentTypes + contentContentTypes))

        return data