# Testimonial App - Table of Content

- [Overview](#overview)
- [Models](#models)
- [REST API](#rest-api)
- [Postman Collections API](#postman-collections)


# Overview

This app provides models to have testimonials.


# Models

| Name                                          | Description                                                           |
| :-------------------------------------------- | :-------------------------------------------------------------------- |
| `testimonial.models.Testimonial`              | Testimonial                                                           |


# REST API

[Please visit documentation of REST API for detailed information](REST_API.md)

| Models & Endpoints                    | HTTP Methods         | View                                                   |
| :------------------------------------ | :------------------- | :----------------------------------------------------- |
| **Testimonial**                       |                      |                                                        |
| `api/v1/testimonials/`                | GET, POST            | `testimonial.views.TestimonialCollectionView`          |
| `api/v1/testimonials/1/`              | GET, PUT, DELETE     | `testimonial.views.TestimonialDetailView`              |


# Postman Collections

Please check `testimonial/data/postman` for `Postman` collections.