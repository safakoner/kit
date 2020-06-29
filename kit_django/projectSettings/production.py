#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
import os

from   projectSettings.project import PROJECT_FOLDER_NAME


#
# ----------------------------------------------------------------------------------------------------
# COMMON
# ----------------------------------------------------------------------------------------------------
## [ bool ] - Production state.
IS_IN_PRODUCTION    = True

## [ bool ] - Debug.
DEBUG               = False

## [ str ] - Django project root.
DJANGO_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



#
# ----------------------------------------------------------------------------------------------------
# HOSTS
# ----------------------------------------------------------------------------------------------------
## [ list of str ] - Allowed hosts.
ALLOWED_HOSTS       = ['*']

## [ str ] - Base URL.
BASE_URL            = 'http://127.0.0.1:8000/'



#
# ----------------------------------------------------------------------------------------------------
# STATIC
# ----------------------------------------------------------------------------------------------------
## [ str ] - Static root.
STATIC_ROOT         = os.path.abspath(os.path.join(os.path.abspath(DJANGO_PROJECT_ROOT) , '..', '..', '{}_static_root'.format(PROJECT_FOLDER_NAME)))

## [ list of str ] - Static file directories.
STATICFILES_DIRS    = [os.path.abspath(os.path.join(os.path.abspath(DJANGO_PROJECT_ROOT), '..', '..', '{}_staticfiles_dirs'.format(PROJECT_FOLDER_NAME)))]



#
# ----------------------------------------------------------------------------------------------------
# STATIC
# ----------------------------------------------------------------------------------------------------
## [ str ] - Media root.
MEDIA_ROOT          = os.path.abspath(os.path.join(os.path.abspath(DJANGO_PROJECT_ROOT), '..', '..', '{}_media'.format(PROJECT_FOLDER_NAME)))



#
# ----------------------------------------------------------------------------------------------------
# TEMPLATES
# ----------------------------------------------------------------------------------------------------
## [ list of str ] - Template directories.
TEMPLATES_DIRS      = []



#
# ----------------------------------------------------------------------------------------------------
# DATABASES
# ----------------------------------------------------------------------------------------------------
## [ dict ] - Databases.
DATABASES = {
                'default':
                {
                    'ENGINE'    : 'django.db.backends.postgresql',
                    'NAME'      : '',
                    'USER'      : '',
                    'PASSWORD'  : '',
                    'HOST'      : '',
                    'PORT'      : '',
                }
            }



#
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
## [ list of dict ] - Password validators.
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]







