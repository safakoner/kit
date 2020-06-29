#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from restAPICore.views              import SimpleCollectionAPIView, SimpleDetailAPIView

from privacyNotice.models           import PrivacyNotice
from privacyNotice.serializers      import PrivacyNoticeSerializer


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ REST FRAMEWORK API VIEW CLASS ] - REST framework API view class.
class PrivacyNoticeCollectionView(SimpleCollectionAPIView):

    ## [ tuple ] - Authentication classes.
    # authentication_classes  = ()
    
    ## [ tuple ] - Permission classes.
    # permission_classes      = ()

    ## [ django.db.models.Model ] - Model class object.
    MODEL_CLASS             = PrivacyNotice

    ## [ rest_framework.serializers.ModelSerializer ] - REST framework model serializer class object.
    MODEL_CLASS_SERIALIZER  = PrivacyNoticeSerializer

#
## @brief [ REST FRAMEWORK API VIEW CLASS ] - REST framework API view class.
class PrivacyNoticeDetailView(SimpleDetailAPIView):

    ## [ tuple ] - Authentication classes.
    # authentication_classes  = ()

    ## [ tuple ] - Permission classes.
    # permission_classes      = ()


    ## [ django.db.models.Model ] - Model class object.
    MODEL_CLASS             = PrivacyNotice

    ## [ rest_framework.serializers.ModelSerializer ] - REST framework model serializer class object.
    MODEL_CLASS_SERIALIZER  = PrivacyNoticeSerializer