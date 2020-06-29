#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from rest_framework         import exceptions
from rest_framework         import authentication

from projectSettings.common import CHECK_IF_REST_API_DISABLED
from projectSettings.models import ProjectSettings


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ REST FRAMEWORK AUTHENTICATION CLASS ] - User account authentication class.
class UserAccountAuthentication(authentication.BaseAuthentication):
    #
    ## @brief Authenticate.
    #
    #  @param request [ rest_framework.request.Request | None | in  ] - Request.
    #
    #  @exception rest_framework.exceptions.AuthenticationFailed - If authentication fails.
    #
    #  @return tuple of userAccount.models.UserAccount and rest_framework.authtoken.models.Token - If authentication is successful.
    def authenticate(self, request):

        if CHECK_IF_REST_API_DISABLED and not ProjectSettings.getIsRESTAPIEnabled():
            raise exceptions.AuthenticationFailed('REST API of this site is disabled.')

        #

        # I user TokenAuthentication here to illustrate an implementation
        # of custom authentication in REST framework
        _auth  = authentication.TokenAuthentication()
        result = _auth.authenticate(request)

        if not result:
            raise exceptions.AuthenticationFailed('Authentication failed.')

        userAccount, token = result

        if not userAccount.has_account_been_verified:
            raise exceptions.AuthenticationFailed('User has not been verified yet.')


        # Do further authenticate here

        return result
