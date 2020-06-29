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
class FAQ(Model):
    #
    # ------------------------------------------------------------------------------------------------
    # CLASSES
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief [ DJANGO MODEL META CLASS ] - Meta class of django.db.models.Model class.
    class Meta:

        ## [ str ] - Verbose name of the model class.
        verbose_name        = 'Frequently Asked Questions'

        ## [ str ] - Verbose plural name of the model class.
        verbose_name_plural = 'Frequently Asked Questions'

        ## [ tuple ] - Ordering of the model class.
        ordering            = ('order',)

    #
    # ------------------------------------------------------------------------------------------------
    # FIELDS
    # ------------------------------------------------------------------------------------------------
    ## [ django.db.models.PositiveIntegerField ] - Order.
    order                   = models.PositiveIntegerField(default=0, blank=True,
                                                          help_text='Order')

    ## [ django.db.models.TextField ] - Question.
    question                = models.TextField(help_text='Question')

    ## [ django.db.models.TextField ] - Answer.
    answer                  = models.TextField(help_text='Answer')

    ## [ django.db.models.CharField ] - Keywords.
    keywords                = models.CharField(max_length=1000, null=True, blank=True,
                                               help_text='Keywords')

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
                                                       self.question[:100]))
