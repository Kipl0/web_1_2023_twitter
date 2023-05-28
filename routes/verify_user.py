from bottle import template, get
# import x

# routen til "din email er godkendt"
@get("/verify-email/<verification_key>") #/<verification-key>
def verify_accout(verification_key):
    try :
        return template("verified_user")


    except Exception as ex :
        print(ex)
        response.status = 400
        return {"error": str(ex)}
