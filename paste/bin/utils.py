import math
from datetime import datetime


def ago(dt=None, epoch=None):
    now = datetime.now()

    if epoch:
        td = int(epoch)
    else:
        if dt:
            td = (now - dt).total_seconds()
        else:
            return None

    if td < 60:
        if td == 1:
            return '%s second ago'
        else:
            return 'Just now'
    elif 60 <= td < 3600:
        if 60 <= td < 120:
            return '1 minute ago'
        else:
            return '%s minutes ago' % str(int(math.floor(td / 60)))
    elif 3600 <= td < 86400:
        if 3600 <= td < 7200:
            return '1 hour ago'
        else:
            return '%s hours ago' % str(int(math.floor(td / 60 / 60)))
    elif td >= 86400:
        if td <= 86400 < 172800:
            return '1 day ago'
        else:
            x = int(math.floor(td / 24 / 60 / 60))
            if x == 1:
                return '1 day ago'
            return '%s days ago' % str(x)