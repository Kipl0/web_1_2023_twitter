from bottle import get, response, request, template
import sqlite3
import pathlib
import x


##############################
@get("/<user_username>")
def _(user_username):
  try:
    db = x.db()

    response.add_header("Cache-control", "no-store, no-cache, must-revalidate, max-age=0")
    response.add_header("Pragma", "no-cache")
    response.add_header("Expires",0)

    user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET) #vi vil gerne have fat i en cookie fra browseren der hedder "login" det har vi defineret i login.py
    
    user = db.execute("SELECT * FROM users WHERE user_username=? COLLATE NOCASE",(user_username,)).fetchall()[0]
    user_id = user["user_id"]    

    # Den matcher user_id med tweet_user_fk, så den filtrer hvem der har tweetet hvad - så hp user sidder sammen med hp tweets AND der hvor user_username er lige url'en
    tweets_and_user_data = db.execute("SELECT * FROM tweets,users WHERE tweets.tweet_user_fk = users.user_id AND user_username=? COLLATE NOCASE",(user_username,)).fetchall()

    trends = db.execute("SELECT * FROM trends")

    user_suggested_follows = []
    user_suggested_follows = db.execute("SELECT * FROM users WHERE user_username!=?",(user_username,))

    return template("profile", user=user, tweets_and_user_data=tweets_and_user_data, trends=trends, user_cookie=user_cookie, user_suggested_follows=user_suggested_follows)

  except Exception as ex:
    print(ex)
    response.status = 400
    return {"error": str(ex)}

  finally:
    if "db" in locals(): db.close()
