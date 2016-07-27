import re
from flask import request, redirect, make_response, jsonify
from paste import app

import paste.controllers.pastes.converters
from paste.controllers.helpers import render
from paste.controllers.pastes.variables import expires_at
from paste.controllers.pastes.controller import PasteController
from paste.controllers.routes.errors import render_error


@app.route("/paste", methods=["POST"])
def paste():
    try:
        if request.files:
            files = request.files
            if not "files[]" in files:
                raise Exception("files[] not found")

            uids = []
            uploaded_files = request.files.getlist("files[]")
            for img in uploaded_files:
                uid = PasteController().write_image(ip_addr=request.remote_addr,
                                                    image=img)
                uids.append(uid)

            if uids:
                return jsonify({"success": True, "uri": "/i/%s" % ",".join(uids)})
            else:
                raise Exception()
        else:
            content = request.form.get("paste[body]", {})

            if "paste[restricted]" in request.form and request.form["paste[restricted]"] == "1":
                restricted = True
            else:
                restricted = False

            lang = request.form.get("paste[lang]", {})
            if lang == "0":
                lang = "plain"

            lang = re.sub("[^0-9a-zA-Z]+", "", lang)

            expiration = expires_at(request.form["paste[expir]"])

            uid = PasteController().write_text(ip_addr=request.remote_addr,
                                               syntax=lang,
                                               expiration=expiration,
                                               contents=content,
                                               private=restricted)

            return redirect("/p/%s" % uid, code=302)
    except Exception as ex:
        return render("index", errors=["failed j00"])


@app.route("/<path:type>/<browse:paste>")
def view_paste(type, paste):
    if type == "p":
        if isinstance(paste, list):
            raise Exception()

        try:
            paste = PasteController().read_text(uid=paste)
        except:
            return render_error("No Paste by that ID")

    elif type == "i":
        pastes = []

        if isinstance(paste, list):
            for p in paste:
                try:
                    paste = PasteController().read_image(uid=p)
                    pastes.append(paste)
                except:
                    pass
        else:
            pastes.append(PasteController().read_image(uid=paste))

        return render("paste", type=type, pastes=pastes, multi=True)

    return render("paste", type=type, paste=paste, multi=False)


@app.route("/<path:type>/<browse:paste>/raw")
def view_paste_raw(type, paste):
    try:
        if type == "p":
            blob = PasteController().read_text(uid=paste)

            r = make_response(blob["contents"], 200)
            r.headers.set("Content-Type", "text/plain")

            return r
        elif type == "i":
            blob = PasteController().read_image(uid=paste)
            r = make_response(blob["image"], 200)
            r.headers.set("Content-Type", "image/jpeg")

            return r
        else:
            raise Exception()
    except:
        return render_error("No Paste by that ID")
