#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from django.utils.timezone      import now

from rest_framework             import exceptions
from rest_framework             import authentication

from core.utilities             import getBearerOrToken

from projectSettings.common     import CHECK_IF_REST_API_DISABLED
from projectSettings.models     import ProjectSettings

from simpleAPIAccount.models    import SimpleAPIAccount


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ REST FRAMEWORK AUTHENTICATION CLASS ] - User account authentication class.
class SimpleAPIAccountAuthentication(authentication.BaseAuthentication):
    #
    ## @brief Authenticate.
    #
    #  @param request [ rest_framework.request.Request | None | in  ] - Request.
    #
    #  @exception rest_framework.exceptions.AuthenticationFailed - If authentication fails.
    #
    #  @return None - If authentication is successful.
    def authenticate(self, request):

        if CHECK_IF_REST_API_DISABLED and not ProjectSettings.getIsRESTAPIEnabled():
            raise exceptions.AuthenticationFailed('REST API of this site is disabled.')

        #

        token = authentication.get_authorization_header(request)
        if not token:
            raise exceptions.AuthenticationFailed('Authentication failed.')

        token = getBearerOrToken(token)

        #

        simpleAPIAccount = SimpleAPIAccount.objects.filter(is_active=True,
                                                           token=token)
        if not simpleAPIAccount:
            raise exceptions.AuthenticationFailed('Authentication failed.')

        simpleAPIAccount = simpleAPIAccount[0]

        if simpleAPIAccount.expiration_date:
            if now() > simpleAPIAccount.expiration_date:
                raise exceptions.AuthenticationFailed('Authentication failed.')

        return None
