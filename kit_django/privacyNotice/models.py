#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from django.db      import models

from core.models    import Model


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ DJANGO MODEL CLASS ] - Django model class.
class PrivacyNotice(Model):
    #
    # ------------------------------------------------------------------------------------------------
    # CLASSES
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief [ DJANGO MODEL META CLASS ] - Meta class of django.db.models.Model class.
    class Meta:

        ## [ str ] - Verbose name of the model class.
        verbose_name        = 'Privacy Notice'

        ## [ str ] - Verbose plural name of the model class.
        verbose_name_plural = 'Privacy Notice'

        ## [ tuple ] - Ordering of the model class.
        ordering            = ('order', 'primary_title',)

    #
    # ------------------------------------------------------------------------------------------------
    # FIELDS
    # ------------------------------------------------------------------------------------------------
    ## [ django.db.models.NullBooleanField ] - Order.
    order                   = models.PositiveIntegerField(default=0, blank=True,
                                                          help_text='Order')

    ## [ django.db.models.CharField ] - Primary title.
    primary_title           = models.CharField(max_length=1000,
                                               help_text='Primary Title')

    ## [ django.db.models.CharField ] - Secondary title.
    secondary_title         = models.CharField(max_length=1000, null=True, blank=True,
                                               help_text='Secondary Title')

    ## [ django.db.models.TextField ] - Testimonial body.
    body                    = models.TextField(help_text='Body')

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
                                      '{} - {}'.format(self.order,
                                                       self.primary_title))
