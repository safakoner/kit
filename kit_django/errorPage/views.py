#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from django.shortcuts import render


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief Render 400 (bad request) error page.
#
#  @param request   [ django.core.handlers.wsgi.WSGIRequest | None | in  ] - Request.
#  @param exception [ Exception                             | None | in  ] - Exception.
#
#  @exception N/A
#
#  @return django.http.response.HttpResponse - Response.
def render400(request, exception=None):

    context = {}

    return render(request,
                  'error-pages/400-rnd.html',
                  context)

#
## @brief Render 403 (permission denied) error page.
#
#  @param request   [ django.core.handlers.wsgi.WSGIRequest | None | in  ] - Request.
#  @param exception [ Exception                             | None | in  ] - Exception.
#
#  @exception N/A
#
#  @return django.http.response.HttpResponse - Response.
def render403(request, exception=None):

    context = {}

    return render(request,
                  'error-pages/403-rnd.html',
                  context)

#
## @brief Render 404 (not found) error page.
#
#  @param request   [ django.core.handlers.wsgi.WSGIRequest | None | in  ] - Request.
#  @param exception [ Exception                             | None | in  ] - Exception.
#
#  @exception N/A
#
#  @return django.http.response.HttpResponse - Response.
def render404(request, exception=None):

    context = {}

    return render(request,
                  'error-pages/404-rnd.html',
                  context)

#
## @brief Render 500 (server) error page.
#
#  @param request   [ django.core.handlers.wsgi.WSGIRequest | None | in  ] - Request.
#  @param exception [ Exception                             | None | in  ] - Exception.
#
#  @exception N/A
#
#  @return django.http.response.HttpResponse - Response.
def render500(request, exception=None):

    context = {}

    return render(request,
                  'error-pages/500-rnd.html',
                  context)

#
## @brief Render CSRF error page.
#
#  @param request [ django.core.handlers.wsgi.WSGIRequest | None | in  ] - Request.
#  @param reason  [ str                                   | None | in  ] - Reason.
#
#  @exception N/A
#
#  @return django.http.response.HttpResponse - Response.
def renderCSRF(request, reason=''):
    
    context = {'reason':reason}

    return render(request,
                  'error-pages/csrf-rnd.html',
                  context)

#
## @brief Render web site is not active page.
#
#  @param request [ django.core.handlers.wsgi.WSGIRequest | None | in  ] - Request.
#
#  @exception N/A
#
#  @return django.http.response.HttpResponse - Response.
def renderMaintenance(request):

    context = {}

    return render(request,
                  'error-pages/maintenance-rnd.html',
                  context)