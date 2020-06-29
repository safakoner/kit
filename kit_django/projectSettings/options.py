#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ ENUM CLASS ] - Project settings keys.
class ProjectSettingsKey(object):

    ## [ str ] - Is web site enabled.
    kIsWebSiteEnabled   = 'isWebSiteEnabled'

    ## [ str ] - Is REST API Enabled.
    kIsRESTAPIEnabled   = 'isRESTAPIEnabled'

## [ dict ] - Default project settings.
DEFAULT_PROJECT_SETTINGS = {ProjectSettingsKey.kIsWebSiteEnabled:'1',
                            ProjectSettingsKey.kIsRESTAPIEnabled:'1'}