#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from restAPICore.serializers    import ModelSerializer

from projectSettings.models     import ProjectSettings


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ REST FRAMEWORK MODEL SERIALIZER CLASS ] - Model serializer class.
class ProjectSettingsSerializer(ModelSerializer):

    ## @brief [ REST FRAMEWORK SERIALIZER META CLASS ] - Overwritten meta class.
    class Meta:

        ## [ django.db.models.Model ] - Django Model Class object.
        model               = ProjectSettings

        ## [ tuple ] - Exclude fields.
        exclude             = ()

        ## [ tuple ] - Read only fields.
        read_only_fields    = ()