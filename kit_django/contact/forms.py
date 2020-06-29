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
from contact.models         import Contact


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
## [ dict of dict ] - Contact form subject choices.
CONTACT_FORM_SUBJECT_CHOICES = (('', ''),
                                ('Request Information'   , 'Request Information'),
                                )

#
## @brief [ DJANGO MODEL FORM CLASS ] - Django model form class.
class ContactForm(forms.ModelForm):
    #
    # ------------------------------------------------------------------------------------------------
    # CLASSES
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief [ DJANGO MODEL META CLASS ] - Meta class of django.db.models.Model class.
    class Meta:

        ## [ django.db.models.Model ] - Django model class instance.
        model   = Contact

        ## [ list ] - Fields.
        fields  = ['name', 'company', 'email', 'subject', 'message']

    #
    # ----------------------------------------------------------------------------------------------------
    # WIDGETS
    # ----------------------------------------------------------------------------------------------------
    ## [ django.forms.CharField ] - Context domain.
    context_domain  = forms.CharField(widget=forms.HiddenInput(attrs={'placeholder':'Context DomainXXXX'}))

    ## [ django.forms.CharField ] - Language code.
    language_code   = forms.CharField(widget=forms.HiddenInput(attrs={'placeholder':'Language Code'}))

    ## [ django.forms.CharField ] - Name.
    name            = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder':'Name'}))

    ## [ django.forms.CharField ] - Company.
    company         = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder':'Company / Organization'}))

    ## [ django.forms.EmailField ] - Email.
    email           = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'E-mail'}))

    ## [ django.forms.ChoiceField ] - Subject.
    subject         = forms.ChoiceField(choices=CONTACT_FORM_SUBJECT_CHOICES, widget=forms.Select(attrs={'placeholder':'subject'}))

    ## [ django.forms.CharField ] - Message.
    message         = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder':'Your message'}))

    ## [ django.forms.CharField ] - Capthca.
    capthca         = forms.CharField(required=True, max_length=4, widget=forms.TextInput(attrs={'placeholder':'Please enter capthca here',
                                                                                                 'class':'contact-form-capthca'}))

    #
    # ------------------------------------------------------------------------------------------------
    # BUILT-IN METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Constructor.
    #
    #  @param args   [ tuple | None | in  ] - Arguments.
    #  @param kwargs [ dict  | None | in  ] - Arguments.
    #
    #  @exception N/A
    #
    #  @return None - None.
    def __init__(self, *args, **kwargs):

        self._request         = kwargs.pop('request'         , None)
        self._contextDomain   = kwargs.pop('contextDomain'   , '')
        self._languageCode    = kwargs.pop('languageCode'    , LANGUAGE_CODE)
        self._subjectChoices  = kwargs.pop('subjectChoices'  , None)
        self._messageRequired = kwargs.pop('messageRequired' , True)

        super(ContactForm, self).__init__(*args, **kwargs)

        if self._contextDomain:
            self.fields['context_domain'] = forms.CharField(max_length=200, widget=forms.HiddenInput(attrs={'placeholder':'Context Domain',
                                                                                                            'value':self._contextDomain}))

        if self._languageCode:
            self.fields['language_code'] = forms.CharField(max_length=200, widget=forms.HiddenInput(attrs={'placeholder':'Language Code',
                                                                                                           'value':self._languageCode}))

        if self._subjectChoices:
            self.fields['subject'] = forms.ChoiceField(choices=self._subjectChoices, widget=forms.Select(attrs={'placeholder':'Subject'}))

        self.fields['message'] = forms.CharField(required=self._messageRequired, widget=forms.Textarea(attrs={'placeholder':'Your message'}))

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

        if not checkCSRFToken(self._request.META.get("CSRF_COOKIE"), capthca, [7, 14, 23, 33]):
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

        modelInstance = super(ContactForm, self).save(commit=False)

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
    #  @return contact.models.Contact - Django model class instance.
    def addContact(self):

        return Contact.addContact(self.cleaned_data)
