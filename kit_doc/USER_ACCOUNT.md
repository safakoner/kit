# User Account App - Table of Content

- [Overview](#overview)
- [Models](#models)
- [REST API](#rest-api)
- [Postman Collections API](#postman-collections)


# Overview

This app provides user model with email based authentication. 


# Models

| Name                                          | Description                                                           |
| :-------------------------------------------- | :-------------------------------------------------------------------- |
| `userAccount.models.UserAccount`              | UserAccount                                                           |


# REST API

[Please visit documentation of REST API for detailed information](REST_API.md)

Two sets of API endpoints provided in this app. `api/v1/admin/user-accounts/` and `api/v1/admin/user-accounts/1/`
endpoints are meant to be used only by super users, who can create, get, edit and delete user accounts. 

`api/v1/user-accounts/` and `api/v1/user-accounts/api-token-auth/` endpoints on the other hand is designed to be used
by valid and active users. Users who use these endpoints neither have permissions to create, delete user accounts
nor do they have permission to edit any other user account apart from theirs. 


| Models & Endpoints                    | HTTP Methods         | View                                                       |
| :------------------------------------ | :------------------- | :--------------------------------------------------------- |
| **UserAccount**                       |                      |                                                            |
| `api/v1/admin/user-accounts/`         | GET, POST            | `userAccount.views.UserAccountSuperUserCollectionAPIView`  |
| `api/v1/admin/user-accounts/1/`       | GET, PUT, DELETE     | `userAccount.views.UserAccountSuperUserDetailAPIView`      |
|                                       |                      |                                                       <br/>|
| **UserAccount**                       |                      |                                                            |
| `api/v1/user-accounts/`               | GET, PATCH           | `userAccount.views.UserAccountDetailAPIView`               |
| `api/v1/user-accounts/api-token-auth/`| POST                 | `userAccount.views.UserAccountTokenAuthDetailAPIView`      |


# Postman Collections

Please check `userAccount/data/postman` for `Postman` collections.