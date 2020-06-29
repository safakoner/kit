# Language App - Table of Content

- [Overview](#overview)
- [Models](#models)
- [REST API](#rest-api)
- [Postman Collections API](#postman-collections)


# Overview

This app provides models to set languages for available content.


# Models

| Name                                          | Description                                                           |
| :-------------------------------------------- | :-------------------------------------------------------------------- |
| `language.models.Language`                    | Language                                                              |

The model `language.models.Language` is used by foreign keys in other models to determine the language they are created
for.


# REST API

[Please visit documentation of REST API for detailed information](REST_API.md)

| Models & Endpoints                    | HTTP Methods         | View                                                   |
| :------------------------------------ | :------------------- | :----------------------------------------------------- |
| **Language**                          |                      |                                                        |
| `api/v1/languages/`                   | GET, POST            | `language.views.LanguageCollectionView`                |
| `api/v1/languages/1/`                 | GET, PUT, DELETE     | `language.views.LanguageDetailView`                    |


# Postman Collections

Please check `language/data/postman` for `Postman` collections.