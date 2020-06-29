#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from restAPICore.views              import SimpleCollectionAPIView, SimpleDetailAPIView

from visitorCount.models            import VisitorCount
from visitorCount.serializers       import VisitorCountSerializer


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ REST FRAMEWORK API VIEW CLASS ] - REST framework API view class.
class VisitorCountCollectionView(SimpleCollectionAPIView):

    ## [ tuple ] - Authentication classes.
    # authentication_classes  = ()
    
    ## [ tuple ] - Permission classes.
    # permission_classes      = ()

    ## [ tuple ] - Allowed HTTP methods.
    http_method_names       = ('get',)

    ## [ django.db.models.Model ] - Model class object.
    MODEL_CLASS             = VisitorCount

    ## [ rest_framework.serializers.ModelSerializer ] - REST framework model serializer class object.
    MODEL_CLASS_SERIALIZER  = VisitorCountSerializer

#
## @brief [ REST FRAMEWORK API VIEW CLASS ] - REST framework API view class.
class VisitorCountDetailView(SimpleDetailAPIView):

    ## [ tuple ] - Authentication classes.
    # authentication_classes  = ()

    ## [ tuple ] - Permission classes.
    # permission_classes      = ()

    ## [ tuple ] - Allowed HTTP methods.
    http_method_names       = ('get',)

    ## [ django.db.models.Model ] - Model class object.
    MODEL_CLASS             = VisitorCount

    ## [ rest_framework.serializers.ModelSerializer ] - REST framework model serializer class object.
    MODEL_CLASS_SERIALIZER  = VisitorCountSerializer