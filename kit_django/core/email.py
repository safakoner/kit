#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
import re

from   django.conf                      import settings
from   django.core.mail                 import EmailMessage
from   django.core.mail.backends.smtp   import EmailBackend

from   projectSettings.common           import IS_IN_PRODUCTION


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief Build email str.
#
#  @param emailTemplate [ dict | None | in  ] - Email template dict instance.
#  @param replace       [ dict | None | in  ] - Replace dict instance.
#
#  @exception N/A
#
#  @return dict - Edited template.
def buildEmailAsStr(emailTemplate, replace):

    template = emailTemplate.copy()

    for tKey, tValue in template.items():

        if not tKey in replace:
            continue

        for rKey, rValue in replace[tKey].items():
            template[tKey] = re.sub(r'{{\s*' + rKey + '+\s*}}', rValue, template[tKey])

    return template

#
## @brief Send simple email.
#
#  @param fromEmail   [ str                                         | None | in  ] - From email address.
#  @param toEmail     [ str, list of str                            | None | in  ] - To email addresses.
#  @param subject     [ str                                         | None | in  ] - Subject.
#  @param body        [ str                                         | None | in  ] - Body.
#  @param backend     [ django.core.mail.backends.smtp.EmailBackend | None | in  ] - Email backend.
#  @param bcc         [ list of str                                 | None | in  ] - BCC email addresses.
#  @param attachments [ list of str                                 | None | in  ] - Absolute path of attachment files.
#
#  @exception N/A
#
#  @return None - None.
def sendSimpleEmail(fromEmail, toEmail, subject, body, backend=None, bcc=[], attachments=[]):

    if isinstance(toEmail, str):
        toEmail = [toEmail]

    if not IS_IN_PRODUCTION:

        print('\nSEND SIMPLE EMAIL\n')
        print('\nfromEmail')
        print(fromEmail)
        print('\ntoEmail')
        print(toEmail)
        print('\nsubject')
        print(subject)
        print('\nbody')
        print(body)
        print('\nbcc')
        print(bcc)
        print('\nbackend')
        print(backend)
        print('\nattachments')
        print(attachments)

    if not backend:
        backend = EmailBackend(host=settings.EMAIL_HOST,
                               port=settings.EMAIL_PORT,
                               username=settings.EMAIL_HOST_USER,
                               password=settings.EMAIL_HOST_PASSWORD,
                               use_tls=settings.EMAIL_USE_TLS,
                               fail_silently=False)

    email = EmailMessage(subject=subject,
                         body=body,
                         from_email=fromEmail,
                         to=toEmail,
                         bcc=bcc,
                         connection=backend)

    if attachments:
        for a in attachments:
            email.attach_file(a)

    email.send()
