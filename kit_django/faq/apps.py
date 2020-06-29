#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------
## @package faq                     @brief [ PACKAGE   ] - Frequently Asked Questions.
## @dir     faq                     @brief [ DIRECTORY ] - Package root directory.
## @package faq.admin               @brief [ MODULE    ] - Admin module.
## @file    faq/admin.py            @brief [ FILE      ] - Admin module file.
## @package faq.apps                @brief [ MODULE    ] - App module.
## @file    faq/apps.py             @brief [ FILE      ] - App module file.
## @package faq.models              @brief [ MODULE    ] - Models module.
## @file    faq/models.py           @brief [ FILE      ] - Models module file.
## @package faq.serializers         @brief [ MODULE    ] - Serializers module.
## @file    faq/serializers.py      @brief [ FILE      ] - Serializers module file.
## @package faq.tests               @brief [ MODULE    ] - Tests module.
## @file    faq/tests.py            @brief [ FILE      ] - Tests module file.
## @package faq.urls                @brief [ MODULE    ] - URLs module.
## @file    faq/urls.py             @brief [ FILE      ] - URLs module file.
## @package faq.views               @brief [ MODULE    ] - Views module.
## @file    faq/views.py            @brief [ FILE      ] - Views module file.


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
class FAQConfig(AppConfig):

    ## [ str ] - Name.
    name            = 'faq'

    ## [ str ] - Verbose Name.
    verbose_name    = 'Frequently Asked Questions'
