#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
import  os

from    rest_framework.authtoken.models import Token

from    core.randomValue                import createUUID, createRandomURL
from    core.storages                   import removeFile, removePath

from    userAccount.models              import UserAccount


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
def userAccountPreSave(sender, instance, raw, using, update_fields, **kwargs):

    if not instance.id:

        folderName = createUUID()
        while UserAccount.objects.filter(folder_name=folderName).exists():
            folderName = createRandomURL()
        instance.folder_name = folderName

        #

        randomURL = createRandomURL()
        while UserAccount.objects.filter(account_verification_id=randomURL).exists():
            randomURL = createRandomURL()
        instance.account_verification_id = randomURL

    else:

        userAccount = None

        try:
            userAccount = UserAccount.objects.get(pk=instance.pk)
        except UserAccount.DoesNotExist:
            return

        if instance.avatar and userAccount.avatar           and \
           instance.avatar.path != userAccount.avatar.path  and \
           os.path.isfile(userAccount.avatar.path):

            removeFile(userAccount.avatar.path)

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
def userAccountPostSave(sender, instance=None, created=False, **kwargs):

    if created:
        Token.objects.create(user=instance)

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
def userAccountPreDelete(sender, instance, using, **kwargs):

    if instance.avatar:
        # User attribute to get the path
        removePath(os.path.dirname(instance.avatar.path))