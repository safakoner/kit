#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from rest_framework import serializers


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ REST FRAMEWORK MODEL SERIALIZER CLASS ] - REST framework model serializer class.
class ModelSerializer(serializers.ModelSerializer):

    #
    ## @brief Constructor.
    #
    #  @param args   [ tuple | None | in  ] - Arguments.
    #  @param kwargs [ dict  | None | in  ] - Keyword arguments.
    #
    #  @exception N/A
    #
    #  @return None - None.
    def __init__(self, *args, **kwargs):

        fields  = None
        request = kwargs.get('context').get('request')

        if request:
            fields = request.query_params.get('fields')
            if fields:
                fields = [x.strip() for x in fields.split(',')]

        super(ModelSerializer, self).__init__(*args, **kwargs)

        if fields:

            allowed  = set(fields)
            existing = set(self.fields.keys())

            for fieldName in existing - allowed:
                self.fields.pop(fieldName)
