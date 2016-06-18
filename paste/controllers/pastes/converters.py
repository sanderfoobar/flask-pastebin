import settings
from paste import app
from werkzeug.routing import BaseConverter
from paste.controllers.helpers import render
from paste.controllers.pastes.controller import PasteController
from paste.controllers.routes.errors import render_error


class PasteUrlConverter(BaseConverter):
    def to_python(self, value):
        if len(value) != 36:
            return render_error("No Paste by that ID")

        try:
            paste = PasteController().read(uid=value)
        except:
            return render_error("No Paste by that ID")

        if not paste:
            return render_error("No Paste by that ID")

        return paste

    def to_url(self, values):
        return '+'.join(BaseConverter.to_url(value)
                        for value in values)

app.url_map.converters['browse'] = PasteUrlConverter
