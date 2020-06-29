#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from django.db              import models

from language               import options

from projectSettings.common import LANGUAGE_CODE


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ DJANGO MODEL CLASS ] - Django model class.
class Language(models.Model):
    #
    # ------------------------------------------------------------------------------------------------
    # CLASSES
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief [ DJANGO MODEL META CLASS ] - Meta class of django.db.models.Model class.
    class Meta:

        ## [ str ] - Verbose name of the model class.
        verbose_name        = 'Language'

        ## [ str ] - Verbose plural name of the model class.
        verbose_name_plural = 'Language'

        ## [ tuple ] - Ordering of the model class.
        ordering            = ('label',)

    #
    # ------------------------------------------------------------------------------------------------
    # FIELDS
    # ------------------------------------------------------------------------------------------------
    ## [ django.db.models.CharField ] - Language code.
    code  = models.CharField(max_length=20,
                             help_text='Language code')

    ## [ django.db.models.CharField ] - Language label.
    label = models.CharField(max_length=200,
                             help_text='Language label')

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

        return '{} - {} - {}'.format(self.pk, self.label, self.code)

    #
    # ------------------------------------------------------------------------------------------------
    # STATIC METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Create default content types.
    #
    #  @see content.options.DEFAULT_CONTENT_TYPES
    #
    #  @exception N/A
    #
    #  @return list of language.models.Language - List of Django model instances.
    @staticmethod
    def createDefaultLanguages():

        languages = []

        for language in options.LANGUAGE_CODE_CHOICES:
            languageInstance, created = Language.objects.get_or_create(code=language[0])
            languageInstance.label = language[1]
            languageInstance.save()
            languages.append(languageInstance)

        return languages

    #
    ## @brief Get default language model instance.
    #
    #  @param defaultLanguageCode [ str | None | in  ] - Language code.
    #
    #  @see projectSettings.common.LANGUAGE_CODE
    #
    #  @exception N/A
    #
    #  @return language.models.Language - Model instance.
    #  @return None                     - If no model found for default language.
    @staticmethod
    def getDefaultLanguageModelInstance(defaultLanguageCode=LANGUAGE_CODE):

        try:
            return Language.objects.get(code=defaultLanguageCode)
        except Language.DoesNotExist as error:
            return None

    #
    ## @brief Get language labels.
    #
    #  @exception N/A
    #
    #  @return list of str  - Language labels.
    #  @return None         - If not instance found.
    @staticmethod
    def getLanguageLabels():

        label = Language.objects.all().values_list('label', flat=True)
        if label:
            return list(label)

        return None

    #
    ## @brief Get language codes.
    #
    #  @exception N/A
    #
    #  @return list of str  - Language codes.
    #  @return None         - If not instance found.
    @staticmethod
    def getLanguageCodes():

        codes = Language.objects.all().values_list('code', flat=True)
        if codes:
            return list(codes)

        return None


