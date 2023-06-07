from bottle import post, response, request, time, template
import x
import pathlib
import bcrypt
import sqlite3
import jwt

@post("/login")
def _():
    try:
        db = x.db()

        login_username = request.forms.get("login-username")
        login_password = request.forms.get("login-password")

        # Kun til thunder client 
        if login_username == None : raise Exception(400, "No input in form data login-username")
        if login_password == None : raise Exception(400, "No input in form data login-password")

        # Hvis password er blevet udfyld -> encode
        login_password = login_password.encode("utf-8")

        does_user_exist = db.execute("SELECT * FROM users WHERE user_username = ? LIMIT 1", (login_username,)).fetchone()

        if not does_user_exist:
            raise Exception(400, "Cannot login")
        
        user_not_verified = db.execute("SELECT * FROM accounts_to_verify WHERE verify_user_fk = ?",(does_user_exist['user_id'],)).fetchone()
        # tjek om bruger ligger i verify tabel
        if not user_not_verified == None :
            print(user_not_verified)
            raise Exception(400, "User account is not verified yet")


        if does_user_exist["user_active"] == "0":
            raise Exception(400, "User account is deactivated")

        if not bcrypt.checkpw(login_password, does_user_exist["user_password"]):
            raise Exception(400, "Cannot login")


        # ----------------------------
        #       cookie og jwt
        # ----------------------------
        # jwt
        does_user_exist["user_password"] = ""
        user_jwt = jwt.encode(does_user_exist, x.JWT_SECRET, algorithm=x.JWT_ALGORITHM)

        # set cookie
        cookie_expiration_date = int(time.time()) + 7200
        response.set_cookie("user_cookie", user_jwt, secret=x.COOKIE_SECRET, httponly=True, expires=cookie_expiration_date)

        
        return {"info": "ok"}
    except Exception as ex:
        # Handle the exception or re-raise it if needed
        response.status = 400
        print(ex)
        return {"info": str(ex)}
        # except Exception as ex:
    finally:
        if "db" in locals(): db.close()

