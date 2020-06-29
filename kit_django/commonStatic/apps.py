#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------
## @package commonStatic                      @brief [ PACKAGE   ] - Common common-static files.
## @dir     commonStatic                      @brief [ DIRECTORY ] - Package root directory.
## @package commonStatic.apps                 @brief [ MODULE    ] - App module.
## @file    commonStatic/apps.py              @brief [ FILE      ] - App module file.


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
class CommonStaticConfig(AppConfig):

    ## [ str ] - Name.
    name            = 'commonStatic'

    ## [ str ] - Verbose Name.
    verbose_name    = 'Common Static'
