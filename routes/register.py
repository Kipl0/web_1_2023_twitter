from bottle import get, template
import x

@get("/register")
def _():
    return template("register", USER_NAME_MIN=x.USER_NAME_MIN, USER_NAME_MAX=x.USER_NAME_MAX, PASSWORD_MIN=x.PASSWORD_MIN, PASSWORD_MAX=x.PASSWORD_MAX)