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

from projectSettings    import options


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ DJANGO MODEL CLASS ] - Django model class.
class ProjectSettings(Model):
    #
    # ------------------------------------------------------------------------------------------------
    # CLASSES
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief [ DJANGO MODEL META CLASS ] - Meta class of django.db.models.Model class.

    class Meta:
        ## [ str ] - Verbose name of the model class.
        verbose_name        = 'Project Settings'

        ## [ str ] - Verbose plural name of the model class.
        verbose_name_plural = 'Project Settings'

        ## [ tuple ] - Ordering of the model class.
        ordering            = ('key',)

    #
    # ------------------------------------------------------------------------------------------------
    # FIELDS
    # ------------------------------------------------------------------------------------------------
    ## [ django.db.models.CharField ] - Key.
    key     = models.CharField(max_length=500,
                               help_text='Key')

    ## [ django.db.models.TextField ] - Value.
    value   = models.TextField(blank=True, null=True,
                               help_text='Value')

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
                                      '{}{}'.format(self.key,
                                                    ' - {}'.format(self.value) if self.value else ''))

    #
    # ------------------------------------------------------------------------------------------------
    # PUBLIC METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Create default project settings.
    #
    #  @see projectSettings.options.DEFAULT_PROJECT_SETTINGS
    #
    #  @exception N/A
    #
    #  @return None - None.
    @staticmethod
    def createDefaultSettings():

        for key, value in options.DEFAULT_PROJECT_SETTINGS.items():

            projectSettings, created = ProjectSettings.objects.get_or_create(key=key)
            projectSettings.value = value
            projectSettings.save()

    #
    ## @brief Get whether web site is enabled.
    #
    #  @exception N/A
    #
    #  @return bool - Result.
    @staticmethod
    def getIsWebSiteEnabled():

        # ProjectSettings.createDefaultSettings()

        projectSettings = None

        try:
            projectSettings = ProjectSettings.objects.get(key=options.ProjectSettingsKey.kIsWebSiteEnabled)
        except ProjectSettings.DoesNotExist as error:
            return True

        if projectSettings.value.strip() in [0, '0', False, 'False', 'false']:
            return False

        return True

    #
    ## @brief Get whether REST API is enabled.
    #
    #  @exception N/A
    #
    #  @return bool - Result.
    @staticmethod
    def getIsRESTAPIEnabled():

        # ProjectSettings.createDefaultSettings()

        projectSettings = None

        try:
            projectSettings = ProjectSettings.objects.get(key=options.ProjectSettingsKey.kIsRESTAPIEnabled)
        except ProjectSettings.DoesNotExist as error:
            return True

        if projectSettings.value.strip() in [0, '0', False, 'False', 'false']:
            return False

        return True