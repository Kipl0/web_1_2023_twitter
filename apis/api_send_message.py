from bottle import post, request, response

@post("/api-send-message")
def _():
    try:
        sms_message = request.forms.get("sms_message", "")
        phone_number = request.forms.get("phone_number", "")

        return {"info": f"this is a test message"}

    except Exception as e:
        print(e)
        pass

    finally:
        pass