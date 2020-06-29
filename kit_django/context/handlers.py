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

from    context.models      import Context


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
def contextPreSave(sender, instance, raw, using, update_fields, **kwargs):

    if instance.id:

        context = None

        try:
            context = Context.objects.get(pk=instance.pk)
        except Context.DoesNotExist:
            return

        if instance.image and context.image           and \
           instance.image.path != context.image.path  and \
           os.path.isfile(context.image.path):

            removeFile(context.image.path)

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
def contextPostSave(sender, instance=None, created=False, **kwargs):

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
def contextPreDelete(sender, instance, using, **kwargs):

    if instance.image:
        # User attribute to get the path
        removeFile(instance.image.path)