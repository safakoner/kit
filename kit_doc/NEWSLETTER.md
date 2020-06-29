# Newsletter App - Table of Content

- [Overview](#overview)
- [Models](#models)
- [REST API](#rest-api)
- [Postman Collections API](#postman-collections)


# Overview

This app provides models to have newsletter subscribers.


# Models

| Name                                          | Description                                                           |
| :-------------------------------------------- | :-------------------------------------------------------------------- |
| `newsletter.models.Newsletter`                | Newsletter                                                            |


# REST API

[Please visit documentation of REST API for detailed information](REST_API.md)

| Models & Endpoints                    | HTTP Methods         | View                                                   |
| :------------------------------------ | :------------------- | :----------------------------------------------------- |
| **Newsletter**                        |                      |                                                        |
| `api/v1/newsletters/`                 | GET, POST            | `newsletter.views.NewsletterCollectionView`            |
| `api/v1/newsletters/1/`               | GET, PUT, DELETE     | `newsletter.views.NewsletterDetailView`                |


# Postman Collections

Please check `newsletter/data/postman` for `Postman` collections.