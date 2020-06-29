#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ ENUM CLASS ] - Language codes.
class LanguageLabel(object):

    ## [ str ] - US english.
    kUSEnglish      = 'English'

    ## [ str ] - Spanish.
    kSpanish        = 'Spanish'

#
## @brief [ ENUM CLASS ] - Language codes.
class LanguageCode(object):

    ## [ str ] - US english.
    kUSEnglish      = 'en-us'

    ## [ str ] - Spanish.
    kSpanish        = 'es'

## [ tuple ] - Language choices.
LANGUAGE_CODE_CHOICES = (

    (LanguageCode.kUSEnglish    , LanguageLabel.kUSEnglish),

    (LanguageCode.kSpanish      , LanguageLabel.kSpanish),

    )

