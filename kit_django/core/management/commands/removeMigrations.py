#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
import  os
import  shutil

from    django.core.management.base     import BaseCommand

from    projectSettings                 import common

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
    help = 'Delete migration files in development mode'

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

        parser.add_argument('--rdb',
                            action='store_true',
                            help='Remove DB if its a file')

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

        if common.IS_IN_PRODUCTION:
            self.stdout.write(self.style.WARNING('This command is not supported in production.'))
            return

        #

        hasErrors = False

        removeDB = options['rdb']
        if removeDB:

            database = common.DATABASES['default']
            if database['ENGINE'] == 'django.db.backends.sqlite3':

                if os.path.isfile(database['NAME']):

                    try:
                        os.remove(database['NAME'])
                    except Exception as error:
                        hasErrors = True
                        self.stdout.write(self.style.ERROR(str(error)))

        #

        entryList = os.listdir(common.DJANGO_PROJECT_ROOT)
        for entry in entryList:

            path = os.path.join(common.DJANGO_PROJECT_ROOT, entry)
            if not os.path.isdir(path):
                continue

            if not os.path.isfile(os.path.join(path, 'apps.py')):
                continue

            migrationsPath = os.path.join(path, 'migrations')
            if not os.path.isdir(migrationsPath):
                continue

            migrationsPathEntryList = os.listdir(migrationsPath)
            for migrationEntry in migrationsPathEntryList:

                if migrationEntry == '__init__.py':
                    continue

                migrationEntryPath = os.path.join(migrationsPath, migrationEntry)

                try:

                    if os.path.isfile(migrationEntryPath):
                        os.remove(migrationEntryPath)
                        print('FILE: {}'.format(migrationEntryPath))

                    elif os.path.isdir(migrationEntryPath) and migrationEntryPath.endswith('__pycache__'):
                        shutil.rmtree(migrationEntryPath)
                        print('DIR:  {}'.format(migrationEntryPath))

                except Exception as error:
                    hasErrors = True
                    self.stdout.write(self.style.ERROR(str(error)))

        if hasErrors:
            self.stdout.write(self.style.WARNING('Some of the migration files couldn\'t be deleted.'))
        else:
            self.stdout.write(self.style.SUCCESS('Migration files have been deleted.'))