# -*- coding: utf-8 -*-
import settings
from gevent import monkey
monkey.patch_all()

from gevent.pywsgi import WSGIServer
from paste import app

http_server = WSGIServer((settings.BIND_HOST, settings.BIND_PORT), app)
print ' * Running on http://%s:%s/ (Press CTRL+C to quit)' % (settings.BIND_HOST, str(settings.BIND_PORT))
http_server.serve_forever()