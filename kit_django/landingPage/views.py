#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from django.shortcuts                       import render
from django.http                            import Http404
from django.template.context_processors     import csrf
from django.middleware.csrf                 import rotate_token

from core.email                             import buildEmailAsStr, sendSimpleEmail
from contact.forms                          import ContactForm
from context.models                         import Context
from newsletter.forms                       import NewsletterForm
from landingPage                            import email

#
#
#
# ----------------------------------------------------------------------------------------------------
# VIEWS
# ----------------------------------------------------------------------------------------------------
#
## @brief View function.
#
#  @param request [ django.core.handlers.wsgi.WSGIRequest | None | in  ] - Request.
#
#  @exception N/A
#
#  @return django.http.response.HttpResponse - Response.
def renderLandingPage(request):

    contextDomain   = 'kit'
    languageCode    = 'en-us'

    data = None
    try:
        data = Context.getProcessedContextDataWithDependencies(contextDomain, languageCode)
    except Exception as error:
        raise Http404

    contactForm     = None
    newsletterForm  = None

    formContext = {'request'        :request,
                   'contextDomain'  :contextDomain,
                   'languageCode'   :languageCode
                   }

    context     = {'contextDomain'  :contextDomain,
                   'contactForm'    :contactForm,
                   'newsletterForm' :newsletterForm,
                   'data'           :data,
                   'anchor'         : ''
                   }

    if request.method == 'POST':

        if 'company' in request.POST and 'subject' in request.POST:
            # This is contact form
            contactForm = ContactForm(request.POST, **formContext)
            if contactForm.is_valid():
                contactInstance = contactForm.addContact()

                emailDict = buildEmailAsStr(email.CONTACT_EMAIL_TEMPLATE,
                                            {'body':{'NAME':contactInstance.name if contactInstance.name else contactInstance.email,
                                                     'EMAIL':contactInstance.email,
                                                     'SUBJECT':contactInstance.subject,
                                                     'MESSAGE':contactInstance.message
                                                     }
                                             }
                                            )

                sendSimpleEmail(emailDict['fromEmail'],
                                contactInstance.email,
                                emailDict['subject'],
                                emailDict['body'],
                                emailDict['backend'],
                                emailDict['bcc']
                                )

                context = {'contactInstance':contactInstance,
                           'context'        :data['context']}

                return render(request,
                              template_name='landing-page/landing-page-contact-success-rnd.html',
                              context=context)

            else:
                context['contactForm']    = ContactForm(request.POST, **formContext)
                context['newsletterForm'] = NewsletterForm(**formContext)
                context['anchor']         = 'Contact'

        else:
            # This is newsletter form
            newsletterForm = NewsletterForm(request.POST, **formContext)
            if newsletterForm.is_valid():
                newsletterInstance = newsletterForm.addSubscriber()

                emailDict = buildEmailAsStr(email.NEWSLETTER_EMAIL_TEMPLATE,
                                            {'body':{'NAME':newsletterInstance.name if newsletterInstance.name else newsletterInstance.email}}
                                            )

                sendSimpleEmail(emailDict['fromEmail'],
                                newsletterInstance.email,
                                emailDict['subject'],
                                emailDict['body'],
                                emailDict['backend'],
                                emailDict['bcc']
                                )

                context = {'newsletterInstance':newsletterInstance,
                           'context'           :data['context']}

                return render(request,
                              template_name='landing-page/landing-page-newsletter-success-rnd.html',
                              context=context)

            else:
                context['contactForm']    = ContactForm(**formContext)
                context['newsletterForm'] = NewsletterForm(request.POST, **formContext)
                context['anchor']         = 'Newsletter'

    else:
        rotate_token(request)

        context['contactForm']    = ContactForm(**formContext)
        context['newsletterForm'] = NewsletterForm(**formContext)

    context.update(csrf(request))

    return render(request,
                  template_name='landing-page/landing-page-rnd.html',
                  context=context)