# REST API Core - Table of Content

- [Overview](#overview)
- [Serializers](#serializers)
- [Views](#views)


# Overview

This app provides core functionalities for REST API implementation.


# Serializers

| Name                                          | Description                                                           |
| :-------------------------------------------- | :-------------------------------------------------------------------- |
| `restAPICore.serializers.ModelSerializer`     | Abstract serializer class with dynamic field feature                  |

All serializers in this project uses this abstract serializer.


# Views

| Name                                          | Description                                                           |
| :-------------------------------------------- | :-------------------------------------------------------------------- |
| `restAPICore.views.SimpleCollectionAPIView`   | Abstract view for collection view, supports GET, POST methods         |
| `restAPICore.views.SimpleDetailAPIView`       | Abstract view for detail view, supports GET, PATCH, DELETE methods    |

All API views uses the relevant view provided in this app.
