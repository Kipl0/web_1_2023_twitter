from bottle import get, template

@get("/send-message")
def _():
    return template("send_message")

