#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from core.email             import sendSimpleEmail

from projectSettings.common import IS_IN_PRODUCTION, BASE_URL, DEFAULT_FROM_EMAIL


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief Send subscribe email to subscriber.
#
#  @param conversion [ conversion.models.Conversion | None | in  ] - Django model class instance.
#  @param subscriber [ conversion.models.Subscriber | None | in  ] - Django model class instance.
#
#  @exception N/A
#
#  @return None - None.
def sendSubscribeEmail(conversion, subscriber):

    subject = '{} Subscription'.format(conversion.label)

    body = '\nHello {}!\n'.format(subscriber.name if subscriber.name else subscriber.email)
    body = '{}\nThanks for signing up. We\'ll keep you updated by contacting you at {}.\n\n'.format(body, subscriber.email)

    body = '{}You can unsubscribe any time by visiting the following link\n'.format(body)
    body = '{}{}conversion/{}/unsubscribe/{}/\n\n'.format(body, BASE_URL, conversion.url_id, subscriber.subscriber_id)

    if not IS_IN_PRODUCTION:

        print('\nsubject')
        print(subject)
        print('\nbody')
        print(body)

    sendSimpleEmail(DEFAULT_FROM_EMAIL,
                    subscriber.email,
                    subject,
                    body)
