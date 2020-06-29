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
from    contact                         import views


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
## [ list of django.urls.path ] - URL list.
urlpatterns = []

if IS_REST_API_PROVIDED:

    urlpatterns += [

        path('{}/addresses/'.format(REST_API_PATH)                  , views.AddressCollectionView.as_view()             ),
        path('{}/addresses/<int:pk>/'.format(REST_API_PATH)         , views.AddressDetailView.as_view()                 ),

        path('{}/contacts/'.format(REST_API_PATH)                   , views.ContactCollectionView.as_view()             ),
        path('{}/contacts/<int:pk>/'.format(REST_API_PATH)          , views.ContactDetailView.as_view()                 ),

        path('{}/emails/'.format(REST_API_PATH)                     , views.EmailCollectionView.as_view()               ),
        path('{}/emails/<int:pk>/'.format(REST_API_PATH)            , views.EmailDetailView.as_view()                   ),

        path('{}/phones/'.format(REST_API_PATH)                     , views.PhoneCollectionView.as_view()               ),
        path('{}/phones/<int:pk>/'.format(REST_API_PATH)            , views.PhoneDetailView.as_view()                   ),

        path('{}/social-medias/'.format(REST_API_PATH)              , views.SocialMediaCollectionView.as_view()         ),
        path('{}/social-medias/<int:pk>/'.format(REST_API_PATH)     , views.SocialMediaDetailView.as_view()             ),

    ]