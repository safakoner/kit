# Project Settings App - Table of Content

- [Overview](#overview)
- [Hard Coded Settings](#hard-coded-settings)
- [Dynamic Settings](#dynamic-settings)
- [Models](#models)
- [REST API](#rest-api)
- [Postman Collections API](#postman-collections)
- [See Also](#see-also)


# Overview

This app provides settings.


# Hard Coded Settings

You can use the following modules for hard coded settings used by Django project.

**`projectSettings.development`**

Settings, which will only be used in development.

**`projectSettings.production`**

Settings, which will only be used in production

**`projectSettings.common`**

Common settings module determines whether development or production settings should be used, does so by using
`projectSettings.server.SERVER_IN_USE` member. The module also contains some hard coded common settings.


# Dynamic Settings
 
Provided `projectSettings.models.ProjectSettings` class can also be used to dynamically set project settings.

`projectSettings.models.ProjectSettings.getIsWebSiteEnabled` and `projectSettings.models.ProjectSettings.getIsRESTAPIEnabled`
static methods are provided to get the relevant settings respectively.

You can use `projectSettings.models.ProjectSettings.createDefaultSettings` static method to create default settings
stated in `projectSettings.options.DEFAULT_PROJECT_SETTINGS` member.


# Models

| Name                                          | Description                                                           |
| :-------------------------------------------- | :-------------------------------------------------------------------- |
| `projectSettings.models.ProjectSettings`      | Context model, which can be used for most of the models               |


# REST API

[Please visit documentation of REST API for detailed information](REST_API.md)

| Models & Endpoints                    | HTTP Methods         | View                                                   |
| :------------------------------------ | :------------------- | :----------------------------------------------------- |
| **ProjectSettings**                   |                      |                                                        |
| `api/v1/project-settings/`            | GET, POST            | `projectSettings.views.ProjectSettingsCollectionView`  |
| `api/v1/project-settings/1/`          | GET, PUT, DELETE     | `projectSettings.views.ProjectSettingsDetailView`      |


# Postman Collections

Please check `projectSettings/data/postman` for `Postman` collections.


# See Also

- `core.middlewares.IsWebSiteEnabledMiddleware`
- `kit_django.settings.MIDDLEWARE`
