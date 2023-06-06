from bottle import get, response, request, template
import sqlite3
import pathlib
import x
import time
from datetime import datetime

@get("/view-tweet/<tweet_id>")
def _(tweet_id):
    try :
        db = x.db()
        response.add_header("Cache-control", "no-store, no-cache, must-revalidate, max-age=0")
        response.add_header("Pragma", "no-cache")
        response.add_header("Expires",0)

        trends = db.execute("SELECT * FROM trends").fetchall()

        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)
        user_cookie = x.validate_jwt(user_cookie) #user_cookie bliver sat lig den decoded JWT - så de nedenstående linjer kan forsætte som de gjorde før JWT kom ind... - se x fil


        # Redirect til login, hvis ikke man har login
        if user_cookie == None:
            response.status = 303
            response.set_header("Location", "/login")
            return


        if user_cookie != None:
            who_to_follow = []
            who_to_follow = db.execute("SELECT * FROM users WHERE user_username!=? AND user_username != ? LIMIT 3",(user_cookie["user_username"],"Admin")).fetchall()

            tweet_and_user_data = db.execute("SELECT * FROM tweets,users WHERE tweets.tweet_user_fk = users.user_id AND tweet_id=? COLLATE NOCASE",(tweet_id,)).fetchone()
            tweet_comment_and_user_data = db.execute("SELECT * FROM tweet_comments, users WHERE tweet_comments.comment_user_fk = users.user_id AND comment_tweet_fk=? ORDER BY comment_created_at DESC",(tweet_id,)).fetchall()
            tweet_retweeted_by_user_record = db.execute("SELECT * FROM tweets_retweeted_by_users WHERE user_fk = ? AND tweet_fk = ?",(user_cookie["user_id"], tweet_and_user_data["tweet_id"])).fetchone()
            
            # Hvis den er lig 1 betyder det at user har liket tweet  # Hvis ikke tweet_liked_by_user_record eksisterer i db, så har user hverken set eller liket opslaget før
            if tweet_retweeted_by_user_record == None : 
                tweet_and_user_data["retweeted"] = 0
                tweet_and_user_data["retweeted_by"] = ""
                tweet_and_user_data["original_tweet"] = 1
                
            elif tweet_retweeted_by_user_record["retweeted"] == 1 :
                # Add the key "liked_viewed" to the dict so that it will be: # {'tweet_id': '1', 'tweet_text': 'mit tweet', 'total_likes': '11', 'liked': 1}
                tweet_and_user_data["retweeted"] = 1 
                retweeted_by = db.execute("SELECT user_username FROM users WHERE user_id = ?",(tweet_retweeted_by_user_record['user_fk'],)).fetchone() # loop igennem alle retweets og sæt retweeted by
                tweet_and_user_data["retweeted_by"] = retweeted_by['user_username']
                tweet_and_user_data["original_tweet"] = 0
            else :
                tweet_and_user_data["retweeted"] = 1
                retweeted_by = db.execute("SELECT user_username FROM users WHERE user_id = ?",( ['user_fk'],)).fetchone() # loop igennem alle retweets og sæt retweeted by
                tweet_and_user_data["retweeted_by"] = retweeted_by['user_username']
                tweet_and_user_data["original_tweet"] = 0
                
            # Vis farverne på de tweets der er liket og dem der ikke er liket ved load af siden
            tweet_liked_by_user_record = db.execute("SELECT * FROM tweets_liked_by_users WHERE user_id = ? AND tweet_id = ?",(user_cookie["user_id"], tweet_and_user_data["tweet_id"])).fetchone()

            # Når man klikker ind på siden, så har man set tweet (hvis man har liket, har man allerede set 0/1 bool)
            # Hvis den er lig 1 betyder det at user har liket tweet # Hvis ikke tweet_liked_by_user_record eksisterer i db, så har user hverken set eller liket opslaget før
            if tweet_liked_by_user_record == None : 
                if user_cookie['user_id'] != tweet_and_user_data['user_id'] :
                    db.execute("INSERT INTO tweets_liked_by_users VALUES(?,?,?)",(user_cookie['user_id'], tweet_id, 0))
                    db.commit()
                    tweet_and_user_data["liked_viewed"] = 0
                    tweet_and_user_data["tweet_total_views"] = int(tweet_and_user_data["tweet_total_views"]) + 1
                else :
                    tweet_and_user_data["liked_viewed"] = 0

            elif tweet_liked_by_user_record["liked_viewed"] == 1 :
                # Add the key "liked_viewed" to the dict so that it will be: # {'tweet_id': '1', 'tweet_text': 'mit tweet', 'total_likes': '11', 'liked': 1}
                tweet_and_user_data["liked_viewed"] = 1
            else : 
                tweet_and_user_data["liked_viewed"] = 0


            # Hvs bruger har kommenteret på tweet, så hvis blå aktiv farve ved load
            tweet_comments = db.execute("SELECT * FROM tweet_comments WHERE comment_user_fk = ? AND comment_tweet_fk = ?",(user_cookie["user_id"], tweet_and_user_data["tweet_id"])).fetchone()
            # Hvis den findes betyder det at user har kommenteret på tweet # laver nyt key-value pair hvor den er 0 eller 1
            if tweet_comments == None : 
                tweet_and_user_data["commented"] = 0
            else:
                tweet_and_user_data["commented"] = 1



            # ##########################
            # Omskriv tweet_created_at Epoch til dato 
            datetime_obj = datetime.fromtimestamp(int(tweet_and_user_data['tweet_created_at']))
            datetime_string=datetime_obj.strftime( "%b-%d") # "%d-%m-%Y %H:%M:%S"
            tweet_and_user_data['created_at_datetime'] = datetime_string



            # Omskriv comment_created_at Epoch til dato 
            for comment in tweet_comment_and_user_data : 
                comment_datetime_obj = datetime.fromtimestamp(int(comment['comment_created_at']))
                comment_datetime_string=comment_datetime_obj.strftime( "%b-%d") # "%d-%m-%Y %H:%M:%S"
                comment['created_at_datetime'] = comment_datetime_string


        return template("full_tweet_and_comments", tweet_and_user_data = tweet_and_user_data, tweet_comment_and_user_data=tweet_comment_and_user_data, user_cookie=user_cookie, tweet_comments = tweet_comments, trends = trends, who_to_follow=who_to_follow, TWEET_MIN_LEN=x.TWEET_MIN_LEN, TWEET_MAX_LEN=x.TWEET_MAX_LEN)


    except Exception as ex :
        print(ex)
        response.status = 400
        return {"error": str(ex)}


    finally : 
        if "db" in locals(): db.close()
