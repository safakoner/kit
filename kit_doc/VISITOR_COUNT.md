# Visitor Count App - Table of Content

- [Overview](#overview)
- [Models](#models)
- [REST API](#rest-api)
- [Postman Collections API](#postman-collections)


# Overview

This app provides model and functionalities to keep track of visitor counts. The following URLs will be ignored.

- Admin URLs
- Static URLs
- Media URLs
- REST API URLs
- Any file URL


# Models

| Name                                          | Description                                                           |
| :-------------------------------------------- | :-------------------------------------------------------------------- |
| `visitorCount.models.VisitorCount`            | Visitor count                                                         |


# REST API

[Please visit documentation of REST API for detailed information](REST_API.md)

| Models & Endpoints                    | HTTP Methods         | View                                                   |
| :------------------------------------ | :------------------- | :----------------------------------------------------- |
| **VisitorCount**                      |                      |                                                        |
| `api/v1/visitor-count/`               | GET                  | `testimonial.views.VisitorCountCollectionView`         |
| `api/v1/visitor-count/1/`             | GET                  | `testimonial.views.VisitorCountDetailView`             |


# Postman Collections

Please check `visitorCount/data/postman` for `Postman` collections.