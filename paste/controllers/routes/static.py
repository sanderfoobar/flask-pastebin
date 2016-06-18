import os
from paste import app
from flask import render_template, request, flash, session, redirect, url_for, send_from_directory, abort


@app.route('/static/<path:filename>')
def static(filename):
    if filename.startswith('/'):
        return abort(404)

    from paste.controllers.helpers import render

    filename = filename.replace('..', '')
    filename = filename.replace('./', '')

    search_dirs = ['static/']

    # if not settings.local:
    #     search_dirs.insert(0, 'themes/_setup/static/')

    if filename.startswith('themes/'):
        spl = filename.split('/')

        if len(spl) >= 3 and spl[2] == 'static':
            filename = '/'.join(spl[3:])
            search_dirs.insert(0, 'themes/%s/static/' % spl[1])

    for search_dir in search_dirs:
        directory = '%s/%s' % (app.config['dir_base'], search_dir)

        if os.path.isfile(directory + filename):
            return send_from_directory(directory, filename)

    return render('errors/404', status_code=404)