#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------
## @package termsOfUse                     @brief [ PACKAGE   ] - Terms of use.
## @dir     termsOfUse                     @brief [ DIRECTORY ] - Package root directory.
## @package termsOfUse.admin               @brief [ MODULE    ] - Admin module.
## @file    termsOfUse/admin.py            @brief [ FILE      ] - Admin module file.
## @package termsOfUse.apps                @brief [ MODULE    ] - App module.
## @file    termsOfUse/apps.py             @brief [ FILE      ] - App module file.
## @package termsOfUse.models              @brief [ MODULE    ] - Models module.
## @file    termsOfUse/models.py           @brief [ FILE      ] - Models module file.
## @package termsOfUse.serializers         @brief [ MODULE    ] - Serializers module.
## @file    termsOfUse/serializers.py      @brief [ FILE      ] - Serializers module file.
## @package termsOfUse.tests               @brief [ MODULE    ] - Tests module.
## @file    termsOfUse/tests.py            @brief [ FILE      ] - Tests module file.
## @package termsOfUse.urls                @brief [ MODULE    ] - URLs module.
## @file    termsOfUse/urls.py             @brief [ FILE      ] - URLs module file.
## @package termsOfUse.views               @brief [ MODULE    ] - Views module.
## @file    termsOfUse/views.py            @brief [ FILE      ] - Views module file.


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
class TermsOfUseConfig(AppConfig):

    ## [ str ] - Name.
    name            = 'termsOfUse'

    ## [ str ] - Verbose Name.
    verbose_name    = 'Terms of Use'
