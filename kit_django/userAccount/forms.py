#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from   django                       import forms
from   django.contrib.auth.forms    import ReadOnlyPasswordHashField

from   userAccount.models           import UserAccount


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ DJANGO MODEL CLASS ] - Django model form class.
class UserAccountCreationForm(forms.ModelForm):
    #
    # ------------------------------------------------------------------------------------------------
    # CLASSES
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief [ DJANGO MODEL META CLASS ] - Meta class of django.forms.ModelForm class.
    class Meta:
        
        ## [ userAccount.models.UserAccount ] - User account model.
        model  = UserAccount
        
        ## [ tuple ] - Fields.
        fields = ('first_name', 'last_name', 'email', 'password', 'is_active', 'is_superuser')

    #
    # ------------------------------------------------------------------------------------------------
    # FIELDS
    # ------------------------------------------------------------------------------------------------
    ## [ django.forms.CharField ] - Password 1.
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)

    ## [ django.forms.CharField ] - Password 2.
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    #
    ## @brief Clean password 2.
    #
    #  @exception N/A
    #
    #  @return str - Cleaned password.
    def clean_password2(self):

        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords don\'t match')

        return password1

    #
    ## @brief Save user.
    #
    #  @exception N/A
    #
    #  @return userAccount.forms.UserAccountCreationForm - User account creation form class instance.
    def save(self, commit=True):

        user = super(UserAccountCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()

        return user

#
## @brief [ DJANGO MODEL CLASS ] - Django model form class.
class UserAccountChangeForm(forms.ModelForm):
    #
    # ------------------------------------------------------------------------------------------------
    # CLASSES
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief [ DJANGO MODEL META CLASS ] - Meta class of django.forms.ModelForm class.
    class Meta:

        ## [ userAccount.models.UserAccount ] - User account model.
        model  = UserAccount

        ## [ tuple ] - Fields.
        fields = ('first_name', 'last_name', 'email', 'is_active', 'is_superuser', )

    #
    # ------------------------------------------------------------------------------------------------
    # FIELDS
    # ------------------------------------------------------------------------------------------------
    ## [ django.contrib.auth.forms.ReadOnlyPasswordHashField ] - Password.
    password = ReadOnlyPasswordHashField()































