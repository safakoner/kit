#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
import os
import re
import binascii
import base64
import random
import uuid
import string


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief Create and return a random string.
#
#  @param size  [ 50     | int | in  ] - Size of the string.
#  @param chars [ a-z0-9 | str | in  ] - Characters to be used to create the random string.
#
#  @exception N/A
#
#  @return None - None.
def createRandomString(size=50, chars=string.ascii_lowercase + string.digits):

    return ''.join(random.choice(chars) for _ in range(size))

#
## @brief Create and return an UUID.
#
#  @param onlyLetters [ True | bool | in  ] - Use only characters.
#  @param lowerCase   [ True | bool | in  ] - Whether to get lowercase value.
#
#  @exception N/A
#
#  @return str - UUID.
def createUUID(onlyLetters=True, lowerCase=True):

    value = base64.b64encode(uuid.uuid4().bytes).decode('utf-8')

    if onlyLetters:
        value = re.sub(r'[\=\+\/\-]', lambda m: {'=':'',
                                                 '+':'',
                                                 '/':'',
                                                 '-':''}[m.group(0)], value)

    if lowerCase:
        value = value.lower()

    return value.lower()

#
## @brief Create and return a random URL based on UUID.
#
#  @param count       [ 2    | int  | in  ] - How many UUID is to be used.
#  @param onlyLetters [ True | bool | in  ] - Use only characters.
#  @param lowerCase   [ True | bool | in  ] - Whether to get lowercase value.
#
#  @exception N/A
#
#  @return str - URL.
def createRandomURL(count=2, onlyLetters=True, lowerCase=True):

    value = ''

    for i in range(count):
        value = '{}{}'.format(value, createUUID(onlyLetters, lowerCase))

    return value

#
## @brief Create random file name for given file.
#
#  @param fileName [ str | None | in  ] - File name with extension.
#
#  @exception N/A
#
#  @return str - Random file name.
def createRandomFileName(fileName):

    return '{}{}'.format(createUUID(), os.path.splitext(fileName)[1])

#
## @brief Create random token.
#
#  @exception N/A
#
#  @return str - Token.
def createToken():

    return binascii.hexlify(os.urandom(20)).decode()