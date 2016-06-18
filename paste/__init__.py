import os
import settings
import gevent
from flask import Flask
from flask.ext.babel import Babel

from jinja2 import Environment, FileSystemLoader
jinja2_env = Environment(loader=FileSystemLoader('paste/themes/'))

app = Flask(import_name=__name__,
            static_folder=None,
            template_folder='themes')

app.config['SECRET_KEY'] = settings.app_secret
app.config['dir_base'] = os.path.dirname(os.path.abspath(__file__))
app.config['dir_root'] = '/'.join(app.config['dir_base'].split('/')[:-1])
app.config['APPLICATION_ROOT'] = settings.BIND_ROUTE

SECRET_KEY = settings.app_secret

babel = Babel(app)

locales = {
    'en': 'English',
}

import paste.controllers.routes.static
import paste.controllers.routes.errors
import paste.controllers.routes.before_request

from bin.config import Config
settings = Config()

if not settings.local:
    raise Exception('Local settings (%s/settings.py) not found' % app.config['dir_root'])

# init routes
import main
import paste.controllers.pastes.routes

from paste.controllers.pastes.controller import PasteLoop
loop = PasteLoop()