#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------
## @package projectSettings                     @brief [ PACKAGE   ] - Project production and development settings.
## @dir     projectSettings                     @brief [ DIRECTORY ] - Package root directory.
## @package projectSettings.admin               @brief [ MODULE    ] - Admin module.
## @file    projectSettings/admin.py            @brief [ FILE      ] - Admin module file.
## @package projectSettings.apps                @brief [ MODULE    ] - App module.
## @file    projectSettings/apps.py             @brief [ FILE      ] - App module file.
## @package projectSettings.common              @brief [ MODULE    ] - Common settings module.
## @file    projectSettings/common.py           @brief [ FILE      ] - Common settings module file.
## @package projectSettings.development         @brief [ MODULE    ] - Development settings module.
## @file    projectSettings/development.py      @brief [ FILE      ] - Development settings module file.
## @package projectSettings.models              @brief [ MODULE    ] - Models module.
## @file    projectSettings/models.py           @brief [ FILE      ] - Models module file.
## @package projectSettings.options             @brief [ MODULE    ] - Options model module.
## @file    projectSettings/options.py          @brief [ FILE      ] - Options model module file.
## @package projectSettings.production          @brief [ MODULE    ] - Production settings module.
## @file    projectSettings/production.py       @brief [ FILE      ] - Production settings module file.
## @package projectSettings.project             @brief [ MODULE    ] - Project settings module.
## @file    projectSettings/project.py          @brief [ FILE      ] - Project settings module file.
## @package projectSettings.serializers         @brief [ MODULE    ] - Serializers module.
## @file    projectSettings/serializers.py      @brief [ FILE      ] - Serializers module file.
## @package projectSettings.server              @brief [ MODULE    ] - Server settings module.
## @file    projectSettings/server.py           @brief [ FILE      ] - Server settings module file.
## @package projectSettings.tests               @brief [ MODULE    ] - Tests module.
## @file    projectSettings/tests.py            @brief [ FILE      ] - Tests module file.
## @package projectSettings.urls                @brief [ MODULE    ] - URLs module.
## @file    projectSettings/urls.py             @brief [ FILE      ] - URLs module file.
## @package projectSettings.views               @brief [ MODULE    ] - Views module.
## @file    projectSettings/views.py            @brief [ FILE      ] - Views module file.


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
class ProjectSettingsConfig(AppConfig):

    ## [ str ] - Name.
    name            = 'projectSettings'

    ## [ str ] - Verbose Name.
    verbose_name    = 'Project Settings'
