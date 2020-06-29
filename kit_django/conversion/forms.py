#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from django             import forms

from core.utilities     import checkCSRFToken

from conversion.models  import Subscriber


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ DJANGO MODEL FORM CLASS ] - Django model form class.
class SubscriberForm(forms.ModelForm):
    #
    # ------------------------------------------------------------------------------------------------
    # CLASSES
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief [ DJANGO MODEL META CLASS ] - Meta class of django.db.models.Model class.
    class Meta:

        ## [ django.db.models.Model ] - Django model class instance.
        model = Subscriber

        ## [ list ] - Fields.
        fields = ['name', 'email', 'willing_to_pay']

    #
    # ------------------------------------------------------------------------------------------------
    # INPUTS
    # ------------------------------------------------------------------------------------------------
    ## [ django.forms.CharField ] - Name.
    name    = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'Name'}))

    ## [ django.forms.EmailField ] - Email.
    email   = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder':'Email'}))

    ## [ django.forms.CharField ] - Capthca.
    capthca = forms.CharField(required=True, max_length=4, widget=forms.TextInput(attrs={'placeholder':'Please type capthca here'}))

    #
    # ------------------------------------------------------------------------------------------------
    # BUILT-IN METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Constructor.
    #
    #  @param args   [ tuple | None | in  ] - Arguments.
    #  @param kwargs [ dict  | None | in  ] - Keyword arguments.
    #
    #  @exception N/A
    #
    #  @return None - None.
    def __init__(self, *args, **kwargs):

        self._request = kwargs.pop('request')

        super(SubscriberForm, self).__init__(*args, **kwargs)

    #
    # ------------------------------------------------------------------------------------------------
    # REIMPLEMENTED PUBLIC METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Clean capthca field.
    #
    #  @exception N/A
    #
    #  @return variant - Cleaned value.
    def clean_capthca(self):

        if not self._request:
            return self.cleaned_data['capthca']

        capthca = self.cleaned_data['capthca']

        if not checkCSRFToken(self._request.META.get("CSRF_COOKIE"), capthca):
            self.add_error('capthca', 'Please confirm capthca')
            return None

        return capthca

    #
    ## @brief Save.
    #
    #  @param commit [ bool | None | in  ] - Commit save.
    #
    #  @exception N/A
    #
    #  @return conversion.models.Subscriber - Model class instance.
    def save(self, commit=True):

        subscriber = super(SubscriberForm, self).save(commit=False)

        if commit:
            subscriber.save()

        return subscriber