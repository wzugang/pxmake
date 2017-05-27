from os.path import isfile
from xmerrno import set_errno
from xmtrace import xmtrace

@xmtrace
def xm_os_isfile(lua, ph):
    try:
        return isfile(ph)
    except OSError as e:
        set_errno(e.errno)
        return False