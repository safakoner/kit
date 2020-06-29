#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from django                 import forms

from core.utilities         import checkCSRFToken
from projectSettings.common import LANGUAGE_CODE

from newsletter.models      import Newsletter


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ DJANGO MODEL FORM CLASS ] - Django model form class.
class NewsletterForm(forms.ModelForm):
    #
    # ------------------------------------------------------------------------------------------------
    # CLASSES
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief [ DJANGO MODEL META CLASS ] - Meta class of django.db.models.Model class.
    class Meta:

        ## [ django.db.models.Model ] - Django model class instance.
        model   = Newsletter

        ## [ list ] - Fields.
        fields  = ['name', 'email']

    #
    # ----------------------------------------------------------------------------------------------------
    # WIDGETS
    # ----------------------------------------------------------------------------------------------------
    ## [ django.forms.CharField ] - Context domain.
    context_domain  = forms.CharField(max_length=200, widget=forms.HiddenInput(attrs={'placeholder':'Context DomainSSSSSs'}))

    ## [ django.forms.CharField ] - Language code.
    language_code   = forms.CharField(max_length=200, widget=forms.HiddenInput(attrs={'placeholder':'Language Code'}))

    ## [ django.forms.CharField ] - Name.
    name            = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'placeholder':'Name (Optional)',
                                                                                                    'class':'newsletter-form-name'}))

    ## [ django.forms.EmailField ] - Email.
    email           = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'E-mail*',
                                                                     'class':'newsletter-form-email'}))

    ## [ django.forms.CharField ] - Capthca.
    capthca         = forms.CharField(required=True, max_length=3, widget=forms.TextInput(attrs={'placeholder':'Please type capthca here*',
                                                                                                 'class':'newsletter-form-capthca'}))

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

        self._request         = kwargs.pop('request'       , None)
        self._contextDomain   = kwargs.pop('contextDomain' , '')
        self._languageCode    = kwargs.pop('languageCode'  , LANGUAGE_CODE)

        super(NewsletterForm, self).__init__(*args, **kwargs)

        if self._contextDomain:
            self.fields['context_domain'] = forms.CharField(max_length=200, widget=forms.HiddenInput(attrs={'placeholder':'Context Domain',
                                                                                                            'value':self._contextDomain}))

        if self._languageCode:
            self.fields['language_code'] = forms.CharField(max_length=200, widget=forms.HiddenInput(attrs={'placeholder':'Language Code',
                                                                                                           'value':self._languageCode}))

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

        if not checkCSRFToken(self._request.META.get("CSRF_COOKIE"), capthca, [2, 8, 10]):
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
    #  @return newsletter.models.Newsletter - Django model class instance.
    def save(self, commit=True):

        modelInstance = super(NewsletterForm, self).save(commit=False)

        if commit:
            modelInstance.save()

        return modelInstance

    #
    # ------------------------------------------------------------------------------------------------
    # PUBLIC METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Add subscriber.
    #
    #  @warning You must call `is_valid` method before you call this method.
    #
    #  @exception N/A
    #
    #  @return newsletter.models.Newsletter - Django model class instance.
    def addSubscriber(self):

        return Newsletter.addSubscriber(self.cleaned_data)
