#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------
## @package testimonial                     @brief [ PACKAGE   ] - Testimonials.
## @dir     testimonial                     @brief [ DIRECTORY ] - Package root directory.
## @package testimonial.admin               @brief [ MODULE    ] - Admin module.
## @file    testimonial/admin.py            @brief [ FILE      ] - Admin module file.
## @package testimonial.apps                @brief [ MODULE    ] - App module.
## @file    testimonial/apps.py             @brief [ FILE      ] - App module file.
## @package testimonial.handlers            @brief [ MODULE    ] - Signal handlers module.
## @file    testimonial/handlers.py         @brief [ FILE      ] - Signal handlers module file.
## @package testimonial.models              @brief [ MODULE    ] - Models module.
## @file    testimonial/models.py           @brief [ FILE      ] - Models module file.
## @package testimonial.serializers         @brief [ MODULE    ] - Serializers module.
## @file    testimonial/serializers.py      @brief [ FILE      ] - Serializers module file.
## @package testimonial.tests               @brief [ MODULE    ] - Tests module.
## @file    testimonial/tests.py            @brief [ FILE      ] - Tests module file.
## @package testimonial.urls                @brief [ MODULE    ] - URLs module.
## @file    testimonial/urls.py             @brief [ FILE      ] - URLs module file.
## @package testimonial.views               @brief [ MODULE    ] - Views module.
## @file    testimonial/views.py            @brief [ FILE      ] - Views module file.


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
class TestimonialConfig(AppConfig):

    ## [ str ] - Name.
    name            = 'testimonial'

    ## [ str ] - Verbose Name.
    verbose_name    = 'Testimonial'

    #
    ## @brief Ready.
    #
    #  @exception N/A
    #
    #  @return None - None.
    def ready(self):

        from .models   import Testimonial
        from .handlers import testimonialPreSave, testimonialPostSave, testimonialPreDelete

        pre_save.connect(testimonialPreSave     , sender=Testimonial)
        post_save.connect(testimonialPostSave   , sender=Testimonial)

        pre_delete.connect(testimonialPreDelete , sender=Testimonial)