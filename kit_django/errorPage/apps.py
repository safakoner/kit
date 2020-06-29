#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------
## @package errorPage                     @brief [ PACKAGE   ] - Render error pages.
## @dir     errorPage                     @brief [ DIRECTORY ] - Package root directory.
## @package errorPage.apps                @brief [ MODULE    ] - App module.
## @file    errorPage/apps.py             @brief [ FILE      ] - App module file.
## @package errorPage.urls                @brief [ MODULE    ] - URLs module.
## @file    errorPage/urls.py             @brief [ FILE      ] - URLs module file.
## @package errorPage.views               @brief [ MODULE    ] - Views module.
## @file    errorPage/views.py            @brief [ FILE      ] - Views module file.


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
class ErrorPageConfig(AppConfig):

    ## [ str ] - Name.
    name            = 'errorPage'

    ## [ str ] - Verbose Name.
    verbose_name    = 'Error Page'
