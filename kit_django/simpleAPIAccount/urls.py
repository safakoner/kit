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
from    simpleAPIAccount                import views


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
## [ list of django.urls.path ] - URL list.
urlpatterns = []

if IS_REST_API_PROVIDED:

    urlpatterns += [

        path('{}/simple-api-accounts/'.format(REST_API_PATH)         , views.SimpleAPIAccountCollectionView.as_view()   ),
        path('{}/simple-api-accounts/<int:pk>/'.format(REST_API_PATH), views.SimpleAPIAccountDetailView.as_view()       ),

    ]