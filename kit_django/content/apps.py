#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------
## @package content                     @brief [ PACKAGE   ] - Content.
## @dir     content                     @brief [ DIRECTORY ] - Package root directory.
## @package content.admin               @brief [ MODULE    ] - Admin module.
## @file    content/admin.py            @brief [ FILE      ] - Admin module file.
## @package content.apps                @brief [ MODULE    ] - App module.
## @file    content/apps.py             @brief [ FILE      ] - App module file.
## @package content.handlers            @brief [ MODULE    ] - Signal handlers module.
## @file    content/handlers.py         @brief [ FILE      ] - Signal handlers module file.
## @package content.models              @brief [ MODULE    ] - Models module.
## @file    content/models.py           @brief [ FILE      ] - Models module file.
## @package content.serializers         @brief [ MODULE    ] - Serializers module.
## @file    content/serializers.py      @brief [ FILE      ] - Serializers module file.
## @package content.tests               @brief [ MODULE    ] - Tests module.
## @file    content/tests.py            @brief [ FILE      ] - Tests module file.
## @package content.urls                @brief [ MODULE    ] - URLs module.
## @file    content/urls.py             @brief [ FILE      ] - URLs module file.
## @package content.views               @brief [ MODULE    ] - Views module.
## @file    content/views.py            @brief [ FILE      ] - Views module file.


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
class ContentConfig(AppConfig):

    ## [ str ] - Name.
    name            = 'content'

    ## [ str ] - Verbose Name.
    verbose_name    = 'Content'

    #
    ## @brief Ready.
    #
    #  @exception N/A
    #
    #  @return None - None.
    def ready(self):

        from .models   import Content, Item
        from .handlers import preSave, postSave, preDelete

        pre_save.connect(preSave     , sender=Content)
        post_save.connect(postSave   , sender=Content)

        pre_delete.connect(preDelete , sender=Content)

        #

        pre_save.connect(preSave     , sender=Item)
        post_save.connect(postSave   , sender=Item)

        pre_delete.connect(preDelete , sender=Item)

