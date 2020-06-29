#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from django.contrib import admin

from content        import models


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ DJANGO USER ADMIN MODEL CLASS ] - Django user admin model class.
class ContentTypeAdmin(admin.ModelAdmin):

    ## [ list of str ] - List filter.
    list_filter         = ['context', 'language']

#
## @brief [ DJANGO USER ADMIN MODEL CLASS ] - Django user admin model class.
class ContentAdmin(admin.ModelAdmin):

    ## [ list of str ] - List filter.
    list_filter         = ['context', 'language']

#
## @brief [ DJANGO USER ADMIN MODEL CLASS ] - Django user admin model class.
class ItemAdmin(admin.ModelAdmin):

    ## [ list of str ] - List filter.
    list_filter         = ['context', 'language']

admin.site.register(models.ContentType  , ContentTypeAdmin)
admin.site.register(models.Content      , ContentAdmin)
admin.site.register(models.Item         , ItemAdmin)
