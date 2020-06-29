#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------
## @package contact                     @brief [ PACKAGE   ] - Contact.
## @dir     contact                     @brief [ DIRECTORY ] - Package root directory.
## @package contact.admin               @brief [ MODULE    ] - Admin module.
## @file    contact/admin.py            @brief [ FILE      ] - Admin module file.
## @package contact.apps                @brief [ MODULE    ] - App module.
## @file    contact/apps.py             @brief [ FILE      ] - App module file.
## @package contact.forms               @brief [ MODULE    ] - Forms module.
## @file    contact/forms.py            @brief [ FILE      ] - Forms module file.
## @package contact.models              @brief [ MODULE    ] - Models module.
## @file    contact/models.py           @brief [ FILE      ] - Models module file.
## @package contact.serializers         @brief [ MODULE    ] - Serializers module.
## @file    contact/serializers.py      @brief [ FILE      ] - Serializers module file.
## @package contact.tests               @brief [ MODULE    ] - Tests module.
## @file    contact/tests.py            @brief [ FILE      ] - Tests module file.
## @package contact.urls                @brief [ MODULE    ] - URLs module.
## @file    contact/urls.py             @brief [ FILE      ] - URLs module file.
## @package contact.views               @brief [ MODULE    ] - Views module.
## @file    contact/views.py            @brief [ FILE      ] - Views module file.


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
class ContactConfig(AppConfig):

    ## [ str ] - Name.
    name            = 'contact'

    ## [ str ] - Verbose Name.
    verbose_name    = 'Contact'
