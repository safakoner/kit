#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from    django.urls                     import path

from    projectSettings.common          import REST_API_PATH, IS_REST_API_PROVIDED
from    userAccount                     import views


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
## [ list of django.urls.path ] - URL list.
urlpatterns = []

if IS_REST_API_PROVIDED:

    urlpatterns += [

        path('{}/admin/user-accounts/'.format(REST_API_PATH)            , views.UserAccountSuperUserCollectionAPIView.as_view() ),
        path('{}/admin/user-accounts/<int:pk>/'.format(REST_API_PATH)   , views.UserAccountSuperUserDetailAPIView.as_view()     ),

        path('{}/user-accounts/'.format(REST_API_PATH)                  , views.UserAccountDetailAPIView.as_view()              ),
        path('{}/user-accounts/api-token-auth/'.format(REST_API_PATH)   , views.UserAccountTokenAuthDetailAPIView.as_view()     ),

    ]