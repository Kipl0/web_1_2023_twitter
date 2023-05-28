from bottle import get, request, response, template
import x

@get("/self-deactivate-profile/<deactivate_key>")
def _(deactivate_key) :
    return template("self_deactivate_profile")