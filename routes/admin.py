from bottle import get, template, response, request
import x

@get("/admin")
def _():
    try:
        db = x.db()

        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)

        if user_cookie["user_username"] == "Admin" :
            users = db.execute("SELECT * FROM users WHERE user_username != ?",(user_cookie["user_username"],)).fetchall()

            trends = db.execute("SELECT * FROM trends")

            deleted_users = db.execute("SELECT * FROM deleted_users").fetchall()

            return template("admin", users=users, user_cookie = user_cookie, trends = trends, deleted_users = deleted_users)

        return template("/")

    except Exception as ex :
        print(ex)
        response.status = 400
        return {"error": str(ex)}

    finally :
        if "db" in locals(): db.close()