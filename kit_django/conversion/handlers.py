#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
import  os

from    core.randomValue    import createUUID, createRandomURL
from    core.storages       import removeFile, removePath

from    conversion.models   import Conversion


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
def conversionPreSave(sender, instance, raw, using, update_fields, **kwargs):

    if not instance.id:

        instance.folder_name = createUUID()

        randomURL = createRandomURL()
        while Conversion.objects.filter(url_id=randomURL).exists():
            randomURL = createRandomURL()
        instance.url_id = randomURL

    else:

        conversion = None

        try:
            conversion = Conversion.objects.get(pk=instance.pk)
        except Conversion.DoesNotExist:
            return

        if instance.background_image and conversion.background_image           and \
           instance.background_image.path != conversion.background_image.path  and \
           os.path.isfile(conversion.background_image.path):

            removeFile(conversion.background_image.path)

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
def conversionPostSave(sender, instance, created, **kwargs):

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
def conversionPreDelete(sender, instance, using, **kwargs):

    if instance.background_image:
        # User attribute to get the path
        removePath(os.path.dirname(instance.background_image.path))
