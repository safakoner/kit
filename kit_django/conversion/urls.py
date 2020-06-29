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
from    conversion                      import views


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
## [ list of django.urls.path ] - URL list.
urlpatterns = [

        path('conversion/<slug:slug>/'                                      , views.renderConversion                    ),

        path('conversion/<slug:slug>/subscribe/<uuid:subscriberID>/'        , views.renderSubscribeByID                 ),
        path('conversion/<slug:slug>/unsubscribe/<uuid:subscriberID>/'      , views.renderUnsubscribeByID               ),

    ]

if IS_REST_API_PROVIDED:

    urlpatterns += [

        path('{}/conversions/'.format(REST_API_PATH)                        , views.ConversionCollectionView.as_view()  ),
        path('{}/conversions/<int:pk>/'.format(REST_API_PATH)               , views.ConversionDetailView.as_view()      ),

    ]
