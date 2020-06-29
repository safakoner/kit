#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------
## @package core                                            @brief [ PACKAGE   ] - Package for core functionalities.
## @dir     core                                            @brief [ DIRECTORY ] - Package root directory.
## @package core.management                                 @brief [ PACKAGE   ] - Management package.
## @dir     core/management                                 @brief [ DIRECTORY ] - Management package directory.
## @package core.management.commands                        @brief [ PACKAGE   ] - Commands package.
## @dir     core/management/commands                        @brief [ DIRECTORY ] - Commands package directory.
## @package core.management.commands.createData             @brief [ MODULE    ] - Command module.
## @file    core/management/commands/createData.py          @brief [ FILE      ] - Command module file.
## @package core.management.commands.removeMigrations       @brief [ MODULE    ] - Command module.
## @file    core/management/commands/removeMigrations.py    @brief [ FILE      ] - Command module file.
## @package core.templatetags                               @brief [ PACKAGE   ] - Templatetags package.
## @dir     core/templatetags                               @brief [ DIRECTORY ] - Templatetags package directory.
## @package core.templatetags.markdownExtras                @brief [ MODULE    ] - Markdown templatetag module.
## @dir     core/templatetags/markdownExtras.py             @brief [ DIRECTORY ] - Markdown templatetag module file.
## @package core.admin                                      @brief [ MODULE    ] - Admin module.
## @file    core/admin.py                                   @brief [ FILE      ] - Admin module file.
## @package core.apps                                       @brief [ MODULE    ] - App module.
## @file    core/apps.py                                    @brief [ FILE      ] - App module file.
## @package core.email                                      @brief [ MODULE    ] - Email module.
## @file    core/email.py                                   @brief [ FILE      ] - Email module file.
## @package core.middlewares                                @brief [ MODULE    ] - Middlewares module.
## @file    core/middlewares.py                             @brief [ FILE      ] - Middlewares module file.
## @package core.models                                     @brief [ MODULE    ] - Abstract model module.
## @file    core/models.py                                  @brief [ FILE      ] - Abstract model module file.
## @package core.randomValue                                @brief [ MODULE    ] - Random module.
## @file    core/randomValue.py                             @brief [ FILE      ] - Random module file.
## @package core.storage                                    @brief [ MODULE    ] - Storage module.
## @file    core/storage.py                                 @brief [ FILE      ] - Storage module file.
## @package core.tests                                      @brief [ MODULE    ] - Tests module.
## @file    core/tests.py                                   @brief [ FILE      ] - Tests module file.
## @package core.utilities                                  @brief [ MODULE    ] - utilities module.
## @file    core/utilities.py                               @brief [ FILE      ] - utilities module file.


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from django.apps import AppConfig


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ APP CONFIG CLASS ] - App config class.
class CoreConfig(AppConfig):

    ## [ str ] - Name.
    name            = 'core'

    ## [ str ] - Verbose Name.
    verbose_name    = 'Core'

