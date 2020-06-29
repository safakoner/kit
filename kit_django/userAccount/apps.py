#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------
## @package userAccount                     @brief [ PACKAGE   ] - User account.
## @dir     userAccount                     @brief [ DIRECTORY ] - Package root directory.
## @package userAccount.admin               @brief [ MODULE    ] - Admin module.
## @file    userAccount/admin.py            @brief [ FILE      ] - Admin module file.
## @package userAccount.apps                @brief [ MODULE    ] - App module.
## @file    userAccount/apps.py             @brief [ FILE      ] - App module file.
## @package userAccount.authentications     @brief [ MODULE    ] - Authentication module.
## @file    userAccount/authentications.py  @brief [ FILE      ] - Authentication module file.
## @package userAccount.forms               @brief [ MODULE    ] - Forms module.
## @file    userAccount/forms.py            @brief [ FILE      ] - Forms module file.
## @package userAccount.handlers            @brief [ MODULE    ] - Signal handlers module.
## @file    userAccount/handlers.py         @brief [ FILE      ] - Signal handlers module file.
## @package userAccount.managers            @brief [ MODULE    ] - Managers module.
## @file    userAccount/managers.py         @brief [ FILE      ] - Managers module file.
## @package userAccount.models              @brief [ MODULE    ] - Models module.
## @file    userAccount/models.py           @brief [ FILE      ] - Models module file.
## @package userAccount.permissions         @brief [ MODULE    ] - Permissions module.
## @file    userAccount/permissions.py      @brief [ FILE      ] - Permissions module file.
## @package userAccount.serializers         @brief [ MODULE    ] - Serializers module.
## @file    userAccount/serializers.py      @brief [ FILE      ] - Serializers module file.
## @package userAccount.tests               @brief [ MODULE    ] - Tests module.
## @file    userAccount/tests.py            @brief [ FILE      ] - Tests module file.
## @package userAccount.urls                @brief [ MODULE    ] - URLs module.
## @file    userAccount/urls.py             @brief [ FILE      ] - URLs module file.
## @package userAccount.views               @brief [ MODULE    ] - Views module.
## @file    userAccount/views.py            @brief [ FILE      ] - Views module file.


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from django.apps                import AppConfig
from django.db.models.signals   import pre_save, post_save, pre_delete


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ APP CONFIG CLASS ] - App config class.
class UserAccountConfig(AppConfig):

    ## [ str ] - Name.
    name            = 'userAccount'

    ## [ str ] - Verbose Name.
    verbose_name    = 'User Account'

    #
    ## @brief Ready.
    #
    #  @exception N/A
    #
    #  @return None - None.
    def ready(self):

        from .models   import UserAccount
        from .handlers import userAccountPreSave, userAccountPostSave, userAccountPreDelete

        pre_save.connect(userAccountPreSave     , sender=UserAccount)
        post_save.connect(userAccountPostSave   , sender=UserAccount)

        pre_delete.connect(userAccountPreDelete , sender=UserAccount)