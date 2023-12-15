from bottle import get, response, request, template
import sqlite3
import pathlib
import x
import time
from datetime import datetime


# I want to display the index page, I want to pass the title, tweets and trends
@get("/")
def render_frontpage():
  try:
    db = x.db()

    response.add_header("Cache-control", "no-store, no-cache, must-revalidate, max-age=0")
    response.add_header("Pragma", "no-cache")
    response.add_header("Expires",0)


    user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET) #vi vil gerne have fat i en cookie fra browseren der hedder "user_cookie" det har vi defineret i login.py
    user_cookie = x.validate_jwt(user_cookie) #user_cookie bliver sat lig den decoded JWT - så de nedenstående linjer kan forsætte som de gjorde før JWT kom ind... - se x fil
    
    trends = db.execute("SELECT * FROM trends")
    # Redirect til login, hvis ikke man har login
    if user_cookie == None:
      response.status = 303
      response.set_header("Location", "/login")
      return


    # Vis farverne på de tweets der er liket og dem der ikke er liket ved load af siden
    if user_cookie != None : 
      who_to_follow = []
      who_to_follow = db.execute("SELECT * FROM users WHERE user_username!=? AND user_username != ? LIMIT 3",(user_cookie["user_username"],"Admin"))


      tweets_and_user_data = db.execute("SELECT * FROM tweets INNER JOIN users ON tweets.tweet_user_fk = users.user_id ORDER BY tweet_created_at DESC").fetchall()
      retweets_and_user_data = db.execute("SELECT * FROM tweets,users,tweets_retweeted_by_users WHERE tweets.tweet_user_fk = users.user_id AND tweets_retweeted_by_users.tweet_fk = tweets.tweet_id COLLATE NOCASE ORDER BY tweet_created_at DESC").fetchall()

      # Key value pair, der sepererer retweet_tweets fra originale tweets - så begge to kan få grøn ikon og grøn tekst
      for tweet_original in tweets_and_user_data :
        tweet_original['original_tweet'] = 1
        tweet_original['retweeted_by'] = ""
      for tweet_retweeted in retweets_and_user_data :
        retweeted_by = db.execute("SELECT user_username FROM users WHERE user_id = ?",(tweet_retweeted['user_fk'],)).fetchone() # loop igennem alle retweets og sæt retweeted by
        tweet_retweeted['retweeted_by'] = retweeted_by['user_username'] # tilføj den som key-value par til hver retweet i tabellen
        tweet_retweeted['original_tweet'] = 0



      # Retweets
      for tweet in tweets_and_user_data :
        tweet_retweeted_by_user_record = db.execute("SELECT * FROM tweets_retweeted_by_users WHERE user_fk = ? AND tweet_fk = ?",(user_cookie["user_id"], tweet["tweet_id"])).fetchone()

        # Hvis den er lig 1 betyder det at user har liket tweet  # Hvis ikke tweet_liked_by_user_record eksisterer i db, så har user hverken set eller liket opslaget før
        if tweet_retweeted_by_user_record == None : 
          tweet["retweeted"] = 0
          continue

        if tweet_retweeted_by_user_record["retweeted"] == 1 :
          # Add the key "liked_viewed" to the dict so that it will be: # {'tweet_id': '1', 'tweet_text': 'mit tweet', 'total_likes': '11', 'liked': 1}
          tweet["retweeted"] = 1
          continue
        tweet["retweeted"] = 1

      
        # merch tweets_and_user_data with retweets_and_user_data
        combined_data = tweets_and_user_data + retweets_and_user_data
        tweets_and_user_data = sorted(combined_data, key=lambda x: x.get("retweeted_at", x["tweet_created_at"]), reverse=True)


      for tweet in tweets_and_user_data :
        tweet_liked_by_user_record = db.execute("SELECT * FROM tweets_liked_by_users WHERE user_id = ? AND tweet_id = ?",(user_cookie["user_id"], tweet["tweet_id"])).fetchone()
          # Hvis den er lig 1 betyder det at user har liket tweet # Hvis ikke tweet_liked_by_user_record eksisterer i db, så har user hverken set eller liket opslaget før
        if tweet_liked_by_user_record == None : 
          tweet["liked_viewed"] = 0
          continue


        if tweet_liked_by_user_record["liked_viewed"] == 1 :
          # Add the key "liked_viewed" to the dict so that it will be: # {'tweet_id': '1', 'tweet_text': 'mit tweet', 'total_likes': '11', 'liked': 1}
          tweet["liked_viewed"] = 1
          continue
        tweet["liked_viewed"] = 0

      # Hvs bruger har kommenteret på tweet, så hvis blå aktiv farve ved load
      for tweet in tweets_and_user_data :
        tweet_comments = db.execute("SELECT * FROM tweet_comments WHERE comment_user_fk = ? AND comment_tweet_fk = ?",(user_cookie["user_id"], tweet["tweet_id"])).fetchone()
        # Hvis den findes betyder det at user har kommenteret på tweet # laver nyt key-value pair hvor den er 0 eller 1
        if tweet_comments == None : 
          tweet["commented"] = 0
          continue

        tweet["commented"] = 1


      # ##########################
      # Omskriv til dato
      for tweet in tweets_and_user_data : 
        datetime_obj = datetime.fromtimestamp(int(tweet['tweet_created_at']))
        datetime_string=datetime_obj.strftime( "%b-%d") # "%d-%m-%Y %H:%M:%S"
        tweet['created_at_datetime'] = datetime_string
      
      # Looper igennem tweets_and_user_data og viser kun de første tweets
      tweets_and_user_data = tweets_and_user_data[0:10]

      return template("frontpage", title="Twitter", tweets_and_user_data=tweets_and_user_data, user_cookie=user_cookie, trends=trends, who_to_follow=who_to_follow, page="frontpage", TWEET_MIN_LEN=x.TWEET_MIN_LEN, TWEET_MAX_LEN=x.TWEET_MAX_LEN)

    return template("frontpage", title="Twitter", trends=trends, user_cookie=user_cookie, page="frontpage", TWEET_MIN_LEN=x.TWEET_MIN_LEN, TWEET_MAX_LEN=x.TWEET_MAX_LEN)


  except Exception as ex:
    print(ex)
    response.status = 400
    return {"error": str(ex)}

  finally:
    if "db" in locals(): db.close()
