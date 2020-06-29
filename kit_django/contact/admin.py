#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from django.contrib import admin

from contact        import models


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ DJANGO USER ADMIN MODEL CLASS ] - Django user admin model class.
class AddressAdmin(admin.ModelAdmin):

    ## [ list of str ] - List filter.
    list_filter         = ['context', 'language']

#
## @brief [ DJANGO USER ADMIN MODEL CLASS ] - Django user admin model class.
class ContactAdmin(admin.ModelAdmin):

    ## [ list of str ] - Readonly fields.
    readonly_fields     = ['date_time']

    ## [ list of str ] - List filter.
    list_filter         = ['context', 'language']

    ## [ list ] - Field set.
    fieldsets           = [

        ('Abstract'             , {'fields':['is_active',
                                             'note',
                                             'context',
                                             'language',
                                            ]
                                   }
         ),

        ('Contact    '          , {'fields':['is_processed',
                                             'date_time',
                                             'name',
                                             'company',
                                             'email',
                                             'subject',
                                             'message'
                                             ]
                                   }
         ),

    ]

#
## @brief [ DJANGO USER ADMIN MODEL CLASS ] - Django user admin model class.
class EmailAdmin(admin.ModelAdmin):

    ## [ list of str ] - List filter.
    list_filter         = ['context', 'language']

#
## @brief [ DJANGO USER ADMIN MODEL CLASS ] - Django user admin model class.
class PhoneAdmin(admin.ModelAdmin):

    ## [ list of str ] - List filter.
    list_filter         = ['context', 'language']

#
## @brief [ DJANGO USER ADMIN MODEL CLASS ] - Django user admin model class.
class SocialMediaAdmin(admin.ModelAdmin):

    ## [ list of str ] - List filter.
    list_filter         = ['context', 'language']


admin.site.register(models.Address      , AddressAdmin)
admin.site.register(models.Contact      , ContactAdmin)
admin.site.register(models.Email        , EmailAdmin)
admin.site.register(models.Phone        , PhoneAdmin)
admin.site.register(models.SocialMedia  , SocialMediaAdmin)
