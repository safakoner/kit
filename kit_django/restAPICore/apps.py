#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------
## @package restAPICore                     @brief [ PACKAGE   ] - Package for REST core functionalities.
## @dir     restAPICore                     @brief [ DIRECTORY ] - Package root directory.
## @package restAPICore.apps                @brief [ MODULE    ] - App module.
## @file    restAPICore/apps.py             @brief [ FILE      ] - App module file.
## @package restAPICore.serializers         @brief [ MODULE    ] - Serializers module.
## @file    restAPICore/serializers.py      @brief [ FILE      ] - Serializers module file.
## @package restAPICore.views               @brief [ MODULE    ] - Views module.
## @file    restAPICore/views.py            @brief [ FILE      ] - Views module file.


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from django.apps                import AppConfig


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ APP CONFIG CLASS ] - App config class.
class RestAPICoreConfig(AppConfig):

    ## [ str ] - Name.
    name            = 'restAPICore'

    ## [ str ] - Verbose Name.
    verbose_name    = 'Rest API Core'
