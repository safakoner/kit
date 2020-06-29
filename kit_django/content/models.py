#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from django.db          import models

from core.models        import Model
from core.randomValue   import createRandomFileName

from content.apps       import ContentConfig


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ DJANGO MODEL CLASS ] - Django model class.
class ContentType(Model):
    #
    # ------------------------------------------------------------------------------------------------
    # CLASSES
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief [ DJANGO MODEL META CLASS ] - Meta class of django.db.models.Model class.
    class Meta:

        ## [ str ] - Verbose name of the model class.
        verbose_name        = 'Content Type'

        ## [ str ] - Verbose plural name of the model class.
        verbose_name_plural = 'Content Type'

        ## [ tuple ] - Ordering of the model class.
        ordering            = ('label',)

    #
    # ------------------------------------------------------------------------------------------------
    # FIELDS
    # ------------------------------------------------------------------------------------------------
    ## [ django.db.models.CharField ] - Icon.
    icon  = models.CharField(max_length=200, blank=True, null=True,
                             help_text='Font Awesome icon with "i" tag')

    ## [ django.db.models.CharField ] - Label.
    label = models.CharField(max_length=200,
                             help_text='Label')

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

        return Model.__dict__['_str'](self, self.label)

#
## @brief Get random file name for testimonial image.
#
#  @param instance [ appModel.models.Testimonial | None | in  ] - Testimonial model class instance.
#  @param fileName [ str                         | None | in  ] - File name.
#
#  @exception N/A
#
#  @return str - File path.
def getContentImageImageFieldUploadTo(instance, fileName):

    fileRelativePath = '{}/{}/{}'.format(ContentConfig.name,
                                         instance.__class__.__name__.lower(),
                                         createRandomFileName(fileName))

    return fileRelativePath

#
## @brief [ DJANGO MODEL CLASS ] - Django model class.
class Content(Model):
    #
    # ------------------------------------------------------------------------------------------------
    # CLASSES
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief [ DJANGO MODEL META CLASS ] - Meta class of django.db.models.Model class.
    class Meta:

        ## [ str ] - Verbose name of the model class.
        verbose_name        = 'Content'

        ## [ str ] - Verbose plural name of the model class.
        verbose_name_plural = 'Content'

        ## [ tuple ] - Ordering of the model class.
        ordering            = ('context', 'language', 'content_type', 'order',)

    #
    # ------------------------------------------------------------------------------------------------
    # FIELDS
    # ------------------------------------------------------------------------------------------------
    ## [ django.db.models.ForeignKey ] - Content type.
    content_type            = models.ForeignKey(ContentType, on_delete=models.SET_NULL, blank=True, null=True,
                                                default=None,
                                                help_text='Type of the content')

    ## [ django.db.models.IntegerField ] - Order.
    order                   = models.IntegerField(default=1, blank=True, null=True,
                                                  help_text='Order')

    ## [ django.db.models.CharField ] - FontAwesome icon.
    icon                    = models.CharField(max_length=200, blank=True, null=True,
                                               help_text='Font Awesome icon with "i" tag')

    ## [ django.db.models.ImageField ] - Image.
    image                   = models.ImageField(upload_to=getContentImageImageFieldUploadTo, blank=True,
                                                help_text='Image')

    ## [ django.db.models.CharField ] - Title.
    title                   = models.CharField(max_length=500, blank=True, null=True,
                                               help_text='Title')

    ## [ django.db.models.TextField ] - Content body.
    body                    = models.TextField(help_text='You can use Markdown')

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

        return Model.__dict__['_str'](self, '{}{}{} {}{}'.format('{} - '.format(self.context.domain) if self.context else '',
                                                                '{} - '.format(self.language.label) if self.language else '',
                                                                '{} - '.format(self.content_type.label) if self.content_type else '',
                                                                self.order,
                                                                ' - {}'.format(self.title if self.title else 'NO TITLE Only Body')))

#
## @brief Get random file name for testimonial image.
#
#  @param instance [ appModel.models.Testimonial | None | in  ] - Testimonial model class instance.
#  @param fileName [ str                         | None | in  ] - File name.
#
#  @exception N/A
#
#  @return str - File path.
def getItemImageImageFieldUploadTo(instance, fileName):

    fileRelativePath = '{}/{}/{}'.format(ContentConfig.name,
                                         instance.__class__.__name__.lower(),
                                         createRandomFileName(fileName))

    return fileRelativePath

#
## @brief [ DJANGO MODEL CLASS ] - Django model class.
class Item(Model):
    #
    # ------------------------------------------------------------------------------------------------
    # CLASSES
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief [ DJANGO MODEL META CLASS ] - Meta class of django.db.models.Model class.
    class Meta:

        ## [ str ] - Verbose name of the model class.
        verbose_name        = 'Item'

        ## [ str ] - Verbose plural name of the model class.
        verbose_name_plural = 'Item'

        ## [ tuple ] - Ordering of the model class.
        ordering            = ('context', 'language', 'content_type', 'order',)

    #
    # ------------------------------------------------------------------------------------------------
    # FIELDS
    # ------------------------------------------------------------------------------------------------
    ## [ django.db.models.ForeignKey ] - Content type.
    content_type            = models.ForeignKey(ContentType, on_delete=models.SET_NULL, blank=True, null=True,
                                                default=1,
                                                help_text='Type of the item')

    ## [ django.db.models.IntegerField ] - Order.
    order                   = models.IntegerField(default=1, blank=True, null=True,
                                                  help_text='Order')

    ## [ django.db.models.CharField ] - FontAwesome icon.
    icon                    = models.CharField(max_length=200, blank=True, null=True,
                                               help_text='Font Awesome icon with "i" tag')

    ## [ django.db.models.ImageField ] - Image.
    image                   = models.ImageField(upload_to=getItemImageImageFieldUploadTo, blank=True,
                                                help_text='Image')

    ## [ django.db.models.CharField ] - Title.
    title                   = models.CharField(max_length=500, blank=True, null=True,
                                               help_text='Title')

    ## [ django.db.models.TextField ] - Content body.
    body                    = models.TextField(help_text='You can use Markdown')

    ## [ django.db.models.URLField ] - URL.
    url                     = models.URLField(max_length=500, blank=True, null=True,
                                              help_text='URL')

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

        return Model.__dict__['_str'](self, '{}{}{} {}{}'.format('{} - '.format(self.context.domain) if self.context else '',
                                                                 '{} - '.format(self.language.label) if self.language else '',
                                                                 '{} - '.format(self.content_type.label) if self.content_type else '',
                                                                 self.order,
                                                                 ' - {}'.format(self.title) if self.title else ''))
