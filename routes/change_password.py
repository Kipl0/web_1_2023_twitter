from bottle import get, request, response, template
import x

@get("/change-password")
def _():
    try :
        db = x.db()

        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)

        print(user_cookie)

        if user_cookie :
            response.status = 303
            response.set_header("Location", "/")
            return
        else:
            print("DEN BURDE VÆRE NONE")
            return template("change_password")


    except Exception as ex :
        print(x)
        response.status = ex.args[0]
        return {"info":ex.args[1]}


    finally :
        if "db" in locals() : db.close()