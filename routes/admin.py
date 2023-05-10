from bottle import get, template
import x

@get("/admin")
def _():
    try:
        db = x.db()

        users = db.execute("SELECT * FROM users").fetchall()
        

        return template("admin", users=users)

    except Exception as ex :
        pass

    finally :
        pass