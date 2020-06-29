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
def preSave(sender, instance, raw, using, update_fields, **kwargs):

    if instance.id:

        retrievedInstance = None

        try:
            retrievedInstance = instance.__class__.objects.get(pk=instance.pk)
        except instance.__class__.DoesNotExist:
            return

        if instance.image and retrievedInstance.image           and \
           instance.image.path != retrievedInstance.image.path  and \
           os.path.isfile(retrievedInstance.image.path):

            removeFile(retrievedInstance.image.path)

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
def postSave(sender, instance, created, **kwargs):

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
def preDelete(sender, instance, using, **kwargs):

    if instance.image:
        # User attribute to get the path
        removeFile(instance.image.path)
