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
from    projectSettings                 import views


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
## [ list of django.urls.path ] - URL list.
urlpatterns = []

if IS_REST_API_PROVIDED:

    urlpatterns += [

        path('{}/project-settings/'.format(REST_API_PATH)           , views.ProjectSettingsCollectionView.as_view()     ),
        path('{}/project-settings/<int:pk>/'.format(REST_API_PATH)  , views.ProjectSettingsDetailView.as_view()         ),

    ]