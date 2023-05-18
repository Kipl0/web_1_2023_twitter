from bottle import get, template, response, request
import x

@get("/admin")
def _():
    try:
        db = x.db()

        users = db.execute("SELECT * FROM users").fetchall()

        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)
        trends = db.execute("SELECT * FROM trends")

        deleted_users = db.execute("SELECT * FROM deleted_users").fetchall()

        return template("admin", users=users, user_cookie = user_cookie, trends = trends, deleted_users = deleted_users)

    except Exception as ex :
        print(ex)
        response.status = 400
        return {"error": str(ex)}

    finally :
        if "db" in locals(): db.close()