#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------
## @package context                     @brief [ PACKAGE   ] - context.
## @dir     context                     @brief [ DIRECTORY ] - Package root directory.
## @package context.admin               @brief [ MODULE    ] - Admin module.
## @file    context/admin.py            @brief [ FILE      ] - Admin module file.
## @package context.apps                @brief [ MODULE    ] - App module.
## @file    context/apps.py             @brief [ FILE      ] - App module file.
## @package context.models              @brief [ MODULE    ] - Models module.
## @file    context/models.py           @brief [ FILE      ] - Models module file.
## @package context.serializers         @brief [ MODULE    ] - Serializers module.
## @file    context/serializers.py      @brief [ FILE      ] - Serializers module file.
## @package context.tests               @brief [ MODULE    ] - Tests module.
## @file    context/tests.py            @brief [ FILE      ] - Tests module file.
## @package context.urls                @brief [ MODULE    ] - URLs module.
## @file    context/urls.py             @brief [ FILE      ] - URLs module file.
## @package context.views               @brief [ MODULE    ] - Views module.
## @file    context/views.py            @brief [ FILE      ] - Views module file.


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
class ContextConfig(AppConfig):

    ## [ str ] - Name.
    name            = 'context'

    ## [ str ] - Verbose Name.
    verbose_name    = 'Context'

    #
    ## @brief Ready.
    #
    #  @exception N/A
    #
    #  @return None - None.
    def ready(self):

        from .models   import Context
        from .handlers import contextPreSave, contextPostSave, contextPreDelete

        pre_save.connect(contextPreSave     , sender=Context)
        post_save.connect(contextPostSave   , sender=Context)

        pre_delete.connect(contextPreDelete , sender=Context)