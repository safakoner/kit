#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------
## @package language                     @brief [ PACKAGE   ] - Project production and development settings.
## @dir     language                     @brief [ DIRECTORY ] - Package root directory.
## @package language.admin               @brief [ MODULE    ] - Admin module.
## @file    language/admin.py            @brief [ FILE      ] - Admin module file.
## @package language.apps                @brief [ MODULE    ] - App module.
## @file    language/apps.py             @brief [ FILE      ] - App module file.
## @package language.models              @brief [ MODULE    ] - Models module.
## @file    language/models.py           @brief [ FILE      ] - Models module file.
## @package language.options             @brief [ MODULE    ] - Options model module.
## @file    language/options.py          @brief [ FILE      ] - Options model module file.
## @package language.serializers         @brief [ MODULE    ] - Serializers module.
## @file    language/serializers.py      @brief [ FILE      ] - Serializers module file.
## @package language.tests               @brief [ MODULE    ] - Tests module.
## @file    language/tests.py            @brief [ FILE      ] - Tests module file.
## @package language.urls                @brief [ MODULE    ] - URLs module.
## @file    language/urls.py             @brief [ FILE      ] - URLs module file.
## @package language.views               @brief [ MODULE    ] - Views module.
## @file    language/views.py            @brief [ FILE      ] - Views module file.


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from django.apps import AppConfig


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ APP CONFIG CLASS ] - App config class.
class LanguageConfig(AppConfig):

    ## [ str ] - Name.
    name            = 'language'

    ## [ str ] - Verbose Name.
    verbose_name    = 'Language'
