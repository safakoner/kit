#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from    django.utils                    import timezone
from    django.contrib.auth.models      import BaseUserManager


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ DJANGO BASE USER MANAGER CLASS ] - Base user manager class.
class UserAccountManager(BaseUserManager):
    #
    ## @brief Create user.
    #
    #  @param email      [ str  | None  | in  ] - Email.
    #  @param password   [ str  | None  | in  ] - Password.
    #  @param first_name [ str  | None  | in  ] - First name.
    #  @param last_name  [ str  | None  | in  ] - Last name.
    #  @param superUser  [ bool | False | in  ] - Whether to create super user.
    #
    #  @exception N/A
    #
    #  @return userAccount.models.UserAccount - Django model class instance.
    def create_user(self, email, password, first_name='', last_name='', superUser=False):

        user                            = self.model(email=self.normalize_email(email))

        user.is_active                  = True
        user.is_staff                   = superUser
        user.is_superuser               = superUser
        user.has_account_been_verified  = superUser

        user.first_name                 = first_name
        user.last_name                  = last_name

        now                             = timezone.now()
        user.last_login                 = now
        user.registration_date          = now

        user.set_password(password)

        user.save(using=self._db)

        return user

    #
    ## @brief Create super user.
    #
    #  @param email      [ str | None | in  ] - Email.
    #  @param password   [ str | None | in  ] - Password.
    #  @param first_name [ str | None | in  ] - First name.
    #  @param last_name  [ str | None | in  ] - Last name.
    #
    #  @exception N/A
    #
    #  @return userAccount.models.UserAccount - Django model class instance.
    def create_superuser(self, email, password, first_name='', last_name=''):

        return self.create_user(email,
                                password,
                                first_name,
                                last_name,
                                True)

