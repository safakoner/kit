#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from django.contrib     import admin

from simpleAPIAccount   import models


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ DJANGO USER ADMIN MODEL CLASS ] - Django user admin model class.
class SimpleAPIAccountAdmin(admin.ModelAdmin):

    ## [ list of str ] - Readonly fields.
    readonly_fields     = ['token']

    ## [ list of str ] - List filter.
    list_filter         = ['context', 'language']

    ## [ list ] - Add field set.
    add_fieldsets       = [

        ('Abstract'             , {'fields':['is_active',
                                             'note',
                                             'context',
                                             'language',
                                             'code'
                                            ]
                                   }
         ),

        ('Account'              , {'fields':['label',
                                            'email',
                                            'expiration_date'
                                            ]
                                   }
         ),

    ]

    ## [ list ] - Field set.
    fieldsets           = [

        ('Abstract'             , {'fields':['is_active',
                                             'note',
                                             'context',
                                             'language',
                                             'code'
                                            ]
                                   }
         ),

        ('Account'              , {'fields':['label',
                                            'email',
                                            'token',
                                            'expiration_date'
                                            ]
                                   }
         ),

    ]

admin.site.register(models.SimpleAPIAccount, SimpleAPIAccountAdmin)
