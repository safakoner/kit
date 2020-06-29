#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from django.shortcuts                       import render
from django.template.context_processors     import csrf
from django.http                            import Http404
from django.middleware.csrf                 import rotate_token

from restAPICore.views                      import SimpleCollectionAPIView, SimpleDetailAPIView

from conversion.forms                       import SubscriberForm
from conversion.models                      import Conversion, Subscriber
from conversion.serializers                 import ConversionSerializer
from conversion.notifications               import sendSubscribeEmail


#
# ----------------------------------------------------------------------------------------------------
# API VIEWS
# ----------------------------------------------------------------------------------------------------
#
## @brief [ REST FRAMEWORK API VIEW CLASS ] - REST framework API view class.
class ConversionCollectionView(SimpleCollectionAPIView):

    ## [ tuple ] - Authentication classes.
    # authentication_classes  = ()

    ## [ tuple ] - Permission classes.
    # permission_classes      = ()

    ## [ django.db.models.Model ] - Model class object.
    MODEL_CLASS             = Conversion

    ## [ rest_framework.serializers.ModelSerializer ] - REST framework model serializer class object.
    MODEL_CLASS_SERIALIZER  = ConversionSerializer

#
## @brief [ REST FRAMEWORK API VIEW CLASS ] - REST framework API view class.
class ConversionDetailView(SimpleDetailAPIView):

    ## [ tuple ] - Authentication classes.
    # authentication_classes  = ()

    ## [ tuple ] - Permission classes.
    # permission_classes      = ()

    ## [ django.db.models.Model ] - Model class object.
    MODEL_CLASS             = Conversion

    ## [ rest_framework.serializers.ModelSerializer ] - REST framework model serializer class object.
    MODEL_CLASS_SERIALIZER  = ConversionSerializer

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
#  @param slug    [ str                                   | None | in  ] - Slug.
#
#  @exception N/A
#
#  @return django.http.response.HttpResponse - Response.
def renderConversion(request, slug):

    # print(request.sessionLanguageCode)
    # print(request.languageCode)

    conversion = None
    try:
        conversion = Conversion.objects.get(is_active=True,
                                            url_id=slug)
    except Conversion.DoesNotExist:
        raise Http404

    #

    context = {'conversion':conversion}

    if request.method == 'POST':

        form = SubscriberForm(request.POST, **{'request':request})
        if form.is_valid():

            try:
                subscriber = Subscriber.objects.get(email=form.cleaned_data['email'])

                if form.cleaned_data['name']:
                    subscriber.name = form.cleaned_data['name']

                if form.cleaned_data['willing_to_pay']:
                    subscriber.willing_to_pay = form.cleaned_data['willing_to_pay']

                subscriber.save()

                context['subscriber'] = subscriber
                conversion.addSubscriber(subscriber)

            except Subscriber.DoesNotExist as error:

                context['subscriber'] = form.save()
                conversion.addSubscriber(context['subscriber'])

            sendSubscribeEmail(conversion, context['subscriber'])

            return render(request,
                          template_name='conversion/conversion-subscribed-result-rnd.html',
                          context=context)

        else:
            context['form'] = SubscriberForm(request.POST, **{'request':request})

    else:

        rotate_token(request)

        conversion.addVisitor()

        context['form'] = SubscriberForm(**{'request':request})
        context.update(csrf(request))

    return render(request,
                  template_name='conversion/conversion-rnd.html',
                  context=context)

#
## @brief View function.
#
#  @param request       [ django.core.handlers.wsgi.WSGIRequest | None | in  ] - Request.
#  @param slug          [ str                                   | None | in  ] - Slug.
#  @param subscriberID  [ str                                   | None | in  ] - Subscriber ID.
#
#  @exception N/A
#
#  @return django.http.response.HttpResponse - Response.
def renderSubscribeByID(request, slug, subscriberID):

    conversion = None
    try:
        conversion = Conversion.objects.get(is_active=True,
                                         url_id=slug)
    except Conversion.DoesNotExist:
        raise Http404

    subscriber = None
    try:
        subscriber = Subscriber.objects.get(is_active=True,
                                            subscriber_id=subscriberID)
    except Subscriber.DoesNotExist:
        raise Http404

    conversion.addSubscriber(subscriber)

    context = {'conversion':conversion,
               'subscriber':subscriber}

    return render(request,
                  template_name='conversion/conversion-subscribe-by-uuid-rnd.html',
                  context=context)

#
## @brief View function.
#
#  @param request       [ django.core.handlers.wsgi.WSGIRequest | None | in  ] - Request.
#  @param slug          [ str                                   | None | in  ] - Slug.
#  @param subscriberID  [ str                                   | None | in  ] - Subscriber ID.
#
#  @exception N/A
#
#  @return django.http.response.HttpResponse - Response.
def renderUnsubscribeByID(request, slug, subscriberID):

    conversion = None
    try:
        conversion = Conversion.objects.get(is_active=True,
                                         url_id=slug)
    except Conversion.DoesNotExist:
        raise Http404

    subscriber = None
    try:
        subscriber = Subscriber.objects.get(is_active=True,
                                            subscriber_id=subscriberID)
    except Subscriber.DoesNotExist:
        raise Http404

    # if not conversion.hasSubscriber(subscriber):
    #     raise Http404

    conversion.removeSubscriber(subscriber)

    context = {'conversion':conversion,
               'subscriber':subscriber}

    return render(request,
                  template_name='conversion/conversion-unsubscribe-by-uuid-rnd.html',
                  context=context)