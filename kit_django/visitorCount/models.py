#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from    django.db       import models
from    django.utils    import timezone



#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ DJANGO MODEL CLASS ] - Django model class.
class VisitorCount(models.Model):
    #
    # ------------------------------------------------------------------------------------------------
    # CLASSES
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief [ DJANGO MODEL META CLASS ] - Meta class of django.db.models.Model class.

    class Meta:
        ## [ str ] - Verbose name of the model class.
        verbose_name        = 'Visitor Count'

        ## [ str ] - Verbose plural name of the model class.
        verbose_name_plural = 'Visitor Count'

        ## [ tuple ] - Ordering of the model class.
        ordering            = ('-count', 'uri',)

    #
    # ------------------------------------------------------------------------------------------------
    # FIELDS
    # ------------------------------------------------------------------------------------------------
    ## [ django.db.models.CharField ] - Key.
    uri     = models.CharField(max_length=500,
                               help_text='URI')

    ## [ django.db.models.DateField ] - Date.
    date    = models.DateField(help_text='Date (Year and month)')

    ## [ django.db.models.PositiveIntegerField ] - Count.
    count   = models.PositiveIntegerField(default=0, blank=True, null=False,
                                          help_text='Visitor count')

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

        return '{} - {} - Visitors: {}'.format(self.uri,
                                               self.date.strftime('%Y/%m'),
                                               self.count)

    #
    # ------------------------------------------------------------------------------------------------
    # STATIC METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Add visitor for the given URI.
    #
    #  @param uri [ str | None | in  ] - URI.
    #
    #  @exception N/A
    #
    #  @return None - None.
    @staticmethod
    def addVisitor(uri):

        today = timezone.now()
        today = timezone.datetime(today.year, today.month, 1)

        modelInstance, created = VisitorCount.objects.get_or_create(uri=uri,
                                                                    date=today)
        modelInstance.count += 1
        modelInstance.save()

