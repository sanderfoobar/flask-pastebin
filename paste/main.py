from paste import app

from paste.controllers.helpers import render


@app.route('/')
def root():
    return render('index')


@app.errorhandler(404)
def error(e):
    return render('error', msg=str(e))
