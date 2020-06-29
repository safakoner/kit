#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
import  uuid

from    django.db                       import models

from    core.randomValue                import createRandomFileName
from    core.models                     import Model

from    conversion.apps                 import ConversionConfig


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ DJANGO MODEL CLASS ] - Django model class.
class Subscriber(Model):
    #
    # ------------------------------------------------------------------------------------------------
    # CLASSES
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief [ DJANGO MODEL META CLASS ] - Meta class of django.db.models.Model class.
    class Meta:

        ## [ str ] - Verbose name of the model class.
        verbose_name        = 'Subscriber'

        ## [ str ] - Verbose plural name of the model class.
        verbose_name_plural = 'Subscriber'

        ## [ tuple ] - Ordering of the model class.
        ordering            = ('email',)

    #
    # ------------------------------------------------------------------------------------------------
    # FIELDS
    # ------------------------------------------------------------------------------------------------
    ## [ django.db.models.CharField ] - Name.
    name                    = models.CharField(max_length=200, blank=True, null=True,
                                               help_text='First name, last name')

    ## [ django.db.models.EmailField ] - Email.
    email                   = models.EmailField(max_length=400,
                                                help_text='Email')

    ## [ django.db.models.CharField ] - Willing to pay.
    willing_to_pay          = models.CharField(max_length=200, blank=True, null=True,
                                               help_text='Willing to pay for the product/service')

    ## [ django.db.models.UUIDField ] - Subscriber ID.
    subscriber_id           = models.UUIDField(default=uuid.uuid4, editable=False,
                                               help_text='Subscriber ID')

    ## [ django.db.models.DateTimeField ] - Date and time.
    date_time               = models.DateTimeField(auto_now_add=True,
                                                   help_text='Date and time of subscription')

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
                                      '{}{}{}'.format(self.email,
                                                      ' - {}'.format(self.name) if self.name else '',
                                                      ' - Willing to pay: {}'.format(self.willing_to_pay) if self.willing_to_pay else ''))

#
## @brief Get random file name.
#
#  @param instance [ conversion.models.Conversion | None | in  ] - Django model class instance.
#  @param fileName [ str                          | None | in  ] - File name.
#
#  @exception N/A
#
#  @return str - File path.
def getConversionPageBackgroundImageImageFieldUploadTo(instance, fileName):

    fileRelativePath = '{}/{}/{}'.format(ConversionConfig.name,
                                         instance.folder_name,
                                         createRandomFileName(fileName))

    return fileRelativePath

#
## @brief [ DJANGO MODEL CLASS ] - Django model class.
class Conversion(Model):
    #
    # ------------------------------------------------------------------------------------------------
    # CLASSES
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief [ DJANGO MODEL META CLASS ] - Meta class of django.db.models.Model class.
    class Meta:

        ## [ str ] - Verbose name of the model class.
        verbose_name        = 'Conversion'

        ## [ str ] - Verbose plural name of the model class.
        verbose_name_plural = 'Conversion'

        ## [ tuple ] - Ordering of the model class.
        ordering            = ('label',)

    #
    # ------------------------------------------------------------------------------------------------
    # FIELDS
    # ------------------------------------------------------------------------------------------------
    ## [ django.db.models.PositiveIntegerField ] - Visitor count.
    visitor_count           = models.PositiveIntegerField(default=0,
                                                          help_text='Total visitor count of this conversion')

    ## [ django.db.models.PositiveIntegerField ] - Subscriber count.
    subscriber_count        = models.PositiveIntegerField(default=0,
                                                          help_text='Total conversion count of this conversion')

    ## [ django.db.models.FloatField ] - Conversion ratio.
    conversion_ratio        = models.FloatField(default=0.0,
                                                help_text='Conversion ratio (%)')

    ## [ django.db.models.CharField ] - Label.
    label                   = models.CharField(max_length=500,
                                               help_text='Label will be used in emails')

    ## [ django.db.models.ImageField ] - Background image.
    background_image        = models.ImageField(upload_to=getConversionPageBackgroundImageImageFieldUploadTo,
                                                help_text='Background image of the header')

    ## [ django.db.models.TextField ] - Primary title.
    primary_title           = models.TextField(help_text='You can use Markdown, provide # (h1)')

    ## [ django.db.models.TextField ] - Secondary title.
    secondary_title         = models.TextField(help_text='You can use Markdown, provide ## (h2)')

    ## [ django.db.models.TextField ] - Body.
    body                    = models.TextField(help_text='You can use Markdown, start with # (h1)')

    ## [ django.db.models.TextField ] - Success page body.
    success_page_body       = models.TextField(help_text='You can use Markdown')

    ## [ django.db.models.ManyToManyField ] - Subscribers.
    subscribers             = models.ManyToManyField(Subscriber, blank=True,
                                                     help_text='Subscriber list',)

    ## [ django.db.models.CharField ] - Folder name.
    folder_name             = models.CharField(max_length=200,
                                               help_text='Folder name used in media')

    ## [ django.db.models.SlugField ] - URL ID.
    url_id                  = models.SlugField(unique=True,
                                               help_text='ULR ID')

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
                                      '{} - Visitors: {} - Subscribers: {}'.format(self.label,
                                                                                   self.visitor_count,
                                                                                   self.subscriber_count))

    #
    # ------------------------------------------------------------------------------------------------
    # PUBLIC METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Calculate conversion ratio and save it.
    #
    #  Method doesn't save the instance. Therefore you must save the instance
    #  after invoking this method.
    #
    #  @param visitorCount    [ int | None | in  ] - Visitor count.
    #  @param subscriberCount [ int | None | in  ] - Subscriber count.
    #
    #  @exception N/A
    #
    #  @return None - None.
    def calculateConversionRate(self, visitorCount, subscriberCount):

        self.conversion_ratio = (round((100.0 / visitorCount) * (subscriberCount / 100.0) * 100.0, 1))

    #
    ## @brief Add visitor.
    #
    #  @param count [ int | None | in  ] - Count.
    #
    #  @exception N/A
    #
    #  @return None - None.
    def addVisitor(self, count=1):

        self.visitor_count += count

        self.calculateConversionRate(self.visitor_count, self.subscriber_count)

        self.save()

    #
    ## @brief Check whether has subscriber.
    #
    #  @param subscriber [ conversion.models.Subscriber | None | in  ] - Django model class instance.
    #
    #  @exception N/A
    #
    #  @return bool - Result.
    def hasSubscriber(self, subscriber):

        return self.subscribers.filter(pk=subscriber.pk).exists()

    #
    ## @brief Add subscriber.
    #
    #  @param subscriber [ conversion.models.Subscriber | None | in  ] - Django model class instance.
    #
    #  @exception N/A
    #
    #  @return None - None.
    def addSubscriber(self, subscriber):

        if self.subscribers.filter(pk=subscriber.pk).exists():
            return

        self.subscribers.add(subscriber)

        self.subscriber_count += 1

        self.calculateConversionRate(self.visitor_count, self.subscriber_count)

        self.save()

    #
    ## @brief remove subscriber.
    #
    #  @param subscriber [ conversion.models.Subscriber | None | in  ] - Django model class instance.
    #
    #  @exception N/A
    #
    #  @return None - None.
    def removeSubscriber(self, subscriber):

        if not self.subscribers.filter(pk=subscriber.pk).exists():
            return

        self.subscribers.remove(subscriber)

        self.subscriber_count -= 1

        self.calculateConversionRate(self.visitor_count, self.subscriber_count)

        self.save()
