from bottle import get, response, request, template
import sqlite3
import pathlib
import x


############################## you want to display the index page, you want to pass the title, tweets and trends
@get("/")
def render_frontpage():
  try:


    db = x.db()

    response.add_header("Cache-control", "no-store, no-cache, must-revalidate, max-age=0")
    response.add_header("Pragma", "no-cache")
    response.add_header("Expires",0)

    user_cookie = request.get_cookie("user_cookie", secret="my-secret") #vi vil gerne have fat i en cookie fra browseren der hedder "user_cookie" det har vi defineret i login.py

    user_suggested_follows = []
    if user_cookie != None:
      user_suggested_follows = db.execute("SELECT * FROM users WHERE user_username!=? LIMIT 3",(user_cookie["user_username"],))

    trends = db.execute("SELECT * FROM trends")

    tweets_and_user_data = db.execute("SELECT * FROM tweets,users WHERE tweets.tweet_user_fk = users.user_id ORDER BY tweet_created_at DESC").fetchall()


    print(tweets_and_user_data)
    if user_cookie != None : 
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


    return template("frontpage", title="Twitter", tweets_and_user_data=tweets_and_user_data, user_cookie=user_cookie, trends=trends, user_suggested_follows=user_suggested_follows, TWEET_MIN_LEN=x.TWEET_MIN_LEN, TWEET_MAX_LEN=x.TWEET_MAX_LEN)
    

  except Exception as ex:
    print(ex)
    response.status = 400
    return {"error": str(ex)}

  finally:
    if "db" in locals(): db.close()
