from bottle import run, get, template
import sqlite3

##############################
def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}

###########################
#       Routes
###########################
import apis.api_delete_user
import apis.api_get_latest_tweets



###########################
#       Routes
###########################
@get("/timeout")
def _():
    return template("timeout")

@get("/")
def _():
    try:
        db = sqlite3.connect("company.db")
        db.row_factory = dict_factory
        users = db.execute("SELECT * FROM users").fetchall()
        # print(users)
        return template("index", users=users)

    except Exception as e:
        print(e)

    finally:
        if "db" in locals(): db.close()

run(host="127.0.0.1", port=1220, debug=True, reloader=True)