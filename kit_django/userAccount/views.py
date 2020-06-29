#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from django.http                        import Http404

from rest_framework.authtoken.models    import Token
from rest_framework                     import status
from rest_framework.response            import Response

from restAPICore.views                  import SimpleCollectionAPIView, SimpleDetailAPIView

from userAccount.models                 import UserAccount
from userAccount.serializers            import UserAccountSuperUserSerializer, UserAccountSerializer
from userAccount.permissions            import UserAccountPermission


#
# ----------------------------------------------------------------------------------------------------
# USER ACCOUNT ADMIN API VIEWS
# ----------------------------------------------------------------------------------------------------
#
## @brief [ REST FRAMEWORK API VIEW CLASS ] - REST framework simple collection API view class.
class UserAccountSuperUserCollectionAPIView(SimpleCollectionAPIView):

    ## [ tuple ] - Authentication classes.
    # authentication_classes  = ()

    ## [ tuple ] - Permission classes.
    # permission_classes      = ()

    ## [ django.db.models.Model ] - Model class object.
    MODEL_CLASS             = UserAccount

    ## [ rest_framework.serializers.ModelSerializer ] - REST framework model serializer class object.
    MODEL_CLASS_SERIALIZER  = UserAccountSuperUserSerializer

#
## @brief [ REST FRAMEWORK API VIEW CLASS ] - REST framework simple detail API view class.
class UserAccountSuperUserDetailAPIView(SimpleDetailAPIView):

    ## [ tuple ] - Authentication classes.
    # authentication_classes  = ()

    ## [ tuple ] - Permission classes.
    # permission_classes      = ()

    ## [ django.db.models.Model ] - Model class object.
    MODEL_CLASS             = UserAccount

    ## [ rest_framework.serializers.ModelSerializer ] - REST framework model serializer class object.
    MODEL_CLASS_SERIALIZER  = UserAccountSuperUserSerializer

#
# ----------------------------------------------------------------------------------------------------
# USER ACCOUNT API VIEWS
# ----------------------------------------------------------------------------------------------------
#
## @brief [ REST FRAMEWORK API VIEW CLASS ] - REST framework simple detail API view class.
class UserAccountDetailAPIView(SimpleDetailAPIView):

    ## [ tuple ] - Authentication classes.
    # authentication_classes  = ()

    ## [ tuple ] - Permission classes.
    permission_classes      = (UserAccountPermission,)

    ## [ tuple ] - Allowed HTTP methods.
    http_method_names       = ('get', 'patch',)

    ## [ django.db.models.Model ] - Model class object.
    MODEL_CLASS             = UserAccount

    ## [ rest_framework.serializers.ModelSerializer ] - REST framework model serializer class object.
    MODEL_CLASS_SERIALIZER  = UserAccountSerializer

    #
    ## @brief Get object by token.
    #
    #  @param token [ str | None | in  ] - Token.
    #
    #  @exception django.http.Http404 - If no object found with given token
    #
    #  @return userAccount.models.UserAccount - Model class instance.
    def getByToken(self, token):

        if not token:
            raise Http404

        if token and 'token ' in token:
            token = token.split('token ')[1]

        if token and 'Token ' in token:
            token = token.split('Token ')[1]

        if token and 'Bearer ' in token:
            token = token.split('Bearer ')[1]

        if token and 'bearer ' in token:
            token = token.split('bearer ')[1]

        try:
            token = Token.objects.get(key=token)
            if token.user.is_active:
                return token.user
            raise Http404
        except Token.DoesNotExist:
            raise Http404

    #
    ## @brief Get detail.
    #
    #  @param request [ rest_framework.request.Request  | None | in  ] - Request.
    #  @param format  [ str                             | None | in  ] - Format.
    #
    #  @exception N/A
    #
    #  @return rest_framework.response.Response - Response.
    def get(self, request, format=None):

        _object     = self.getByToken(request.META.get('HTTP_AUTHORIZATION'))
        serializer  = self.MODEL_CLASS_SERIALIZER(_object, context={'request': request})

        return Response(serializer.data)

    #
    ## @brief Patch detail.
    #
    #  @param request [ rest_framework.request.Request  | None | in  ] - Request.
    #  @param format  [ str                             | None | in  ] - Format.
    #
    #  @exception N/A
    #
    #  @return rest_framework.response.Response - Response.
    def patch(self, request, format=None):

        _object     = self.getByToken(request.META.get('HTTP_AUTHORIZATION'))
        serializer  = self.MODEL_CLASS_SERIALIZER(_object, data=request.data, context={'request':request}, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
## @brief [ REST FRAMEWORK API VIEW CLASS ] - REST framework simple detail API view class.
class UserAccountTokenAuthDetailAPIView(SimpleDetailAPIView):

    ## [ tuple ] - Authentication classes.
    authentication_classes  = ()

    ## [ tuple ] - Permission classes.
    permission_classes      = ()

    ## [ tuple ] - Allowed HTTP methods.
    http_method_names       = ('post',)

    ## [ django.db.models.Model ] - Model class object.
    MODEL_CLASS             = UserAccount

    ## [ rest_framework.serializers.ModelSerializer ] - REST framework model serializer class object.
    MODEL_CLASS_SERIALIZER  = UserAccountSerializer

    #
    ## @brief Post.
    #
    #  @param request [ rest_framework.request.Request  | None | in  ] - Request.
    #  @param format  [ str                             | None | in  ] - Format.
    #
    #  @exception N/A
    #
    #  @return rest_framework.response.Response - Response.
    def post(self, request, format=None):

        if not 'email' in request.data:
            return Response('No email provided.', status=status.HTTP_400_BAD_REQUEST)

        if not 'password' in request.data:
            return Response('No password provided.', status=status.HTTP_400_BAD_REQUEST)

        userAccount = UserAccount.objects.filter(email=request.data['email'],
                                                 is_active=True)

        if not userAccount:
            return Response('User with given credentials does not exist.', status=status.HTTP_404_NOT_FOUND)

        userAccount = userAccount[0]

        if not userAccount.has_account_been_verified:
            return Response('Account has not been verified by the user.', status=status.HTTP_401_UNAUTHORIZED)

        if not userAccount.check_password(request.data['password']):
            return Response('User with given credentials does not exist.', status=status.HTTP_404_NOT_FOUND)

        serializer = UserAccountSerializer(userAccount, context={'request':request})

        return Response(serializer.data, status=status.HTTP_200_OK)