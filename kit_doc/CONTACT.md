# Contact App - Table of Content

- [Overview](#overview)
- [Models](#models)
- [REST API](#rest-api)
- [Postman Collections API](#postman-collections)


# Overview

This app provides models so you can use them to store contact information, including the information
send form visitors via forms, such as contact form.


# Models

| Name                                          | Description                                           |
| :-------------------------------------------- | :---------------------------------------------------- |
| `contact.models.Address`                      | Store addresses                                       |
| `contact.models.Contact`                      | Model to store contact information send by visitors   |
| `contact.models.Email`                        | Store emails                                          |
| `contact.models.Phone`                        | Store phones                                          |
| `contact.models.SocialMedia`                  | Store social media information                        |


# REST API

[Please visit documentation of REST API for detailed information](REST_API.md)

| Models & Endpoints                    | HTTP Methods         | View                                                   |
| :------------------------------------ | :------------------- | :----------------------------------------------------- |
| **Address**                           |                      |                                                        |
| `api/v1/addresses/`                   | GET, POST            | `contact.views.AddressCollectionView`                  |
| `api/v1/addresses/1/`                 | GET, PUT, DELETE     | `contact.views.AddressDetailView`                      |
|                                       |                      |                                                   <br/>|
| **Contact**                           |                      |                                                        |
| `api/v1/emails/`                      | GET, POST            | `contact.views.EmailCollectionView`                    |
| `api/v1/emails/1/`                    | GET, PUT, DELETE     | `contact.views.EmailDetailView`                        |
|                                       |                      |                                                   <br/>|
| **Email**                             |                      |                                                        |
| `api/v1/emails/`                      | GET, POST            | `contact.views.EmailCollectionView`                    |
| `api/v1/emails/1/`                    | GET, PUT, DELETE     | `contact.views.EmailDetailView`                        |
|                                       |                      |                                                   <br/>|
| **Phone**                             |                      |                                                        |
| `api/v1/phones/`                      | GET, POST            | `contact.views.PhoneCollectionView`                    |
| `api/v1/phones/1/`                    | GET, PUT, DELETE     | `contact.views.PhoneDetailView`                        |
|                                       |                      |                                                   <br/>|
| **Social Media**                      |                      |                                                        |
| `api/v1/social-medias/`               | GET, POST            | `contact.views.SocialMediaCollectionView`              |
| `api/v1/social-medias/1/`             | GET, PUT, DELETE     | `contact.views.SocialMediaDetailView`                  |


# Postman Collections

Please check `contact/data/postman` for `Postman` collections.