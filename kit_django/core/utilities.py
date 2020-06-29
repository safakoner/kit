#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief Get bool value from the given value.
#
#  @exception N/A
#
#  @return bool - Value.
def valueToBool(value):

    if value.strip() in ['true', 'True', '1', 1]:
        return True

    if value.strip() in ['false', 'False', '0', 0]:
        return False

#
## @brief Check given value against CSRF token.
#
#  This function is used for capthca validation.
#
#  @param token     [ str           | None | in  ] - CSRF token.
#  @param value     [ str           | None | in  ] - Value to be checked.
#  @param indexList [ list of int   | None | in  ] - Indices to be checked.
#
#  @exception N/A
#
#  @return bool - Result.
def checkCSRFToken(token, value, indexList=[7, 14, 23, 33]):

    tokenList = list(token)

    result = ''
    for i in indexList:
        result = '{}{}'.format(result, tokenList[i])

    return result == value

#
## @brief Check whether `Bearer` or `Token` provided, if so return the value.
#
#  @param bearerOrTokenStr [ str, bytes | None | in  ] - Value.
#
#  @exception N/A
#
#  @return str  - Bearer or token.
#  @return None - If no bearer or token provided in `bearerOrTokenStr`.
def getBearerOrToken(bearerOrTokenStr):

    if isinstance(bearerOrTokenStr, bytes):
        bearerOrTokenStr = bearerOrTokenStr.decode('utf-8')

    for value in ['token ', 'Token ', 'Bearer ', 'bearer ']:
        if value in bearerOrTokenStr:
            return bearerOrTokenStr.split(value)[1]

    return None