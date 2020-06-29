#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from restAPICore.views                      import SimpleCollectionAPIView, SimpleDetailAPIView

from context.models                         import Context
from context.serializers                    import ContextSerializer


#
# ----------------------------------------------------------------------------------------------------
# API VIEWS
# ----------------------------------------------------------------------------------------------------
#
## @brief [ REST FRAMEWORK API VIEW CLASS ] - REST framework API view class.
class ContextCollectionView(SimpleCollectionAPIView):

    ## [ tuple ] - Authentication classes.
    # authentication_classes  = ()

    ## [ tuple ] - Permission classes.
    # permission_classes      = ()

    ## [ django.db.models.Model ] - Model class object.
    MODEL_CLASS             = Context

    ## [ rest_framework.serializers.ModelSerializer ] - REST framework model serializer class object.
    MODEL_CLASS_SERIALIZER  = ContextSerializer

#
## @brief [ REST FRAMEWORK API VIEW CLASS ] - REST framework API view class.
class ContextDetailView(SimpleDetailAPIView):

    ## [ tuple ] - Authentication classes.
    # authentication_classes  = ()

    ## [ tuple ] - Permission classes.
    # permission_classes      = ()

    ## [ django.db.models.Model ] - Model class object.
    MODEL_CLASS             = Context

    ## [ rest_framework.serializers.ModelSerializer ] - REST framework model serializer class object.
    MODEL_CLASS_SERIALIZER  = ContextSerializer
