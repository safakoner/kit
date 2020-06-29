#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from    django.utils.deprecation    import MiddlewareMixin
from    django.http                 import HttpResponseRedirect

from    projectSettings             import common
from    projectSettings.models      import ProjectSettings


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ MIDDLEWARE CLASS ] - Middleware class.
class IsWebSiteEnabledMiddleware(MiddlewareMixin):
    #
    ## @brief Process request.
    #
    #  If the web site is not active it will be redirected to `projectSettings.common.WEB_SITE_DISABLED_REDIRECT_URL`.
    #
    #  @param request [ django.core.handlers.wsgi.WSGIRequest | None | in  ] - Request.
    #
    #  @exception N/A
    #
    #  @return None                              - If web site is enabled.
    #  @return django.http.response.HttpResponse - Response if web site is disabled.
    def process_request(self, request):

        if common.CHECK_IF_WEB_SITE_DISABLED and not ProjectSettings.getIsWebSiteEnabled():
            # Web site is not enabled, do not allow any request
            # apart from the allowed URL
            if not request.build_absolute_uri().endswith(common.WEB_SITE_DISABLED_REDIRECT_URL) and \
               not common.ADMIN_URL in request.build_absolute_uri():
                return HttpResponseRedirect('{}{}'.format(common.BASE_URL, common.WEB_SITE_DISABLED_REDIRECT_URL))

#
## @brief [ MIDDLEWARE CLASS ] - Middleware class.
class LanguageMiddleware(MiddlewareMixin):
    #
    ## @brief Process request.
    #
    #  Method sets `request.sessionLanguageCode` and `request.languageCode` to language and use.
    #
    #  @param request [ django.core.handlers.wsgi.WSGIRequest | None | in  ] - Request.
    #
    #  @exception N/A
    #
    #  @return None                              - If web site is enabled.
    #  @return django.http.response.HttpResponse - Response if web site is disabled.
    def process_request(self, request):

        sessionLanguageCode = request.session.get('lang', common.LANGUAGE_CODE)
        languageCode        = request.COOKIES.get('lang', common.LANGUAGE_CODE)

        requestedLanguage   = request.GET.get('lang')

        if requestedLanguage:

            # TODO: Check supported languages here

            sessionLanguageCode = requestedLanguage
            languageCode        = requestedLanguage

        request.sessionLanguageCode = sessionLanguageCode
        request.languageCode        = languageCode
