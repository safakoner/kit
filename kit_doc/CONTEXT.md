# Context App - Table of Content

- [Overview](#overview)
- [Models](#models)
- [REST API](#rest-api)
- [Postman Collections API](#postman-collections)


# Overview

This app provides context for other models, meaning that you can use `context.models.Context` model to determine what
other models belong to. By utilizing context, you can serve multiple services (websites, domains) in same Django project
while consuming less server resources.


# Models

| Name                                          | Description                                                           |
| :-------------------------------------------- | :-------------------------------------------------------------------- |
| `context.models.Context`                      | Context model, which can be used for most of the models               |


# REST API

[Please visit documentation of REST API for detailed information](REST_API.md)

| Models & Endpoints                    | HTTP Methods         | View                                                   |
| :------------------------------------ | :------------------- | :----------------------------------------------------- |
| **Context**                           |                      |                                                        |
| `api/v1/contexts/`                    | GET, POST            | `context.views.ContextCollectionView`                  |
| `api/v1/contexts/1/`                  | GET, PUT, DELETE     | `context.views.ContextDetailView`                      |


# Postman Collections

Please check `context/data/postman` for `Postman` collections.