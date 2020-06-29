#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from context.models         import Context
from language.models        import Language


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief Get or create default context and language.
#
#  @exception N/A
#
#  @return tuple of django.db.models.Model - Django model instances.
def getOrCreateContextAndLanguageObjects():

    return Context.createDefaultContext(), Language.createDefaultLanguages()[0]




