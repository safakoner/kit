#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------
## @package privacyNotice                     @brief [ PACKAGE   ] - Privacy notice.
## @dir     privacyNotice                     @brief [ DIRECTORY ] - Package root directory.
## @package privacyNotice.admin               @brief [ MODULE    ] - Admin module.
## @file    privacyNotice/admin.py            @brief [ FILE      ] - Admin module file.
## @package privacyNotice.apps                @brief [ MODULE    ] - App module.
## @file    privacyNotice/apps.py             @brief [ FILE      ] - App module file.
## @package privacyNotice.models              @brief [ MODULE    ] - Models module.
## @file    privacyNotice/models.py           @brief [ FILE      ] - Models module file.
## @package privacyNotice.serializers         @brief [ MODULE    ] - Serializers module.
## @file    privacyNotice/serializers.py      @brief [ FILE      ] - Serializers module file.
## @package privacyNotice.tests               @brief [ MODULE    ] - Tests module.
## @file    privacyNotice/tests.py            @brief [ FILE      ] - Tests module file.
## @package privacyNotice.urls                @brief [ MODULE    ] - URLs module.
## @file    privacyNotice/urls.py             @brief [ FILE      ] - URLs module file.
## @package privacyNotice.views               @brief [ MODULE    ] - Views module.
## @file    privacyNotice/views.py            @brief [ FILE      ] - Views module file.


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
class PrivacyNoticeConfig(AppConfig):

    ## [ str ] - Name.
    name            = 'privacyNotice'

    ## [ str ] - Verbose Name.
    verbose_name    = 'Privacy Notice'
