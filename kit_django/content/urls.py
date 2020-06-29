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
from    content                         import views


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
## [ list of django.urls.path ] - URL list.
urlpatterns = []

if IS_REST_API_PROVIDED:

    urlpatterns += [

        path('{}/content-types/'.format(REST_API_PATH)                  , views.ContentTypeCollectionView.as_view()     ),
        path('{}/content-types/<int:pk>/'.format(REST_API_PATH)         , views.ContentTypeDetailView.as_view()         ),

        path('{}/contents/'.format(REST_API_PATH)                       , views.ContentCollectionView.as_view()         ),
        path('{}/contents/<int:pk>/'.format(REST_API_PATH)              , views.ContentDetailView.as_view()             ),

        path('{}/items/'.format(REST_API_PATH)                          , views.ItemCollectionView.as_view()            ),
        path('{}/items/<int:pk>/'.format(REST_API_PATH)                 , views.ItemDetailView.as_view()                ),

    ]