#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from    django.db                   import models

from    core.models                 import Model
from    core.randomValue            import createRandomFileName

from    testimonial.apps            import TestimonialConfig


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief Get random file name for testimonial image.
#
#  @param instance [ appModel.models.Testimonial | None | in  ] - Testimonial model class instance.
#  @param fileName [ str                         | None | in  ] - File name.
#
#  @exception N/A
#
#  @return str - File path.
def getTestimonialAvatarImageFieldUploadTo(instance, fileName):

    fileRelativePath = '{}/{}'.format(TestimonialConfig.name,
                                      createRandomFileName(fileName))

    return fileRelativePath

#
## @brief [ DJANGO MODEL CLASS ] - Django model class.
class Testimonial(Model):
    #
    # ------------------------------------------------------------------------------------------------
    # CLASSES
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief [ DJANGO MODEL META CLASS ] - Meta class of django.db.models.Model class.
    class Meta:

        ## [ str ] - Verbose name of the model class.
        verbose_name        = 'Testimonial'

        ## [ str ] - Verbose plural name of the model class.
        verbose_name_plural = 'Testimonial'

        ## [ tuple ] - Ordering of the model class.
        ordering            = ('order',)

    #
    # ------------------------------------------------------------------------------------------------
    # FIELDS
    # ------------------------------------------------------------------------------------------------
    ## [ django.db.models.NullBooleanField ] - Order.
    order                   = models.PositiveIntegerField(default=0, blank=True,
                                                          help_text='Order')

    ## [ django.db.models.CharField ] - Name of the person.
    name                    = models.CharField(max_length=200,
                                               help_text='First and Last Name')

    ## [ django.db.models.CharField ] - Job title of the person.
    job_title               = models.CharField(max_length=200, blank=True,
                                               help_text='Job Title')

    ## [ django.db.models.CharField ] - Company.
    company                 = models.CharField(max_length=200, blank=True,
                                               help_text='Company')

    ## [ django.db.models.CharField ] - Testimonial body.
    body                    = models.TextField(max_length=2000,
                                               help_text='Testimonial Body')

    ## [ django.db.models.CharField ] - URL.
    url                     = models.CharField(max_length=500, blank=True,
                                               help_text='URL')

    ## [ django.db.models.ImageField ] - Avatar.
    avatar                  = models.ImageField(upload_to=getTestimonialAvatarImageFieldUploadTo, blank=True,
                                                help_text='Avatar')

    #
    # ------------------------------------------------------------------------------------------------
    # BUILT-IN METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief String representation.
    #
    #  @exception N/A
    #
    #  @return str - String representation.
    def __str__(self):

        return Model.__dict__['_str'](self,
                                      '{} - {} - {}'.format(self.order,
                                                            self.name,
                                                            self.job_title))
