# Error Page App - Table of Content

- [Overview](#overview)
- [Models](#models)
- [See Also](#see-also)


# Overview

This app provides views to render error pages for the following errors.

- `400`  via `errorPage.views.render400`
- `403`  via `errorPage.views.render403`
- `404`  via `errorPage.views.render404`
- `500`  via `errorPage.views.render500`
- `CSRF` via `errorPage.views.renderCSRF`
- Maintenance, when site is under maintenance via `errorPage.views.renderMaintenance`

You can test the pages by following URLs in development mode. These URLs, apart from `maintenance/` will not be active
in production.

- `error-page/400/`
- `error-page/403/`
- `error-page/404/`
- `error-page/500/`
- `error-page/csrf/`
- `maintenance/`


# See Also

- `projectSettings.common.WEB_SITE_DISABLED_REDIRECT_URL`
- `core.middlewares.IsWebSiteEnabledMiddleware`
- `kit_django.settings.MIDDLEWARE`
- `errorPage.views`
- [core](CORE.md)


