#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from rest_framework.permissions import BasePermission


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ REST FRAMEWORK PERMISSION CLASS ] - User account super user permission class.
class SimpleAPIAccountPermission(BasePermission):

    ## [ str ] - Error message.
    message = 'You do not have permission.'

    #
    ## @brief Determine whether permission should be granted.
    #
    #  @param request [ rest_framework.request.Request | None | in  ] - Request.
    #  @param view    [ variant                        | None | in  ] - View.
    #
    #  @exception N/A
    #
    #  @return bool - Result.
    def has_permission(self, request, view):

        return request.method == 'GET'
