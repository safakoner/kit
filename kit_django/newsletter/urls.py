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
from    newsletter                      import views


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
## [ list of django.urls.path ] - URL list.
urlpatterns = []

if IS_REST_API_PROVIDED:

    urlpatterns += [

        path('{}/newsletters/'.format(REST_API_PATH)            , views.NewsletterCollectionView.as_view()      ),
        path('{}/newsletters/<int:pk>/'.format(REST_API_PATH)   , views.NewsletterDetailView.as_view()          ),

    ]