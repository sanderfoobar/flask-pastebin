import os
import json
import uuid
import collections
import time  # heuheuhe
from datetime import datetime

from paste import app
from paste.bin.utils import ago

path_base = app.config['dir_base'] + '/data/'


class PasteController:
    def __init__(self):
        pass

    @staticmethod
    def write(**kwargs):
        from paste import loop
        loop.check()

        keys = 'ip_addr', 'syntax', 'expiration', 'private', 'contents'
        data = collections.OrderedDict()
        data['date'] = time.mktime(datetime.now().timetuple())

        for expected in keys:
            if not expected in kwargs:
                raise Exception('%s not found in arguments' % expected)

            data[expected] = kwargs[expected]

        uid = PasteController._gen_uid()
        exposure = 'pub' if not data['private'] else 'priv'

        blob = json.dumps(data, indent=4, separators=(',', ': '))

        f = open('%s%s/%s' % (path_base, exposure, uid), 'w')
        f.write(blob)
        f.close()

        if data['expiration']:
            loop.data[uid] = {
                'date': data['expiration'],
                'uid': uid
            }

        return uid

    @staticmethod
    def read(uid):
        try:
            exposures = ['priv', 'pub']
            path = ''

            for exposure in exposures:
                try_path = '%s%s/%s' % (path_base, exposure, uid)

                if os.path.isfile(try_path):
                    path = try_path

            if not path:
                raise Exception('No paste found by that id')

            data = open(path).read()
            blob = json.loads(data)
            blob['uid'] = uid
            blob['ago'] = ago(dt=datetime.fromtimestamp(blob['date']))

            return blob
        except:
            raise Exception('Error while reading paste file')

    @staticmethod
    def delete(uid):
        for exposure in ['priv', 'pub']:
            try_path = '%s%s/%s' % (path_base, exposure, uid)
            if not os.path.isfile(try_path):
                continue

            try:
                os.remove(try_path)
            except:
                pass

    @staticmethod
    def recent_public():
        from paste import loop
        loop.check()

        data = []

        uids = os.popen('ls -ht %spub/ | head -n 12' % path_base).read()
        uids = [z for z in uids.split('\n') if z]

        for uid in uids:
            paste = PasteController.read(uid)
            data.append(paste)

        return data

    @staticmethod
    def _gen_uid():
        return str(uuid.uuid4())


class PasteLoop:
    def __init__(self):
        self.data = {}

    def check(self):
        pops = []
        now = time.mktime(datetime.now().timetuple())

        for k, v in self.data.iteritems():
            uid = k
            date = v['date']

            if now > date:
                PasteController.delete(uid)
                pops.append(uid)

        for p in pops:
            try:
                self.data.pop(p)
            except:
                pass