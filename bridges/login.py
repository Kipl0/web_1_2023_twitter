from bottle import post, response, request, time, template
import sqlite3
import pathlib

def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}

@post("/login")
def _():
    # Redirection
    #status code
    # the redirected page
    try:
        # db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/twitter.db") 
        db = sqlite3.connect("twitter.db") 
        # db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/twitter.db") 
        db.row_factory = dict_factory

        # Eksisterer brugeren
        # matcher input password med bruger password
        login_username = request.forms.get("login-username")
        login_password = request.forms.get("login-password")

        if not login_username: #is there any data in the requested input field
            raise Exception("Please insert username")

        if not login_password:
            raise Exception("Please insert password")

        does_user_exist = db.execute("SELECT * FROM users WHERE user_username = ? AND user_password = ?",(login_username,login_password,)).fetchall()[0]
        if not does_user_exist:
            raise Exception("User doesn't exist")

        response.set_cookie("login", does_user_exist, secret="my-secret", httponly=True)


        cookie_expiration_date = int(time.time()) + 7200
        response.status = 303 #vi bruger denne status til at lede videre på en ny side - tjek forskellige status og hvad de betyder
        response.set_header("Location", "/")
    except Exception as ex:
        print(ex)
        response.status = 400
        return template("login", ex=ex)
    finally:
        if "db" in locals(): db.close()

    return 



