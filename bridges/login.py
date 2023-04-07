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

        response.set_cookie("user_cookie", does_user_exist, secret=x.COOKIE_SECRET, httponly=True)

        cookie_expiration_date = int(time.time()) + 7200

        return {"info":"success login", "login_username":does_user_exist["user_username"]}

    except Exception as ex:
        print(ex)
        response.status = 400
        return template("login", ex=ex)
    finally:
        if "db" in locals(): db.close()
