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

from    django.conf import settings


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief Remove file from storage.
#
#  Function checks whether given `filePath` exists, if so it tries to delete it.
#  If file doesn't exists, `parentPath` will be added front of the `filePath` and
#  operation repeats. Function doesn't raise any error if file doesn't exist or couldn't be deleted.
#
#  @param filePath   [ str | None | in  ] - Path of the file, which will be removed.
#  @param parentPath [ str | None | in  ] - Parent path.
#
#  @exception N/A
#
#  @return True  - File found and deleted.
#  @return False - File either not found nor deleted.
def removeFile(filePath, parentPath=settings.MEDIA_ROOT):

    if os.path.isfile(filePath):

        try:
            os.remove(filePath)
            return True
        except Exception:
            pass

        return

    filePath = os.path.join(parentPath, filePath)
    if os.path.isfile(filePath):

        try:
            os.remove(filePath)
            return True
        except Exception:
            pass

    return False

#
## @brief Remove path from storage.
#
#  Function checks whether given `path` exists, if so it tries to delete it.
#  If file doesn't exists, `parentPath` will be added front of the `path` and
#  operation repeats. Function doesn't raise any error if path doesn't exist or couldn't be deleted.
#
#  @param path       [ str | None | in  ] - Path, which will be removed.
#  @param parentPath [ str | None | in  ] - Parent path.
#
#  @exception N/A
#
#  @return True  - Path found and deleted.
#  @return False - Path either not found nor deleted.
def removePath(path, parentPath=settings.MEDIA_ROOT):

    if os.path.isdir(path):

        try:
            shutil.rmtree(path)
            return True
        except Exception:
            return False

    path = os.path.join(parentPath, path)
    if os.path.isdir(path):

        try:
            shutil.rmtree(path)
            return True
        except Exception:
            return False

    return False



