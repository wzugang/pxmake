from shutil import rmtree
from os import rmdir

def xm_os_rmdir(lua, ph, *args):
    rmempty = True if args and args[0] == True else False
    try:
        if rmempty:
            rmdir(ph)
        else:
            rmtree(ph)
    except (OSError, PermissionError, FileNotFoundError, NotADirectoryError):
        return False
    return True
