from bottle import post, response, request, time, template
import x
import pathlib


@post("/login")
def _():
    # Redirection, status code, the redirected page
    try:
        db = x.db()
    
        # Eksisterer brugeren
        # matcher input password med bruger password
        login_username = request.forms.get("login-username")
        login_password = request.forms.get("login-password")

        does_user_exist = db.execute("SELECT * FROM users WHERE user_username = ? AND user_password = ?",(login_username,login_password,)).fetchall()[0]

        response.set_cookie("login", does_user_exist, secret=x.COOKIE_SECRET, httponly=True)

        cookie_expiration_date = int(time.time()) + 7200
        # response.status = 303 #vi bruger denne status til at lede videre på en ny side - tjek forskellige status og hvad de betyder
        # response.set_header("Location", "/")

        return {"info":"success login", "login_username":does_user_exist["user_username"]}

    except Exception as ex:
        print(ex)
        response.status = 400
        return template("login", ex=ex)
    finally:
        if "db" in locals(): db.close()




        ################# skal slettes#######################
        # if not login_username: #is there any data in the requested input field
        #     raise Exception("Please insert username") #pass også en 400 error

        # if not login_password:
        #     raise Exception("Please insert password") #pass også en 400 error

        # does_user_exist = db.execute("SELECT * FROM users WHERE user_username = ? AND user_password = ?",(login_username,login_password,)).fetchall()[0]
        # if not does_user_exist:
        #     raise Exception("User doesn't exist") #pass også en 400 error


