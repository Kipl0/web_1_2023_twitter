from bottle import get, template

@get("/register")
def _():
    return template("register")