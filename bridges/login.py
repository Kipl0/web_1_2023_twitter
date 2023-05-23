from bottle import post, response, request, time, template
import x
import pathlib
import bcrypt
import sqlite3


@post("/login")
def _():
    try:
        db = x.db()

        login_username = request.forms.get("login-username")
        login_password = request.forms.get("login-password").encode("utf-8")

        does_user_exist = db.execute("SELECT * FROM users WHERE user_username = ? LIMIT 1", (login_username,)).fetchone()

        print(does_user_exist["user_verified"] == "0")

        if not does_user_exist:
            raise Exception(400, "Cannot login")

        if does_user_exist["user_verified"] == "0" :
            raise Exception(400, "User account is not verified yet")


        if does_user_exist["user_active"] == "0":
            raise Exception(400, "User account is deactivated")

        if not bcrypt.checkpw(login_password, does_user_exist["user_password"]):
            raise Exception(400, "Cannot login")

        response.set_cookie("user_cookie", does_user_exist, secret=x.COOKIE_SECRET, httponly=True)
        cookie_expiration_date = int(time.time()) + 7200
        return
    except Exception as ex:
        # Handle the exception or re-raise it if needed
        response.status = 400
        print(ex)
        return template("login", ex=ex)
        # except Exception as ex:
    finally:
        if "db" in locals(): db.close()

