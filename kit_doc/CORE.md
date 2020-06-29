# Context App - Table of Content

- [Overview](#overview)
- [Models](#models)
- [Middlewares](#middlewares)
- [See Also](#see-also)


# Overview

This app provides some core functionalities, which can be utilized throughout any Django project. Please check Doxygen
documentation for more information.


# Models

| Name                                          | Description                                                           |
| :-------------------------------------------- | :-------------------------------------------------------------------- |
| core.models.Model                             | Abstract model                                                        |

This app provides `core.models.Model` abstract model class so you can use it for any other model. It provides the
following built-in fields.

| Field         | Description                                                                                           |
| :------------ | :---------------------------------------------------------------------------------------------------- |
| is_active     | Whether the instance is active                                                                        |
| note          | Note, for admin/superuser purposes                                                                    |
| context       | Context, foreign key to `context.models.Context` model                                                |
| language      | Language, foreign key to `language.models.Language` model                                             |
| code          | Code, can be used to refer to instance                                                                |

I use this abstract class virtually for all model classes in the project.


# Middlewares

Middleware module `core.middlewares` provides some built-in middlewares. 

| Name                                          | Description                                                           |
| :-------------------------------------------- | :-------------------------------------------------------------------- |
| `core.middlewares.IsWebSiteEnabledMiddleware` | Checks whether the site enabled                                       |
| `core.middlewares.LanguageMiddleware`         | Set language code in use                                              |

### `core.middlewares.IsWebSiteEnabledMiddleware`

If `projectSettings.common.CHECK_IF_WEB_SITE_DISABLED` is `True`, `projectSettings.models.ProjectSettings.getIsWebSiteEnabled`
method will be invoked by this middleware. Therefore, if the web site is not enabled, meaning that it is under maintenance
or something, middleware will redirect to `projectSettings.common.WEB_SITE_DISABLED_REDIRECT_URL`, which is handled by 
`errorPages.views.renderMaintenance` view by default.


# See Also

- `core.models.Model`
- `core.middlewares.IsWebSiteEnabledMiddleware`
- `core.middlewares.LanguageMiddleware`
- `kit_django.settings.MIDDLEWARE`
- `kit_doc/doxygen/html/namespacecore.html` (Doxygen Documentation)


