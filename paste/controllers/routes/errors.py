import settings
from paste import app, jinja2_env


@app.errorhandler(404)
def page_not_found(e):
    print e
    return '404', 404


@app.errorhandler(500)
def internal_error(error):
    return "500 error"


def render_error(error):
    template = jinja2_env.get_template('%s/templates/index.html' % settings.theme)
    return template.render(errors=[error], recent_public=None)
