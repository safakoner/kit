#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------
'''
kit_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
'''


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from django.conf.urls           import handler400, handler403, handler404, handler500
from django.contrib             import admin
from django.urls                import path, include
from django.conf                import settings
from django.conf.urls.static    import static

from rest_framework.urlpatterns import format_suffix_patterns

from projectSettings.common     import ADMIN_URL


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
## [ str ] - 400 handler.
handler400 = 'errorPage.views.render400'

## [ str ] - 403 handler.
handler403 = 'errorPage.views.render403'

## [ str ] - 404 handler.
handler404 = 'errorPage.views.render404'

## [ str ] - 500 handler.
handler500 = 'errorPage.views.render500'

## [ list of django.urls.path ] - URL list.
urlpatterns = [

    path(ADMIN_URL                                      , admin.site.urls                       ),

    path(''                                             , include('contact.urls')               ),
    path(''                                             , include('content.urls')               ),
    path(''                                             , include('context.urls')               ),
    path(''                                             , include('conversion.urls')            ),
    path(''                                             , include('errorPage.urls')             ),
    path(''                                             , include('faq.urls')                   ),
    path(''                                             , include('landingPage.urls')           ),
    path(''                                             , include('language.urls')              ),
    path(''                                             , include('newsletter.urls')            ),
    path(''                                             , include('privacyNotice.urls')         ),
    path(''                                             , include('projectSettings.urls')       ),
    path(''                                             , include('simpleAPIAccount.urls')      ),
    path(''                                             , include('termsOfUse.urls')            ),
    path(''                                             , include('testimonial.urls')           ),
    path(''                                             , include('userAccount.urls')           ),

]

urlpatterns = format_suffix_patterns(urlpatterns) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)