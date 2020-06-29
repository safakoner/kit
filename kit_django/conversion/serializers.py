#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from restAPICore.serializers    import ModelSerializer

from conversion.models          import Conversion


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ REST FRAMEWORK MODEL SERIALIZER CLASS ] - Model serializer class.
class ConversionSerializer(ModelSerializer):

    ## @brief [ REST FRAMEWORK SERIALIZER META CLASS ] - Overwritten meta class.
    class Meta:

        ## [ django.db.models.Model ] - Django Model Class object.
        model               = Conversion

        ## [ tuple ] - Exclude fields.
        exclude             = ('subscribers',)

        ## [ tuple ] - Read only fields.
        read_only_fields    = ('visitor_count',
                               'subscriber_count',
                               'conversion_ratio'
                               'subscribers',
                               'folder_name',
                               'url_id')