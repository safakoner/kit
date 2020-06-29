# Conversion App - Table of Content

- [Overview](#overview)
- [Example](#example)
- [Models](#models)
- [Web URLs](#web-urls)
- [REST API](#rest-api)
- [Postman Collections API](#postman-collections)
- [See Also](#see-also)


# Overview

This app provides conversion model along with built-in web page for conversion. Once you create a
`conversion.models.Conversion` model instance you can visit its page via the following URL pattern.

```
<HOST>/conversion/<CONVERSION_SLUG>
```

Where `<CONVERSION_SLUG>` is `conversion.models.Conversion.url_id` of the model. App uses `conversion.models.Subscriber`
class as subscriber model if any visitor subscribes to the conversion page. Please check [See Also](#see-also) for more
information on conversion and `The Lean Startup`.

# Example

Default conversion page would look like this one, which you can customize.

<img src="img/conversion.png" width="900">


# Models

| Name                                          | Description                                                           |
| :-------------------------------------------- | :-------------------------------------------------------------------- |
| `conversion.models.Subscriber`                | Subscriber of conversion models                                       |
| `conversion.models.Conversion`                | Conversion model for conversion pages                                 |


# Web URLs

| Models & URL                                              |  View                                                     |
| :-------------------------------------------------------- | :-------------------------------------------------------- |
| **Conversion**                                            |                                                           |
| `conversion/<slug:slug>/`                                 | `conversion.views.renderConversion`                       |
|                                                           |                                                      <br/>|
| **Subscriber**                                            |                                                           |
| `conversion/<slug:slug>/subscribe/<uuid:subscriberID>/`   | `conversion.views.renderSubscribeByID`                    |
| `conversion/<slug:slug>/unsubscribe/<uuid:subscriberID>/` | `conversion.views.renderUnsubscribeByID`                  |


# REST API

[Please visit documentation of REST API for detailed information](REST_API.md)

| Models & Endpoints                    | HTTP Methods         | View                                                   |
| :------------------------------------ | :------------------- | :----------------------------------------------------- |
| **Conversion**                        |                      |                                                        |
| `api/v1/conversions/`                 | GET, POST            | `conversion.views.ConversionCollectionView`            |
| `api/v1/conversions/1/`               | GET, PUT, DELETE     | `conversion.views.ConversionDetailView`                |


# Postman Collections

Please check `conversion/data/postman` for `Postman` collections.


# See Also
- The Lean Startup: How Today's Entrepreneurs Use Continuous Innovation to Create Radically Successful Businesses by Eric Ries


