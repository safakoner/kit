#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from django.db              import models

from projectSettings.common import LANGUAGE_CODE

from context.models         import Context
from language.models        import Language



#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ ABSTRACT DJANGO MODEL CLASS ] - Abstract model class.
class Model(models.Model):
    #
    # ------------------------------------------------------------------------------------------------
    # CLASSES
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief [ DJANGO MODEL META CLASS ] - Meta class of django.db.models.Model class.
    class Meta:

        ## [ bool ] - Abstract class.
        abstract = True

    #
    # ------------------------------------------------------------------------------------------------
    # FIELDS
    # ------------------------------------------------------------------------------------------------
    ## [ django.db.models.BooleanField ] - Whether this instance is active.
    is_active   = models.BooleanField(default=True,
                                      help_text='Whether this instance is active')

    ## [ django.db.models.TextField ] - Note.
    note        = models.TextField(blank=True, null=True,
                                   help_text='Note')

    ## [ django.db.models.ForeignKey ] - Context.
    context     = models.ForeignKey(Context,
                                    related_name='%(app_label)s_%(class)s_related',
                                    related_query_name='%(app_label)s_%(class)ss',
                                    blank=True, null=True, on_delete=models.SET_NULL,
                                    default=None,
                                    help_text='Context')

    ## [ django.db.models.ForeignKey ] - Language.
    language    = models.ForeignKey(Language,
                                    related_name='%(app_label)s_%(class)s_related',
                                    related_query_name='%(app_label)s_%(class)ss',
                                    blank=True, null=True, on_delete=models.SET_NULL,
                                    default=None,
                                    help_text='Language of this instance')

    ## [ django.db.models.CharField ] - Code.
    code                    = models.CharField(max_length=200, blank=True, null=True,
                                               help_text='Code')

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

        return '{} object ({})'.format(self.__class__.__name__, self.pk)

    #
    # ------------------------------------------------------------------------------------------------
    # PROTECTED METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Add built in features information to string representation.
    #
    #  @param strRepresentation [ str | None | in  ] - Child class string representation.
    #
    #  @exception N/A
    #
    #  @return str - String representation.
    def _str(self, strRepresentation):

        abstract = '{}{}'.format('{}'.format(self.language) if self.language else '',
                                 '' if self.is_active else ' | INACTIVE')

        if abstract:
            return '{} [ {} ]'.format(strRepresentation, abstract)

        return strRepresentation

    #
    # ------------------------------------------------------------------------------------------------
    # PUBLIC METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Set default language of this instance.
    #
    #  @param defaultLanguageCode [ str | None | in  ] - Language code.
    #
    #  @see projectSettings.common.LANGUAGE_CODE
    #
    #  @exception N/A
    #
    #  @return bool - Result.
    def setDefaultLanguage(self, defaultLanguageCode=LANGUAGE_CODE):

        languageInstance = Language.getDefaultLanguageModelInstance(defaultLanguageCode)

        if languageInstance:
            self.language = languageInstance
            self.save()
            return True

        return False

    #
    # ------------------------------------------------------------------------------------------------
    # STATIC METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Set default language of given model instance.
    #
    #  @param modelInstance [ django.db.models.Model | None | in  ] - Django model class instance.
    #
    #  @see projectSettings.common.LANGUAGE_CODE
    #
    #  @exception N/A
    #
    #  @return bool - Result.
    @staticmethod
    def setDefaultLanguageOfModelInstance(modelInstance):

        if not hasattr(modelInstance, 'setDefaultLanguage'):
            return False

        return modelInstance.setDefaultLanguage()

