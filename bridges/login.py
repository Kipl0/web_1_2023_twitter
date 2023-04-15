from bottle import post, response, request, time, template
import x
import pathlib
import bcrypt
import sqlite3



@post("/login")
def _():
    # Redirection, status code, the redirected page
    try:
        db = x.db()
        # Eksisterer brugeren
        # matcher input password med bruger password
        login_username = request.forms.get("login-username")
        login_password = request.forms.get("login-password").encode("utf-8")

        does_user_exist = db.execute("SELECT * FROM users WHERE user_username = ? LIMIT 1",(login_username,)).fetchone()

        if not does_user_exist: raise Exception(400, "Cannot login")
        if not bcrypt.checkpw(login_password, does_user_exist["user_password"]) :
            raise Exception(400, "cannot login")

        response.set_cookie("user_cookie", does_user_exist, secret=x.COOKIE_SECRET, httponly=True)
        cookie_expiration_date = int(time.time()) + 7200
        return 
        # return {"info":"success log in", "login_username":does_user_exist["user_username"]} #bruges til at få fat i username til at logge ind på egen profil - men det vil jeg ikke have

    except Exception as ex:
        print(ex)
        response.status = 400
        return template("login", ex=ex)
    finally:
        if "db" in locals(): db.close()
