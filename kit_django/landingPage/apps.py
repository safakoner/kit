#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------
## @package landingPage                     @brief [ PACKAGE   ] - Landing page.
## @dir     landingPage                     @brief [ DIRECTORY ] - Package root directory.
## @package landingPage.apps                @brief [ MODULE    ] - App module.
## @file    landingPage/apps.py             @brief [ FILE      ] - App module file.
## @package landingPage.views               @brief [ MODULE    ] - Views module.
## @file    landingPage/views.py            @brief [ FILE      ] - Views module file.


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
class LandingPageConfig(AppConfig):

    ## [ str ] - Name.
    name            = 'landingPage'

    ## [ str ] - Verbose Name.
    verbose_name    = 'Landing Page'
