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
    tweets_and_user_data = db.execute("SELECT * FROM tweets,users WHERE tweets.tweet_user_fk = users.user_id AND user_username=? COLLATE NOCASE ORDER BY tweet_created_at DESC LIMIT 10",(user_username,)).fetchall()
    
    trends = db.execute("SELECT * FROM trends")

    user_suggested_follows = []
    user_suggested_follows = db.execute("SELECT * FROM users WHERE user_username!=?",(user_username,))


    # Vis farverne på de tweets der er liket og dem der ikke er liket ved load af siden
    for tweet in tweets_and_user_data :
      tweet_liked_by_user_record = db.execute("SELECT * FROM tweets_liked_by_users WHERE user_id = ? AND tweet_id = ?",(user_cookie["user_id"], tweet["tweet_id"])).fetchone()
        # Hvis den er lig 1 betyder det at user har liket tweet
        # Hvis ikke tweet_liked_by_user_record eksisterer i db, så har user hverken set eller liket opslaget før
      if tweet_liked_by_user_record == None : 
        tweet["liked"] = 0
        continue

      if tweet_liked_by_user_record["liked"] == 1 :
        # Add the key "liked" to the dict so that it will be:
        # {'tweet_id': '1', 'tweet_text': 'mit tweet', 'total_likes': '11', 'liked': 1}
        tweet["liked"] = 1
        continue
      tweet["liked"] = 0


    return template("profile", user=user, tweets_and_user_data=tweets_and_user_data, trends=trends, user_cookie=user_cookie, user_suggested_follows=user_suggested_follows)

  except Exception as ex:
    print(ex)
    response.status = 400
    return {"error": str(ex)}

  finally:
    if "db" in locals(): db.close()
