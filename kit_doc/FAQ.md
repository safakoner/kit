# Frequently Asked Questions App - Table of Content

- [Overview](#overview)
- [Models](#models)
- [REST API](#rest-api)
- [Postman Collections API](#postman-collections)


# Overview

This app provides models and functionalities so you can use them to provide frequently asked questions.


# Models

| Name                                          | Description                                                           |
| :-------------------------------------------- | :-------------------------------------------------------------------- |
| `faq.models.FAQ`                              | Frequently Asked Questions                                            |


# REST API

[Please visit documentation of REST API for detailed information](REST_API.md)

| Models & Endpoints                    | HTTP Methods         | View                                                   |
| :------------------------------------ | :------------------- | :----------------------------------------------------- |
| **FAQ**                               |                      |                                                        |
| `api/v1/faqs/`                        | GET, POST            | `faq.views.FAQCollectionView`                          |
| `api/v1/faqs/1/`                      | GET, PUT, DELETE     | `faq.views.FAQDetailView`                              |


# Postman Collections

Please check `faq/data/postman` for `Postman` collections.