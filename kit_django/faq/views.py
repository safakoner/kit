#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from restAPICore.views              import SimpleCollectionAPIView, SimpleDetailAPIView

from faq.models                     import FAQ
from faq.serializers                import FAQSerializer


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ REST FRAMEWORK API VIEW CLASS ] - REST framework API view class.
class FAQCollectionView(SimpleCollectionAPIView):

    ## [ tuple ] - Authentication classes.
    # authentication_classes  = ()
    
    ## [ tuple ] - Permission classes.
    # permission_classes      = ()

    ## [ django.db.models.Model ] - Model class object.
    MODEL_CLASS             = FAQ

    ## [ rest_framework.serializers.ModelSerializer ] - REST framework model serializer class object.
    MODEL_CLASS_SERIALIZER  = FAQSerializer

#
## @brief [ REST FRAMEWORK API VIEW CLASS ] - REST framework API view class.
class FAQDetailView(SimpleDetailAPIView):

    ## [ tuple ] - Authentication classes.
    # authentication_classes  = ()

    ## [ tuple ] - Permission classes.
    # permission_classes      = ()

    ## [ django.db.models.Model ] - Model class object.
    MODEL_CLASS             = FAQ

    ## [ rest_framework.serializers.ModelSerializer ] - REST framework model serializer class object.
    MODEL_CLASS_SERIALIZER  = FAQSerializer