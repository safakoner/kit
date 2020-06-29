#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
import  os
import  json

from    django.core.management.base     import BaseCommand

from    contact.models                  import Address, Contact, Email, Phone, SocialMedia
from    content.models                  import Content, ContentType, Item
from    context.models                  import Context
from    conversion.models               import Conversion
from    faq.models                      import FAQ
from    language.models                 import Language
from    newsletter.models               import Newsletter
from    privacyNotice.models            import PrivacyNotice
from    projectSettings.models          import ProjectSettings
from    simpleAPIAccount.models         import SimpleAPIAccount
from    termsOfUse.models               import TermsOfUse
from    testimonial.models              import Testimonial


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ DJANGO BASE COMMAND CLASS ] - Base command class.
class Command(BaseCommand):
    #
    # ------------------------------------------------------------------------------------------------
    # PUBLIC STATIC MEMBERS
    # ------------------------------------------------------------------------------------------------
    ## [ str ] - Help.
    help = 'Create data'

    #
    # ------------------------------------------------------------------------------------------------
    # REIMPLEMENTED PUBLIC METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Add arguments.
    #
    #  @param parser [ django.core.management.base.CommandParser | None | in  ] - Parser.
    #
    #  @exception N/A
    #
    #  @return None - None.
    def add_arguments(self, parser):

        parser.add_argument('name', type=str)

    #
    ## @brief Handle.
    #
    #  @param args    [ tuple | None | in  ] - Arguments.
    #  @param options [ dict  | None | in  ] - Options.
    #
    #  @exception N/A
    #
    #  @return None - None.
    def handle(self, *args, **options):

        dataFilesPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data', options['name']))
        #dataFileList = [x for x in os.listdir(dataFilePath) if os.path.isfile(os.path.join(dataFilePath, x))]

        if not os.path.isdir(dataFilesPath):
            self.stdout.write(self.style.WARNING('Data path doesn\'t exist: {}'.format(dataFilesPath)))
            return

        Language.createDefaultLanguages()

        modelClassObjectList = [Context,
                                ContentType,
                                Content,
                                Item,
                                Address,
                                Contact,
                                Email,
                                Phone,
                                SocialMedia,
                                Conversion,
                                FAQ,
                                Newsletter,
                                PrivacyNotice,
                                ProjectSettings,
                                SimpleAPIAccount,
                                TermsOfUse,
                                Testimonial
                                ]

        for modelClassObject in modelClassObjectList:

            dataFileName = '{}.json'.format(modelClassObject.__name__)
            dataFilePath = os.path.join(dataFilesPath, dataFileName)

            if not os.path.isfile(dataFilePath):
                self.stdout.write(self.style.WARNING('Data file doesn\'t exist: {}'.format(dataFilePath)))
                continue

            _dataFile = open(dataFilePath, 'r')
            dataList  = json.loads(_dataFile.read())
            _dataFile.close()

            for dataObject in dataList:

                if 'context' in dataObject and dataObject['context']:
                    dataObject['context'] = Context.objects.filter(domain=dataObject['context'])[0]

                if 'language' in dataObject and dataObject['language']:
                    dataObject['language'] = Language.objects.filter(code=dataObject['language'])[0]

                if 'content_type' in dataObject and dataObject['content_type']:
                    dataObject['content_type'] = ContentType.objects.filter(code=dataObject['content_type'])[0]

                modelInstance, created = modelClassObject.objects.get_or_create(**dataObject)

            self.stdout.write(self.style.SUCCESS('Data created: {}'.format(modelClassObject.__name__)))

        self.stdout.write(self.style.SUCCESS('Demo data has been created.'))