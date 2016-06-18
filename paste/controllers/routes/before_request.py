from paste import app


@app.before_request
def require_authorization():
    pass