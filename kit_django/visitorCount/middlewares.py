#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
import  re
from    django.utils.deprecation    import MiddlewareMixin

from    projectSettings             import common
from    visitorCount.models         import VisitorCount


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ MIDDLEWARE CLASS ] - Middleware class.
class VisitorCountMiddleware(MiddlewareMixin):
    #
    ## @brief Process response.
    #
    #  @param request  [ django.core.handlers.wsgi.WSGIRequest | None | in  ] - Request.
    #  @param response [ django.http.response.HttpResponse     | None | in  ] - Response.
    #
    #  @exception N/A
    #
    #  @return django.http.response.HttpResponse - Response if web site is disabled.
    def process_response(self, request, response):

        if not common.SHOULD_TRACK_VISITOR_COUNT:
            return response

        uri = request.get_full_path()

        #

        # Ignore some URLs
        urlsToIgnore = [common.ADMIN_URL, common.STATIC_URL, common.MEDIA_URL, common.REST_API_PATH]
        for url in urlsToIgnore:
            if url in uri:
                return response

        #

        # Ignore files
        match = re.match(r'.*(\.[aA-zZ]+$)', uri)
        if match:
            return response

        VisitorCount.addVisitor(uri)

        return response


