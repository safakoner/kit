#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from django.test    import TestCase

from core.tests     import getOrCreateContextAndLanguageObjects
from testimonial    import models


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
TESTIMONIALS = [
    {
        "is_active"         : True,
        "note"              : "",
        "context"           : "djangokit",
        "language"          : "en-us",
        "code"              : "",
        "order"             : 1,
        "name"              : "Alexandre Dumas",
        "job_title"         : "CTO",
        "company"           : "Monte Cristo",
        "body"              : "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using, making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).",
        "url"               : "http://www.safakoner.com/",
        "avatar"            : None
    },
    {
        "is_active"         : True,
        "note"              : "",
        "context"           : "djangokit",
        "language"          : "en-us",
        "code"              : "",
        "order"             : 2,
        "name"              : "Jules Verne",
        "job_title"         : "CEO",
        "company"           : "Thousand Leagues",
        "body"              : "On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying.",
        "url"               : "http://www.safakoner.com/",
        "avatar"            : None
    }

]

class TestimonialTest(TestCase):

    def setUp(self):

        context, language = getOrCreateContextAndLanguageObjects()

        for data in TESTIMONIALS:

            if 'context' in data:
                data['context']  = context

            if 'language' in data:
                data['language'] = language

            models.Testimonial.objects.create(**data)

    def test_testimonial(self):

        modelInstance = models.Testimonial.objects.get(name=TESTIMONIALS[0]['name'])
        self.assertEqual(modelInstance.job_title, TESTIMONIALS[0]['job_title'])
        self.assertEqual(modelInstance.company, TESTIMONIALS[0]['company'])

