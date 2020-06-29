#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from django.http                    import Http404

from rest_framework                 import status
from rest_framework.pagination      import LimitOffsetPagination
from rest_framework.response        import Response
from rest_framework.views           import APIView

from userAccount.authentications    import UserAccountAuthentication
from userAccount.permissions        import UserAccountSuperUserPermission


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ REST FRAMEWORK API VIEW CLASS ] - REST framework simple collection API view class.
class SimpleCollectionAPIView(APIView):

    ## [ tuple ] - Authentication classes.
    authentication_classes  = (UserAccountAuthentication,)

    ## [ tuple ] - Permission classes.
    permission_classes      = (UserAccountSuperUserPermission,)

    ## [ django.db.models.Model ] - Model class object.
    MODEL_CLASS             = None

    ## [ rest_framework.serializers.ModelSerializer ] - REST framework model serializer class object.
    MODEL_CLASS_SERIALIZER  = None

    #
    # ------------------------------------------------------------------------------------------------
    # PUBLIC METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Get collection.
    #
    #  @param request [ rest_framework.request.Request  | None | in  ] - Request.
    #  @param format  [ str                             | None | in  ] - Format.
    #
    #  @exception N/A
    #
    #  @return rest_framework.response.Response - Response.
    def get(self, request, format=None):

        _objects = None
        if hasattr(self.MODEL_CLASS, 'is_active'):
            _objects    = self.MODEL_CLASS.objects.filter(is_active=True)
        else:
            _objects    = self.MODEL_CLASS.objects.filter()

        paginator   = LimitOffsetPagination()
        result      = paginator.paginate_queryset(_objects, request)
        serializer  = self.MODEL_CLASS_SERIALIZER(result,
                                                  many=True,
                                                  context={'request': request}
                                                  )

        return Response(serializer.data, status=status.HTTP_200_OK)

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

        serializer = self.MODEL_CLASS_SERIALIZER(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
## @brief [ REST FRAMEWORK API VIEW CLASS ] - REST framework simple detail API view class.
class SimpleDetailAPIView(APIView):

    ## [ tuple ] - Authentication classes.
    authentication_classes  = (UserAccountAuthentication,)

    ## [ tuple ] - Permission classes.
    permission_classes      = (UserAccountSuperUserPermission,)

    ## [ django.db.models.Model ] - Model class object.
    MODEL_CLASS             = None

    ## [ rest_framework.serializers.ModelSerializer ] - REST framework model serializer class object.
    MODEL_CLASS_SERIALIZER  = None

    #
    # ------------------------------------------------------------------------------------------------
    # PUBLIC METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Get object with given PK.
    #
    #  @param pk [ int | None | in  ] - Primary key.
    #
    #  @exception django.http.Http404 - If object with given PK doesn't exist.
    #
    #  @return django.db.models.Model - Model instance.
    def get_object(self, pk):

        try:
            return self.MODEL_CLASS.objects.get(pk=pk)
        except self.MODEL_CLASS.DoesNotExist:
            raise Http404

    #
    ## @brief Get detail.
    #
    #  @param request [ rest_framework.request.Request  | None | in  ] - Request.
    #  @param pk      [ int                             | None | in  ] - Primary key.
    #  @param format  [ str                             | None | in  ] - Format.
    #
    #  @exception N/A
    #
    #  @return rest_framework.response.Response - Response.
    def get(self, request, pk, format=None):

        _object     = self.get_object(pk)
        serializer  = self.MODEL_CLASS_SERIALIZER(_object, context={'request': request})

        return Response(serializer.data)

    #
    ## @brief Patch detail.
    #
    #  @param request [ rest_framework.request.Request  | None | in  ] - Request.
    #  @param pk      [ int                             | None | in  ] - Primary key.
    #  @param format  [ str                             | None | in  ] - Format.
    #
    #  @exception N/A
    #
    #  @return rest_framework.response.Response - Response.
    def patch(self, request, pk, format=None):

        _object     = self.get_object(pk)
        serializer  = self.MODEL_CLASS_SERIALIZER(_object, data=request.data, context={'request':request}, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #
    ## @brief Delete detail.
    #
    #  @param request [ rest_framework.request.Request  | None | in  ] - Request.
    #  @param pk      [ int                             | None | in  ] - Primary key.
    #  @param format  [ str                             | None | in  ] - Format.
    #
    #  @exception N/A
    #
    #  @return rest_framework.response.Response - Response.
    def delete(self, request, pk, format=None):

        _object = self.get_object(pk)
        _object.delete()

        return Response({'id': pk}, status=status.HTTP_200_OK)