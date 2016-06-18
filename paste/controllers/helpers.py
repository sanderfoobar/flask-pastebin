import settings
from paste import app

from flask import request, url_for, render_template
from paste.controllers.pastes.controller import PasteController


def redirect_url(default='index'):
    return request.args.get('next') or url_for(default) or request.referrer


def render(template_path, status_code=200, **kwargs):
    # @TO-DO: check session theme here
    theme = settings.theme

    # @TO-DO: use a context processor
    kwargs['env'] = {z: app.config[z] for z in app.config if z.islower()}
    kwargs['env']['application_root'] = app.config['APPLICATION_ROOT']

    kwargs['recent_public'] = PasteController.recent_public()

    return render_template('%s/templates/%s.html' % (theme, template_path), **kwargs), status_code