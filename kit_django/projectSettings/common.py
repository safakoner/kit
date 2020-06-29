#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
import projectSettings.server

if projectSettings.server.SERVER_IN_USE == projectSettings.server.Server.kDevelopment:

    from projectSettings.development import *

else:

    from projectSettings.production import *



#
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
## [ str ] - User model.
AUTH_USER_MODEL                 = 'userAccount.UserAccount'

## [ str ] - Login URL.
LOGIN_URL                       = '/account/sign-in/'

## [ str ] - Admin URL.
ADMIN_URL                       = 'admin/'

## [ bool ] - Whether to track visitor counts for each URL.
SHOULD_TRACK_VISITOR_COUNT      = True



#
# ----------------------------------------------------------------------------------------------------
# STATIC
# ----------------------------------------------------------------------------------------------------
## [ str ] - Static URL.
STATIC_URL                      = '/static/'



#
# ----------------------------------------------------------------------------------------------------
# MEDIA
# ----------------------------------------------------------------------------------------------------
## [ str ] - Media URL.
MEDIA_URL                       = '/media/'



#
# ----------------------------------------------------------------------------------------------------
# WEB SITE
# ----------------------------------------------------------------------------------------------------
## [ str ] - Redirect URL when web site is disabled.
WEB_SITE_DISABLED_REDIRECT_URL  = 'maintenance/'

## [ bool ] - Whether to check web site is disabled.
# If this variable is True, `projectSettings.models.ProjectSettings.getIsWebSiteEnabled` method
# will be invoked in `core.middlewares.IsWebSiteEnabledMiddleware` middleware. If web site is disabled
# request will be redirected to `projectSettings.common.WEB_SITE_DISABLED_REDIRECT_URL`
CHECK_IF_WEB_SITE_DISABLED      = True



#
# ----------------------------------------------------------------------------------------------------
# REST API
# ----------------------------------------------------------------------------------------------------
## [ str ] - REST API  path.
REST_API_PATH                   = 'api/v1'

## [ bool ] - Whether REST API is provided. If False, API URL's will not be used and raise 404.
IS_REST_API_PROVIDED            = True

## [ bool ] - Whether to check REST API is disabled.
# If this variable is True, `projectSettings.models.ProjectSettings.getIsRESTAPIEnabled` method
# will be invoked in authentication of the REST API calls.
CHECK_IF_REST_API_DISABLED      = True



#
# ----------------------------------------------------------------------------------------------------
# INTERNATIONALIZATION
# ----------------------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.0/topics/i18n/

## [ str ] - Language code.
LANGUAGE_CODE                   = 'en-us'



#
# ----------------------------------------------------------------------------------------------------
# E-MAIL
# ----------------------------------------------------------------------------------------------------
## [ bool ] - Email use TLS.
EMAIL_USE_TLS                   = False

## [ int ] - Email port.
EMAIL_PORT                      = 25

## [ str ] - Email host.
EMAIL_HOST                      = ''

## [ str ] - Email host user.
EMAIL_HOST_USER                 = ''

## [ str ] - Email from email.
DEFAULT_FROM_EMAIL              = ''

## [ str ] - Email server email.
SERVER_EMAIL                    = ''

## [ str ] - Email host password.
EMAIL_HOST_PASSWORD             = ''



#
# ----------------------------------------------------------------------------------------------------
# REST FRAMEWORK
# ----------------------------------------------------------------------------------------------------
## [ dict ] - REST framework settings.
REST_FRAMEWORK = {

    'DEFAULT_PAGINATION_CLASS'  : 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE'                 : 100,

}



