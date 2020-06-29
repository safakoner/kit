# Common Static App - Table of Content

- [Overview](#overview)
- [Using Common Static Files](#using-common-static-files)
- [See Also API](#see-also)


# Overview

This app contains common static files such as sass, css, JavaScript files and libraries.

Please check `commonStatic/static/common-static` folder for available content.


# Using Common Static Files

You can add commonly used static files under relevant folder in `commonStatic/static/common-static`
folder and use it in the templates like so;

```html
{% load static %}

<script src="{% static "common-static/libs/jquery/3.5.1/jquery-3.5.1.min.js" %}"></script>
```

Please do not forget to run `python manage.py collectstatic` command. In order to ignore built-in `.sass`
files, which are not needed for production, you may want to use the command with `-i` flag like so;
`python manage.py collectstatic -i *.sass`


# See Also
- [collectstatic](https://docs.djangoproject.com/en/3.0/ref/contrib/staticfiles/#collectstatic)


