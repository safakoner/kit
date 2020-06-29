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
from    privacyNotice                   import views


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
## [ list of django.urls.path ] - URL list.
urlpatterns = []

if IS_REST_API_PROVIDED:

    urlpatterns += [

        path('{}/privacy-notices/'.format(REST_API_PATH)            , views.PrivacyNoticeCollectionView.as_view()       ),
        path('{}/privacy-notices/<int:pk>/'.format(REST_API_PATH)   , views.PrivacyNoticeDetailView.as_view()           ),

    ]