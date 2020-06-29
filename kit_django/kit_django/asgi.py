#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------
'''
ASGI config for kit_django project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
'''


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
import os

from    django.core.asgi import get_asgi_application


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kit_django.settings')

## [ django.core.handlers.asgi.ASGIHandler ] - ASGI handler.
application = get_asgi_application()
