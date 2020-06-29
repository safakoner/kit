#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from django.contrib import admin

from conversion     import models


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ DJANGO USER ADMIN MODEL CLASS ] - Django user admin model class.
class ConversionAdmin(admin.ModelAdmin):

    ## [ list of str ] - Readonly fields.
    readonly_fields     = ['visitor_count',
                           'subscriber_count',
                           'conversion_ratio',
                           'url_id',
                           'folder_name'
                           ]

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

        ('Report'               , {'fields':['visitor_count',
                                             'subscriber_count',
                                             'conversion_ratio'
                                             ]
                                   }
         ),

        ('Identification'       , {'fields':['url_id',
                                             'folder_name'
                                             ]
                                   }
         ),

        ('Information'          , {'fields':['label',
                                             'background_image',
                                             'primary_title',
                                             'secondary_title',
                                             'body',
                                             'success_page_body'
                                             ]
                                   }
         ),

        ('Subscribers'          , {'fields':['subscribers']}),

    ]

#
## @brief [ DJANGO USER ADMIN MODEL CLASS ] - Django user admin model class.
class SubscriberAdmin(admin.ModelAdmin):

    ## [ list of str ] - Readonly fields.
    readonly_fields     = ['subscriber_id',
                           'date_time']

    ## [ list of str ] - List filter.
    list_filter         = ['context', 'language']

    ## [ list ] - Field set.
    fieldsets           = [

        ('Abstract'             , {'fields':['is_active',
                                             'note',
                                            ]
                                   }
         ),

        ('Subscriber'          , {'fields':['date_time',
                                            'subscriber_id',
                                            'name',
                                            'email',
                                            'willing_to_pay'
                                            ]
                                   }
         ),

    ]

admin.site.register(models.Conversion, ConversionAdmin)
admin.site.register(models.Subscriber, SubscriberAdmin)
