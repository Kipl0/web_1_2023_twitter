from bottle import get, request, response, template
import x

@get("/change-password/<user_key>")
def _(user_key):
    try :
        db = x.db()

        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)

        if user_cookie :
            response.status = 303
            response.set_header("Location", "/")
            return
        else:
            print("user_cookie eksisterer ikke")
            return template("change_password_page")


    except Exception as ex :
        print(x)
        response.status = ex.args[0]
        return {"info":ex.args[1]}


    finally :
        if "db" in locals() : db.close()