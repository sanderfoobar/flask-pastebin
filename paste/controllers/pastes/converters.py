import re
import settings
from paste import app
from werkzeug.routing import BaseConverter
from paste.controllers.helpers import render
from paste.controllers.routes.errors import render_error
from paste.controllers.pastes.controller import PasteController


class PasteUrlConverter(BaseConverter):
    def to_python(self, value):
        if not re.match(r'^[a-zA-Z0-9][ A-Za-z0-9-,]*$', value):
            return render_error("No Paste by that ID")

        if len(value) < 36:
            return render_error("No Paste by that ID")

        if ',' in value:
            value = value.split(',')

        return value

    def to_url(self, values):
        return '+'.join(BaseConverter.to_url(value)
                        for value in values)

app.url_map.converters['browse'] = PasteUrlConverter
