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
from    termsOfUse                      import views


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
## [ list of django.urls.path ] - URL list.
urlpatterns = []

if IS_REST_API_PROVIDED:

    urlpatterns += [

        path('{}/terms-of-uses/'.format(REST_API_PATH)              , views.TermsOfUseCollectionView.as_view()          ),
        path('{}/terms-of-uses/<int:pk>/'.format(REST_API_PATH)     , views.TermsOfUseDetailView.as_view()              ),

    ]