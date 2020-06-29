#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------
## @package newsletter                     @brief [ PACKAGE   ] - Newsletter.
## @dir     newsletter                     @brief [ DIRECTORY ] - Package root directory.
## @package newsletter.admin               @brief [ MODULE    ] - Admin module.
## @file    newsletter/admin.py            @brief [ FILE      ] - Admin module file.
## @package newsletter.apps                @brief [ MODULE    ] - App module.
## @file    newsletter/apps.py             @brief [ FILE      ] - App module file.
## @package newsletter.forms               @brief [ MODULE    ] - Forms module.
## @file    newsletter/forms.py            @brief [ FILE      ] - Forms module file.
## @package newsletter.models              @brief [ MODULE    ] - Models module.
## @file    newsletter/models.py           @brief [ FILE      ] - Models module file.
## @package newsletter.serializers         @brief [ MODULE    ] - Serializers module.
## @file    newsletter/serializers.py      @brief [ FILE      ] - Serializers module file.
## @package newsletter.tests               @brief [ MODULE    ] - Tests module.
## @file    newsletter/tests.py            @brief [ FILE      ] - Tests module file.
## @package newsletter.urls                @brief [ MODULE    ] - URLs module.
## @file    newsletter/urls.py             @brief [ FILE      ] - URLs module file.
## @package newsletter.views               @brief [ MODULE    ] - Views module.
## @file    newsletter/views.py            @brief [ FILE      ] - Views module file.


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
class NewsletterConfig(AppConfig):

    ## [ str ] - Name.
    name            = 'newsletter'

    ## [ str ] - Verbose Name.
    verbose_name    = 'Newsletter'
