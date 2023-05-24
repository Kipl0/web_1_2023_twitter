from bottle import get, response, request, template
import sqlite3
import pathlib
import x


@get("/view-tweet/<tweet_id>")
def _(tweet_id):
    try :
        db = x.db()
        response.add_header("Cache-control", "no-store, no-cache, must-revalidate, max-age=0")
        response.add_header("Pragma", "no-cache")
        response.add_header("Expires",0)

        trends = db.execute("SELECT * FROM trends").fetchall()

        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)
        if user_cookie != None:
            who_to_follow = []
            who_to_follow = db.execute("SELECT * FROM users WHERE user_username!=? AND user_username != ? LIMIT 3",(user_cookie["user_username"],"Admin")).fetchall()


            tweet_and_user_data = db.execute("SELECT * FROM tweets,users WHERE tweets.tweet_user_fk = users.user_id AND tweet_id=? COLLATE NOCASE",(tweet_id,)).fetchone()
   

            tweet_comment_and_user_data = db.execute("SELECT * FROM tweet_comments, users WHERE tweet_comments.comment_user_fk = users.user_id AND comment_tweet_fk=? ORDER BY comment_created_at DESC",(tweet_id,)).fetchall()


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


        return template("full_tweet_and_comments", tweet_and_user_data = tweet_and_user_data, tweet_comment_and_user_data=tweet_comment_and_user_data, user_cookie=user_cookie, tweet_comments = tweet_comments, trends = trends, who_to_follow=who_to_follow, TWEET_MIN_LEN=x.TWEET_MIN_LEN, TWEET_MAX_LEN=x.TWEET_MAX_LEN)


    except Exception as ex :
        print(ex)
        response.status = 400
        return {"error": str(ex)}


    finally : 
        if "db" in locals(): db.close()
