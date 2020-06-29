#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from django.contrib import admin

from newsletter     import models


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ DJANGO USER ADMIN MODEL CLASS ] - Django user admin model class.
class NewsletterAdmin(admin.ModelAdmin):

    ## [ list of str ] - Readonly fields.
    readonly_fields     = ['date_time', 'subscriber_id']

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

        ('Contact    '          , {'fields':['date_time',
                                             'subscriber_id',
                                             'name',
                                             'email'
                                             ]
                                   }
         ),

    ]

admin.site.register(models.Newsletter, NewsletterAdmin)
