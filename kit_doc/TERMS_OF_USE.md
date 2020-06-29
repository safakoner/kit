# Terms of Use App - Table of Content

- [Overview](#overview)
- [Models](#models)
- [REST API](#rest-api)
- [Postman Collections API](#postman-collections)


# Overview

This app provides models to provide terms of use to visitors.


# Models

| Name                                          | Description                                                           |
| :-------------------------------------------- | :-------------------------------------------------------------------- |
| `termsOfUse.models.TermsOfUse`                | Terms of use                                                          |


# REST API

[Please visit documentation of REST API for detailed information](REST_API.md)

| Models & Endpoints                    | HTTP Methods         | View                                                   |
| :------------------------------------ | :------------------- | :----------------------------------------------------- |
| **TermsOfUse**                        |                      |                                                        |
| `api/v1/terms-of-uses/`               | GET, POST            | `termsOfUse.views.TermsOfUseCollectionView`            |
| `api/v1/terms-of-uses/1/`             | GET, PUT, DELETE     | `termsOfUse.views.TermsOfUseDetailView`                |


# Postman Collections

Please check `termsOfUse/data/postman` for `Postman` collections.