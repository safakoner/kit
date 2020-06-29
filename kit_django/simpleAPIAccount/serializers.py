#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from restAPICore.serializers    import ModelSerializer

from simpleAPIAccount.models    import SimpleAPIAccount


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ REST FRAMEWORK MODEL SERIALIZER CLASS ] - Model serializer class.
class SimpleAPIAccountSerializer(ModelSerializer):

    ## @brief [ REST FRAMEWORK SERIALIZER META CLASS ] - Overwritten meta class.
    class Meta:

        ## [ django.db.models.Model ] - Django Model Class object.
        model               = SimpleAPIAccount

        ## [ tuple ] - Exclude fields.
        exclude             = ()

        ## [ tuple ] - Read only fields.
        read_only_fields    = ()