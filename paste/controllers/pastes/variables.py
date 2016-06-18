import time
from datetime import datetime, timedelta


def expires_at(exp):
    data = {
        '0': -1,
        '1': 60*10,
        '2': 60*60,
        '3': 60*60*24
    }

    if not exp in data or data[exp] == -1:
        return
    else:
        future = datetime.now() + timedelta(seconds=data[exp])
        return time.mktime(future.timetuple())
