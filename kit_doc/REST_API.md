# REST API - Table of Content

- [Overview](#overview)
- [Authentication](#authentication)
- [Permissions](#permissions)
- [Making API Calls](#making-api-calls)
- [Endpoints](#endpoints)
- [Postman Collections](#postman-collections)
- [See Also](#see-also)


# Overview

All models in this project come with built-in REST API implementation. The following documentation will provide essential
information how you can use REST API.


# Authentication

Authentication is provided by `userAccount.authentications.UserAccountAuthentication` class, which you can customize 
further based on your needs. This class inherits `rest_framework.authentication.BaseAuthentication` class as you can
guess and it uses hijacked token authentication, meaning that any user authenticated via token "can" operate on all the
models. 

| Authentication Classes                                    | Description                       |
| :-------------------------------------------------------- | :-------------------------------- |
| `userAccount.authentications.UserAccountAuthentication`   | User authentication               |


# Permissions

Any active super user authenticated by token can operate on any models provided by the project. Super user permission
will be checked by `userAccount.permissions.UserAccountSuperUserPermission` class. 

If you need to give permissions to non-super user you can use `userAccount.permissions.UserAccountPermission` class,
which I provided. Though this class is not currently used anywhere in the project and you can customize and use it as
you need.  

| Permission Classes                                        | Description                                       |
| :-------------------------------------------------------- | :------------------------------------------------ |
| `userAccount.permissions.UserAccountSuperUserPermission`  | Checks whether user has super user permission     |
| `userAccount.permissions.UserAccountPermission`           | Checks whether user has permission                |


# Making API Calls

Current REST API implementation uses simple token authentication, which you can start using right away. A token is
created (`rest_framework.authtoken.models.Token`) for every user when a user account is created.

In order to obtain the token for a user `api/v1/user-accounts/api-token-auth/` end point can be used, like so;

```shell script
curl --location --request POST '<HOST>/api/v1/user-accounts/api-token-auth/' \
     --form 'email=name@domain.com' \
     --form 'password=<PASSWORD>'
```

The result upon successful call would look like;

```json
{
    "id": 1,
    "api_token": {
        "key": "05b65f04f0d4dd7757404ee576ba88e661007276",
        "user": 1
    },
    "email": "name@domain.com",
    "first_name": "",
    "last_name": "",
    "avatar": null,
    "folder_name": "irlyycxrs7uqmoslvilepw",
    "last_login": "2020-06-27T14:54:09.572468-07:00",
    "registration_date_time": "2020-06-24T22:56:32.560903-07:00",
    "has_account_been_verified": true
}
```

Now we can use the token for out API calls, like so;

```shell script
curl --location --request GET '<HOST>/api/v1/privacy-notices/' \
     --header 'Authorization: token 05b65f04f0d4dd7757404ee576ba88e661007276'
```


# Endpoints

REST API endpoints for every app(where applicable) can be found app's documentation in this section of the repository.


# Postman Collections

Each REST API endpoint has Postman collection and request examples associated with the app and they can be found in
`<APP_NAME>/data/postman` folder.


# See Also
- [django-rest-framework](https://www.django-rest-framework.org/)
- [django-rest-framework authentication](https://www.django-rest-framework.org/api-guide/authentication/)
- [django-rest-framework permissions](https://www.django-rest-framework.org/api-guide/permissions/)




