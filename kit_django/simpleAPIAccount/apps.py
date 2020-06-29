#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------
## @package simpleAPIAccount                     @brief [ PACKAGE   ] - Simple API account.
## @dir     simpleAPIAccount                     @brief [ DIRECTORY ] - Package root directory.
## @package simpleAPIAccount.admin               @brief [ MODULE    ] - Admin module.
## @file    simpleAPIAccount/admin.py            @brief [ FILE      ] - Admin module file.
## @package simpleAPIAccount.apps                @brief [ MODULE    ] - App module.
## @file    simpleAPIAccount/apps.py             @brief [ FILE      ] - App module file.
## @package simpleAPIAccount.authentications     @brief [ MODULE    ] - Authentication module.
## @file    simpleAPIAccount/authentications.py  @brief [ FILE      ] - Authentication module file.
## @package simpleAPIAccount.handlers            @brief [ MODULE    ] - Signal handlers module.
## @file    simpleAPIAccount/handlers.py         @brief [ FILE      ] - Signal handlers module file.
## @package simpleAPIAccount.models              @brief [ MODULE    ] - Models module.
## @file    simpleAPIAccount/models.py           @brief [ FILE      ] - Models module file.
## @package simpleAPIAccount.permissions         @brief [ MODULE    ] - Permissions module.
## @file    simpleAPIAccount/permissions.py      @brief [ FILE      ] - Permissions module file.
## @package simpleAPIAccount.serializers         @brief [ MODULE    ] - Serializers module.
## @file    simpleAPIAccount/serializers.py      @brief [ FILE      ] - Serializers module file.
## @package simpleAPIAccount.tests               @brief [ MODULE    ] - Tests module.
## @file    simpleAPIAccount/tests.py            @brief [ FILE      ] - Tests module file.
## @package simpleAPIAccount.urls                @brief [ MODULE    ] - URLs module.
## @file    simpleAPIAccount/urls.py             @brief [ FILE      ] - URLs module file.
## @package simpleAPIAccount.views               @brief [ MODULE    ] - Views module.
## @file    simpleAPIAccount/views.py            @brief [ FILE      ] - Views module file.


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from django.apps                import AppConfig
from django.db.models.signals   import pre_save, post_save


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ APP CONFIG CLASS ] - App config class.
class SimpleAPIAccountConfig(AppConfig):

    ## [ str ] - Name.
    name            = 'simpleAPIAccount'

    ## [ str ] - Verbose Name.
    verbose_name    = 'Simple API Account'

    #
    ## @brief Ready.
    #
    #  @exception N/A
    #
    #  @return None - None.
    def ready(self):

        from .models   import SimpleAPIAccount
        from .handlers import apiAccountPreSave, apiAccountPostSave

        pre_save.connect(apiAccountPreSave  , sender=SimpleAPIAccount)
        post_save.connect(apiAccountPostSave, sender=SimpleAPIAccount)
