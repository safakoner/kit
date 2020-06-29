#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from    django.urls             import path

from    projectSettings.common  import IS_IN_PRODUCTION, WEB_SITE_DISABLED_REDIRECT_URL

from    errorPage               import views


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
## [ list of django.urls.path ] - URL list.
urlpatterns = [path(WEB_SITE_DISABLED_REDIRECT_URL , views.renderMaintenance)]

if not IS_IN_PRODUCTION:

    urlpatterns += [

        path('error-page/400/'              , views.render400),
        path('error-page/403/'              , views.render403),
        path('error-page/404/'              , views.render404),
        path('error-page/500/'              , views.render500),
        path('error-page/csrf/'             , views.renderCSRF),

    ]