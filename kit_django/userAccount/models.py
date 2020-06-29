#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from    django.db                       import models
from    django.contrib.auth.models      import AbstractBaseUser, PermissionsMixin

from    rest_framework.authtoken.models import Token

from    core.randomValue                import createRandomFileName

from    userAccount.apps                import UserAccountConfig
from    userAccount.managers            import UserAccountManager


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
def getUserAccountAvatarImageFieldUploadTo(instance, fileName):

    fileRelativePath = '{}/{}/{}'.format(UserAccountConfig.name,
                                         instance.folder_name,
                                         createRandomFileName(fileName))

    return fileRelativePath

#
## @brief [ DJANGO MODEL CLASS ] - Django model class.
class UserAccount(AbstractBaseUser, PermissionsMixin):

    ## [ userAccount.managers.UserAccountManager ] - Objects.
    objects                     = UserAccountManager()

    ## [ str ] - Username field.
    USERNAME_FIELD              = 'email'

    #
    # ------------------------------------------------------------------------------------------------
    # CLASSES
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief [ DJANGO MODEL META CLASS ] - Meta class of django.db.models.Model class.
    class Meta:

        ## [ str ] - Verbose name of the model class.
        verbose_name        = 'User Account'

        ## [ str ] - Verbose plural name of the model class.
        verbose_name_plural = 'User Account'

        ## [ tuple ] - Ordering of the model class.
        ordering            = ('email',)

    #
    # ------------------------------------------------------------------------------------------------
    # FIELDS
    # ------------------------------------------------------------------------------------------------
    ## [ django.db.models.NullBooleanField ] - Whether this user is super user.
    is_superuser                = models.NullBooleanField(default=False, null=True, blank=True)

    ## [ django.db.models.NullBooleanField ] - Whether this user is admin.
    is_staff                    = models.NullBooleanField(default=False, null=True, blank=True)

    ## [ django.db.models.NullBooleanField ] - Whether this instance is active.
    is_active                   = models.NullBooleanField(default=True, null=True, blank=True)

    ## [ django.db.models.EmailField ] - Email.
    email                       = models.EmailField(verbose_name='email', max_length=255, unique=True, blank=False, null=False)

    ## [ django.db.models.CharField ] - First name.
    first_name                  = models.CharField(max_length=20, blank=True, null=True)

    ## [ django.db.models.CharField ] - Last name.
    last_name                   = models.CharField(max_length=20, blank=True, null=True)

    ## [ django.db.models.ImageField ] - Avatar.
    avatar                      = models.ImageField(upload_to=getUserAccountAvatarImageFieldUploadTo, blank=True)

    ## [ django.db.models.CharField ] - Folder name.
    folder_name                 = models.CharField(max_length=200, null=False, blank=False)

    ## [ django.db.models.DateTimeField ] - Last login.
    last_login                  = models.DateTimeField(auto_now=True)

    ## [ django.db.models.DateTimeField ] - Registration.
    registration_date_time      = models.DateTimeField(auto_now=False, auto_now_add=True)

    ## [ django.db.models.DateTimeField ] - Has account been verified.
    has_account_been_verified   = models.NullBooleanField(default=False, null=True, blank=True)

    ## [ django.db.models.DateTimeField ] - Account verification id.
    account_verification_id     = models.SlugField(max_length=300, unique=True, null=False, blank=False,)

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

        return self.email

    #
    # ------------------------------------------------------------------------------------------------
    # PROTECTED METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Property.
    #
    #  @exception N/A
    #
    #  @return rest_framework.authtoken.models.Token - Django model class instance.
    def api_token(self):

        return Token.objects.get(user=self)

    #
    ## @brief Property.
    #
    #  @exception N/A
    #
    #  @return bool - Value.
    def get_full_name(self):

        return '{} {}'.format(self.first_name, self.last_name)

    #
    ## @brief Property.
    #
    #  @exception N/A
    #
    #  @return bool - Value.
    def get_short_name(self):

        return self.first_name


