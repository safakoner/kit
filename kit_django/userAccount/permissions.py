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
class UserAccountSuperUserPermission(BasePermission):

    ## [ str ] - Error message.
    message = 'You do not have super user permission.'

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

        if not hasattr(request, 'user'):
            return False

        if not hasattr(request.user, 'is_superuser'):
            return False

        if not request.user.is_superuser:
            return False

        # Check further permission here

        return True

#
## @brief [ REST FRAMEWORK PERMISSION CLASS ] - User account permission class.
class UserAccountPermission(BasePermission):

    ## [ str ] - Error message.
    message = 'You do not have permission for this operation.'

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

        # Check further permission here

        return True

