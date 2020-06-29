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
IS_IN_PRODUCTION    = False

## [ bool ] - Debug.
DEBUG               = True

## [ str ] - Django project root.
DJANGO_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



#
# ----------------------------------------------------------------------------------------------------
# HOSTS
# ----------------------------------------------------------------------------------------------------
## [ list of str ] - Allowed hosts.
ALLOWED_HOSTS       = ['http://127.0.0.1:8000/',
                       '127.0.0.1',
                       'localhost']

## [ str ] - Base URL.
BASE_URL            = 'http://127.0.0.1:8000/'



#
# ----------------------------------------------------------------------------------------------------
# STATIC
# ----------------------------------------------------------------------------------------------------
## [ str ] - Static root.
STATIC_ROOT         = os.path.abspath(os.path.join(os.path.abspath(DJANGO_PROJECT_ROOT) , '..', '{}_static_root'.format(PROJECT_FOLDER_NAME)))

## [ list of str ] - Static file directories.
STATICFILES_DIRS    = [os.path.abspath(os.path.join(os.path.abspath(DJANGO_PROJECT_ROOT), '..', '{}_staticfiles_dirs'.format(PROJECT_FOLDER_NAME)))]



#
# ----------------------------------------------------------------------------------------------------
# STATIC
# ----------------------------------------------------------------------------------------------------
## [ str ] - Media root.
MEDIA_ROOT          = os.path.abspath(os.path.join(os.path.abspath(DJANGO_PROJECT_ROOT), '..', '{}_media'.format(PROJECT_FOLDER_NAME)))



#
# ----------------------------------------------------------------------------------------------------
# TEMPLATES
# ----------------------------------------------------------------------------------------------------
#
## @brief Get template directories in development mode.
#
#  @exception N/A
#
#  @return list of str - Directories.
def getTemplateDirectories():

    directories = []

    for sfd in STATICFILES_DIRS:

        templatePath = os.path.join(sfd, 'templates')
        if not templatePath in directories:
            directories.append(templatePath)

    return directories

## [ list of str ] - Template directories.
TEMPLATES_DIRS = []



#
# ----------------------------------------------------------------------------------------------------
# DATABASES
# ----------------------------------------------------------------------------------------------------
## [ dict ] - Databases.
DATABASES = {
                'default':
                {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': os.path.join(DJANGO_PROJECT_ROOT, 'db.sqlite3'),
                    'TEST': {'NAME': 'test.sqlite3'}
                }
            }



#
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
## [ list of dict ] - Password validators.
AUTH_PASSWORD_VALIDATORS = []







