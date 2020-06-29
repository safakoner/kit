#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from restAPICore.views          import SimpleCollectionAPIView, SimpleDetailAPIView

from newsletter.models          import Newsletter
from newsletter.serializers     import NewsletterSerializer


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ REST FRAMEWORK API VIEW CLASS ] - REST framework simple collection API view class.
class NewsletterCollectionView(SimpleCollectionAPIView):

    ## [ tuple ] - Authentication classes.
    # authentication_classes  = ()

    ## [ tuple ] - Permission classes.
    # permission_classes      = ()

    ## [ django.db.models.Model ] - Model class object.
    MODEL_CLASS             = Newsletter

    ## [ rest_framework.serializers.ModelSerializer ] - REST framework model serializer class object.
    MODEL_CLASS_SERIALIZER  = NewsletterSerializer

#
## @brief [ REST FRAMEWORK API VIEW CLASS ] - REST framework simple detail API view class.
class NewsletterDetailView(SimpleDetailAPIView):

    ## [ tuple ] - Authentication classes.
    # authentication_classes  = ()

    ## [ tuple ] - Permission classes.
    # permission_classes      = ()

    ## [ django.db.models.Model ] - Model class object.
    MODEL_CLASS             = Newsletter

    ## [ rest_framework.serializers.ModelSerializer ] - REST framework model serializer class object.
    MODEL_CLASS_SERIALIZER  = NewsletterSerializer

