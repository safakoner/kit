#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------
'''
WSGI config for kit_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
'''


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
import os

from    django.core.wsgi import get_wsgi_application


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kit_django.settings')

## [ django.core.handlers.wsgi.WSGIHandler ] - WSGI handler.
application = get_wsgi_application()

