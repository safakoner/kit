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
class SimpleAPIAccount(Model):
    #
    # ------------------------------------------------------------------------------------------------
    # CLASSES
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief [ DJANGO MODEL META CLASS ] - Meta class of django.db.models.Model class.
    class Meta:

        ## [ str ] - Verbose name of the model class.
        verbose_name        = 'Simple API Account'

        ## [ str ] - Verbose plural name of the model class.
        verbose_name_plural = 'Simple API Account'

        ## [ tuple ] - Ordering of the model class.
        ordering            = ('label',)

    #
    # ------------------------------------------------------------------------------------------------
    # FIELDS
    # ------------------------------------------------------------------------------------------------
    ## [ django.db.models.CharField ] - Label.
    label                   = models.CharField(max_length=800,
                                               help_text='Label')

    ## [ django.db.models.EmailField ] - Email.
    email                   = models.EmailField(max_length=400, blank=True, null=True,
                                                help_text='Email address')

    ## [ django.db.models.CharField ] - Token.
    token                   = models.CharField(max_length=40, blank=True, null=True,
                                               help_text='token')

    ## [ django.db.models.DateTimeField ] - Expire.
    expiration_date         = models.DateTimeField(blank=True, null=True,
                                                   help_text='Expiration date')

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
                                      '{}{} - {}{}'.format('{} - '.format(self.email) if self.email else '',
                                                           self.label,
                                                           self.token,
                                                           ' - {}'.format(self.expiration_date.strftime('%Y/%m/%d')) if self.expiration_date else ''))