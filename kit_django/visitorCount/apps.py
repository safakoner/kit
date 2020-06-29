#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------
## @package visitorCount                     @brief [ PACKAGE   ] - Visitor count tracker.
## @dir     visitorCount                     @brief [ DIRECTORY ] - Package root directory.
## @package visitorCount.admin               @brief [ MODULE    ] - Admin module.
## @file    visitorCount/admin.py            @brief [ FILE      ] - Admin module file.
## @package visitorCount.apps                @brief [ MODULE    ] - App module.
## @file    visitorCount/apps.py             @brief [ FILE      ] - App module file.
## @package visitorCount.middlewares         @brief [ MODULE    ] - Middlewares module.
## @file    visitorCount/middlewares.py      @brief [ FILE      ] - Middlewares module file.
## @package visitorCount.models              @brief [ MODULE    ] - Models module.
## @file    visitorCount/models.py           @brief [ FILE      ] - Models module file.
## @package visitorCount.serializers         @brief [ MODULE    ] - Serializers module.
## @file    visitorCount/serializers.py      @brief [ FILE      ] - Serializers module file.
## @package visitorCount.tests               @brief [ MODULE    ] - Tests module.
## @file    visitorCount/tests.py            @brief [ FILE      ] - Tests module file.
## @package visitorCount.urls                @brief [ MODULE    ] - URLs module.
## @file    visitorCount/urls.py             @brief [ FILE      ] - URLs module file.
## @package visitorCount.views               @brief [ MODULE    ] - Views module.
## @file    visitorCount/views.py            @brief [ FILE      ] - Views module file.


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
class VisitorCountConfig(AppConfig):

    ## [ str ] - Name.
    name            = 'visitorCount'

    ## [ str ] - Verbose Name.
    verbose_name    = 'Visitor Count'
