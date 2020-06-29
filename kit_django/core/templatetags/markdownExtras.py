#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from    django                             import template
from    django.template.defaultfilters     import stringfilter

import  markdown                            as md


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
## [ django.template.Library ] - Class instance.
register = template.Library()

#
## @brief Markdown template filter.
#
#  @param value [ str | None | in  ] - Value.
#
#  @exception N/A
#
#  @return str - HTML version of the markdown value.
@register.filter()
@stringfilter
def markdown(value):

    return md.markdown(value, extensions=['nl2br'])
