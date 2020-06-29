#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from django.core.mail.backends.smtp import EmailBackend
from django.conf                    import settings


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
## [ django.core.mail.backends.smtp.EmailBackend ] - Email backend to be used to send emails for this app.
BACKEND = EmailBackend(host=settings.EMAIL_HOST,
                       port=settings.EMAIL_PORT,
                       username=settings.EMAIL_HOST_USER,
                       password=settings.EMAIL_HOST_PASSWORD,
                       use_tls=settings.EMAIL_USE_TLS,
                       fail_silently=False)

## [ str ] - Email template to be used for contacts.
CONTACT_EMAIL_TEMPLATE = {'fromEmail':'',
                          'subject'  :'We\'ve received your message!',
                          'backend'  :BACKEND,
                          'bcc'      :[],
                          'body'     : '''
Hello {{NAME}},

Thank you for contacting us. We'll be in touch with you shortly.

Your message:

Name        : {{NAME}}

E-mail      : {{EMAIL}}

Subject     : {{SUBJECT}}

Message     :

{{MESSAGE}}

'''
                         }

## [ dict ] - Email template to be used for newsletter subscribers.
NEWSLETTER_EMAIL_TEMPLATE = {'fromEmail':'',
                             'subject'  :'Newsletter Subscription',
                             'backend'  :BACKEND,
                             'bcc'      :[],
                             'body'     : '''
Hello {{NAME}},

It's good to have you, thank you for subscribing.

'''
                            }