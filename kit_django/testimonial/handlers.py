#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
import  os

from    core.storages       import removeFile
from    testimonial.models  import Testimonial


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief Pre save callback.
#
#  @param sender        [ django.db.models.base.ModelBase | None | in  ] - Django model.
#  @param instance      [ django.db.models.Model          | None | in  ] - Django model class instance.
#  @param raw           [ bool                            | None | in  ] - If the model is saved exactly as presented.
#  @param using         [ str                             | None | in  ] - The database alias being used.
#  @param update_fields [ set                             | None | in  ] - The set of fields to update as passed.
#  @param kwargs        [ dict                            | None | in  ] - Keyword arguments.
#
#  @exception N/A
#
#  @return None - None.
def testimonialPreSave(sender, instance, raw, using, update_fields, **kwargs):

    if instance.id:

        testimonial = None

        try:
            testimonial = Testimonial.objects.get(pk=instance.pk)
        except Testimonial.DoesNotExist:
            return

        if instance.avatar and testimonial.avatar           and \
           instance.avatar.path != testimonial.avatar.path  and \
           os.path.isfile(testimonial.avatar.path):

            removeFile(testimonial.avatar.path)

#
## @brief Post save callback.
#
#  @param sender   [ django.db.models.base.ModelBase | None | in  ] - Django model.
#  @param instance [ django.db.models.Model          | None | in  ] - Django model class instance.
#  @param created  [ bool                            | None | in  ] - Whether this instance is created.
#  @param kwargs   [ dict                            | None | in  ] - Keyword arguments.
#
#  @exception N/A
#
#  @return None - None.
def testimonialPostSave(sender, instance=None, created=False, **kwargs):

    pass

#
## @brief Pre delete callback.
#
#  @param sender   [ django.db.models.base.ModelBase | None | in  ] - Django model.
#  @param instance [ django.db.models.Model          | None | in  ] - Django model class instance.
#  @param using    [ str                             | None | in  ] - The database alias being used.
#  @param kwargs   [ dict                            | None | in  ] - Keyword arguments.
#
#  @exception N/A
#
#  @return None - None.
def testimonialPreDelete(sender, instance, using, **kwargs):

    if instance.avatar:
        # User attribute to get the path
        removeFile(instance.avatar.path)