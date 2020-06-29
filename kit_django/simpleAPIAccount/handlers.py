#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from core.randomValue   import createToken


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
def apiAccountPreSave(sender, instance, raw, using, update_fields, **kwargs):

    if not instance.token:
        instance.token = createToken()

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
def apiAccountPostSave(sender, instance=None, created=False, **kwargs):

    pass
