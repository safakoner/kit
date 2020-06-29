#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------
## @package conversion                     @brief [ PACKAGE   ] - Conversion for lean startups.
## @dir     conversion                     @brief [ DIRECTORY ] - Package root directory.
## @package conversion.admin               @brief [ MODULE    ] - Admin module.
## @file    conversion/admin.py            @brief [ FILE      ] - Admin module file.
## @package conversion.apps                @brief [ MODULE    ] - App module.
## @file    conversion/apps.py             @brief [ FILE      ] - App module file.
## @package conversion.forms               @brief [ MODULE    ] - Forms module.
## @file    conversion/forms.py            @brief [ FILE      ] - Forms module file.
## @package conversion.handlers            @brief [ MODULE    ] - Signal handlers module.
## @file    conversion/handlers.py         @brief [ FILE      ] - Signal handlers module file.
## @package conversion.models              @brief [ MODULE    ] - Models module.
## @file    conversion/models.py           @brief [ FILE      ] - Models module file.
## @package conversion.notifications       @brief [ MODULE    ] - Notifications module.
## @file    conversion/notifications.py    @brief [ FILE      ] - Notifications module file.
## @package conversion.serializers         @brief [ MODULE    ] - Serializers module.
## @file    conversion/serializers.py      @brief [ FILE      ] - Serializers module file.
## @package conversion.tests               @brief [ MODULE    ] - Tests module.
## @file    conversion/tests.py            @brief [ FILE      ] - Tests module file.
## @package conversion.urls                @brief [ MODULE    ] - URLs module.
## @file    conversion/urls.py             @brief [ FILE      ] - URLs module file.
## @package conversion.views               @brief [ MODULE    ] - Views module.
## @file    conversion/views.py            @brief [ FILE      ] - Views module file.


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
class ConversionConfig(AppConfig):

    ## [ str ] - Name.
    name            = 'conversion'

    ## [ str ] - Verbose Name.
    verbose_name    = 'Conversion'

    #
    ## @brief Ready.
    #
    #  @exception N/A
    #
    #  @return None - None.
    def ready(self):

        from .models   import Conversion
        from .handlers import conversionPreSave, conversionPostSave, conversionPreDelete

        pre_save.connect(conversionPreSave      , sender=Conversion)
        post_save.connect(conversionPostSave    , sender=Conversion)

        pre_delete.connect(conversionPreDelete  , sender=Conversion)
