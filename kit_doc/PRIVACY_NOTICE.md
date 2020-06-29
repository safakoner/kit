# Privacy Notice App - Table of Content

- [Overview](#overview)
- [Models](#models)
- [REST API](#rest-api)
- [Postman Collections API](#postman-collections)


# Overview

This app provides models to provide privacy notices to visitors.


# Models

| Name                                          | Description                                                           |
| :-------------------------------------------- | :-------------------------------------------------------------------- |
| `privacyNotice.models.PrivacyNotice`          | Privacy notice                                                        |


# REST API

[Please visit documentation of REST API for detailed information](REST_API.md)

| Models & Endpoints                    | HTTP Methods         | View                                                   |
| :------------------------------------ | :------------------- | :----------------------------------------------------- |
| **PrivacyNotice**                     |                      |                                                        |
| `api/v1/privacy-notices/`             | GET, POST            | `privacyNotice.views.PrivacyNoticeCollectionView`      |
| `api/v1/privacy-notices/1/`           | GET, PUT, DELETE     | `privacyNotice.views.PrivacyNoticeDetailView`          |


# Postman Collections

Please check `privacyNotice/data/postman` for `Postman` collections.