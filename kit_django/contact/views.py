#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from restAPICore.views          import SimpleCollectionAPIView, SimpleDetailAPIView

from contact.models             import Address, Contact, Email, Phone, SocialMedia
from contact.serializers        import AddressSerializer, ContactSerializer, EmailSerializer, PhoneSerializer, SocialMediaSerializer


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ REST FRAMEWORK API VIEW CLASS ] - REST framework API view class.
class AddressCollectionView(SimpleCollectionAPIView):

    ## [ tuple ] - Authentication classes.
    # authentication_classes  = ()

    ## [ tuple ] - Permission classes.
    # permission_classes      = ()

    ## [ django.db.models.Model ] - Model class object.
    MODEL_CLASS             = Address

    ## [ rest_framework.serializers.ModelSerializer ] - REST framework model serializer class object.
    MODEL_CLASS_SERIALIZER  = AddressSerializer

#
## @brief [ REST FRAMEWORK API VIEW CLASS ] - REST framework API view class.
class AddressDetailView(SimpleDetailAPIView):

    ## [ tuple ] - Authentication classes.
    # authentication_classes  = ()

    ## [ tuple ] - Permission classes.
    # permission_classes      = ()

    ## [ django.db.models.Model ] - Model class object.
    MODEL_CLASS             = Address

    ## [ rest_framework.serializers.ModelSerializer ] - REST framework model serializer class object.
    MODEL_CLASS_SERIALIZER  = AddressSerializer

#
## @brief [ REST FRAMEWORK API VIEW CLASS ] - REST framework API view class.
class ContactCollectionView(SimpleCollectionAPIView):

    ## [ tuple ] - Authentication classes.
    # authentication_classes  = ()

    ## [ tuple ] - Permission classes.
    # permission_classes      = ()

    ## [ django.db.models.Model ] - Model class object.
    MODEL_CLASS             = Contact

    ## [ rest_framework.serializers.ModelSerializer ] - REST framework model serializer class object.
    MODEL_CLASS_SERIALIZER  = ContactSerializer

#
## @brief [ REST FRAMEWORK API VIEW CLASS ] - REST framework API view class.
class ContactDetailView(SimpleDetailAPIView):

    ## [ tuple ] - Authentication classes.
    # authentication_classes  = ()

    ## [ tuple ] - Permission classes.
    # permission_classes      = ()

    ## [ django.db.models.Model ] - Model class object.
    MODEL_CLASS             = Contact

    ## [ rest_framework.serializers.ModelSerializer ] - REST framework model serializer class object.
    MODEL_CLASS_SERIALIZER  = ContactSerializer

#
#
#
## @brief [ REST FRAMEWORK API VIEW CLASS ] - REST framework API view class.
class EmailCollectionView(SimpleCollectionAPIView):

    ## [ tuple ] - Authentication classes.
    # authentication_classes  = ()

    ## [ tuple ] - Permission classes.
    # permission_classes      = ()

    ## [ django.db.models.Model ] - Model class object.
    MODEL_CLASS             = Email

    ## [ rest_framework.serializers.ModelSerializer ] - REST framework model serializer class object.
    MODEL_CLASS_SERIALIZER  = EmailSerializer

#
## @brief [ REST FRAMEWORK API VIEW CLASS ] - REST framework API view class.
class EmailDetailView(SimpleDetailAPIView):

    ## [ tuple ] - Authentication classes.
    # authentication_classes  = ()

    ## [ tuple ] - Permission classes.
    # permission_classes      = ()

    ## [ django.db.models.Model ] - Model class object.
    MODEL_CLASS             = Email

    ## [ rest_framework.serializers.ModelSerializer ] - REST framework model serializer class object.
    MODEL_CLASS_SERIALIZER  = EmailSerializer

#
#
#
## @brief [ REST FRAMEWORK API VIEW CLASS ] - REST framework API view class.
class PhoneCollectionView(SimpleCollectionAPIView):

    ## [ tuple ] - Authentication classes.
    # authentication_classes  = ()

    ## [ tuple ] - Permission classes.
    # permission_classes      = ()

    ## [ django.db.models.Model ] - Model class object.
    MODEL_CLASS             = Phone

    ## [ rest_framework.serializers.ModelSerializer ] - REST framework model serializer class object.
    MODEL_CLASS_SERIALIZER  = PhoneSerializer

#
## @brief [ REST FRAMEWORK API VIEW CLASS ] - REST framework API view class.
class PhoneDetailView(SimpleDetailAPIView):

    ## [ tuple ] - Authentication classes.
    # authentication_classes  = ()

    ## [ tuple ] - Permission classes.
    # permission_classes      = ()

    ## [ django.db.models.Model ] - Model class object.
    MODEL_CLASS             = Phone

    ## [ rest_framework.serializers.ModelSerializer ] - REST framework model serializer class object.
    MODEL_CLASS_SERIALIZER  = PhoneSerializer

#
#
#
## @brief [ REST FRAMEWORK API VIEW CLASS ] - REST framework API view class.
class SocialMediaCollectionView(SimpleCollectionAPIView):

    ## [ tuple ] - Authentication classes.
    # authentication_classes  = ()

    ## [ tuple ] - Permission classes.
    # permission_classes      = ()

    ## [ django.db.models.Model ] - Model class object.
    MODEL_CLASS             = SocialMedia

    ## [ rest_framework.serializers.ModelSerializer ] - REST framework model serializer class object.
    MODEL_CLASS_SERIALIZER  = SocialMediaSerializer

#
## @brief [ REST FRAMEWORK API VIEW CLASS ] - REST framework API view class.
class SocialMediaDetailView(SimpleDetailAPIView):

    ## [ tuple ] - Authentication classes.
    # authentication_classes  = ()

    ## [ tuple ] - Permission classes.
    # permission_classes      = ()

    ## [ django.db.models.Model ] - Model class object.
    MODEL_CLASS             = SocialMedia

    ## [ rest_framework.serializers.ModelSerializer ] - REST framework model serializer class object.
    MODEL_CLASS_SERIALIZER  = SocialMediaSerializer

