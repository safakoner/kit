# Simple API Account App - Table of Content

- [Overview](#overview)
- [Authentication](#authentication)
- [Permissions](#permissions)
- [Making API Class](#making-api-class)
- [Models](#models)
- [REST API](#rest-api)
- [Postman Collections API](#postman-collections)


# Overview

This app provides simple API account, which requires no user account registration and can be provided for API
consumption. You can use this feature if you want to provide read only API access, therefore Simple API account only
supports `GET` requests.


# Authentication

Authentication for simple API account is provided by `simpleAPIAccount.authentications.SimpleAPIAccountAuthentication`
class and you must explicitly use it in the view that you want to provide simple API account authentication for.


# Permissions

Provided permission `simpleAPIAccount.permissions.SimpleAPIAccountPermission` class checks whether the HTTP method is
`GET`, if so it permits the action otherwise it rejects it.


# Making API Class

When you create an instance of `simpleAPIAccount.models.SimpleAPIAccount` class a token accociated with it also created
and saved in the instance. You can provide this token to API users. Also you can set an expiration date.

Making calls to endpoints with the simple API account token as same as token based authentication. It can be done like
so; 

```shell script
curl --location --request GET '<HOST>/api/v1/privacy-notices/' \
     --header 'Authorization: token 05b65f04f0d4dd7757404ee576ba88e661007276'
```


# Models

| Name                                          | Description                                                           |
| :-------------------------------------------- | :-------------------------------------------------------------------- |
| `simpleAPIAccount.models.SimpleAPIAccount`    | SimpleAPIAccount                                                      |


# REST API

[Please visit documentation of REST API for detailed information](REST_API.md)

| Models & Endpoints                    | HTTP Methods         | View                                                   |
| :------------------------------------ | :------------------- | :----------------------------------------------------- |
| **SimpleAPIAccount**                  |                      |                                                        |
| `api/v1/simple-api-accounts/`         | GET, POST            | `simpleAPIAccount.views.SimpleAPIAccountCollectionView`|
| `api/v1/simple-api-accounts/1/`       | GET, PUT, DELETE     | `simpleAPIAccount.views.SimpleAPIAccountDetailView`    |


# Postman Collections

Please check `simpleAPIAccount/data/postman` for `Postman` collections.