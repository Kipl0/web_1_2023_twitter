from bottle import post
import x

# post til at user bliver verified i db
@post("/verify-email/<verification-key>") #verification key kommer fra db
def _():
    try :
        db = x.db()
        print("##"*20)
        print("Tester test")

    except Exception as ex :
        print(ex)
        response.status = 400
        return {"error": str(ex)}

    finally :
        if "db" in locals : close.db()