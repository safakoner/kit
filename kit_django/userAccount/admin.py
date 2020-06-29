#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from django.contrib             import admin
from django.contrib.auth.admin  import UserAdmin

from userAccount.models         import UserAccount
from userAccount.forms          import UserAccountCreationForm, UserAccountChangeForm


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ DJANGO USER ADMIN MODEL CLASS ] - Django user admin model class.
class UserAccountAdmin(UserAdmin):

    ## [ userAccount.forms.UserAccountCreationForm ] - User account creation form.
    add_form            = UserAccountCreationForm

    ## [ userAccount.forms.UserAccountChangeForm ] - User account change form.
    form                = UserAccountChangeForm

    ## [ tuple ] - List display.
    list_display        = ['email', 'first_name', 'last_name', 'is_active', 'is_superuser', 'is_staff',]

    ## [ list of str ] - List filter.
    list_filter         = ['is_active', 'is_superuser', 'is_staff', 'has_account_been_verified']

    ## [ list of str ] - Search fields.
    search_fields       = ['email',]

    ## [ list of str ] - Ordering.
    ordering            = ['-is_superuser', '-is_staff', '-email',]

    ## [ list of str ] - Filter horizontal.
    filter_horizontal   = []

    ## [ list of str ] - Readonly fields.
    readonly_fields     = ['folder_name', 'account_verification_id',]

    ## [ list ] - Add field set.
    add_fieldsets = [

        ('Account Related'                  , {'fields': ['is_active', 'email', 'first_name', 'last_name', 'avatar', 'password1', 'password2']}),

        ('Admin Related'                    , {'fields': ['is_superuser', 'is_staff',  'groups', 'user_permissions']}),

        ]

    ## [ list ] - Field set.
    fieldsets = [

        ('Account Related'                  , {'fields': ['is_active', 'email', 'first_name', 'last_name', 'avatar', 'folder_name']}),

        ('Registration'                     , {'fields': ['has_account_been_verified', 'account_verification_id']}),

        ('Admin Related'                    , {'fields': ['is_superuser', 'is_staff',  'groups', 'user_permissions']}),

        ]

admin.site.register(UserAccount, UserAccountAdmin)
