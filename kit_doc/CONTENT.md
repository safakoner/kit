# Content App - Table of Content

- [Overview](#overview)
- [Models](#models)
- [REST API](#rest-api)
- [Postman Collections API](#postman-collections)


# Overview

This app provides models so you can use them to provide content for several purposes.


# Models

| Name                                          | Description                                                           |
| :-------------------------------------------- | :-------------------------------------------------------------------- |
| `content.models.ContentType`                    | Content types, determines the type of `Content` and `Item`            |
| `content.models.Content`                        | Content, model to provide content body                                |
| `content.models.Item`                           | Item, model to provide highlight items like features, benefits, etc.  |


# REST API

[Please visit documentation of REST API for detailed information](REST_API.md)

| Models & Endpoints                    | HTTP Methods         | View                                                   |
| :------------------------------------ | :------------------- | :----------------------------------------------------- |
| **ContentType**                       |                      |                                                        |
| `api/v1/content-types/`               | GET, POST            | `content.views.ContentTypeCollectionView`              |
| `api/v1/content-types/1/`             | GET, PUT, DELETE     | `content.views.ContentTypeDetailView`                  |
|                                       |                      |                                                   <br/>|
| **Content**                           |                      |                                                        |
| `api/v1/contents/`                    | GET, POST            | `content.views.ContentCollectionView`                  |
| `api/v1/contents/1/`                  | GET, PUT, DELETE     | `content.views.ContentDetailView`                      |
|                                       |                      |                                                   <br/>|
| **Item**                              |                      |                                                        |
| `api/v1/items/`                       | GET, POST            | `content.views.ItemCollectionView`                     |
| `api/v1/items/1/`                     | GET, PUT, DELETE     | `content.views.ItemDetailView`                         |


# Postman Collections

Please check `content/data/postman` for `Postman` collections.