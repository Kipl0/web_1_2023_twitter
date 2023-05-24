from bottle import post, response, request
import sqlite3
import x


@post("/like-tweet")
def _():
    try:
        # user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET) #vi vil gerne have fat i en cookie fra browseren der hedder "user_cookie" det har vi defineret i login.py
        user_cookie = request.get_cookie("user_cookie", secret="my-secret") #vi vil gerne have fat i en cookie fra browseren der hedder "user_cookie" det har vi defineret i login.py

        if user_cookie is None : 
            return {"info" : "no user logged in"}

        db = x.db()
        tweet_id = request.forms.get("tweet_id")
        
        # User likes tweet --- and therefor view
        tweet_liked_by_user_record = db.execute("SELECT * FROM tweets_liked_by_users WHERE user_id = ? AND tweet_id = ?",(user_cookie["user_id"], tweet_id)).fetchone()



        if tweet_liked_by_user_record == None :
            db.execute("INSERT INTO tweets_liked_by_users VALUES(?,?,?)",(user_cookie["user_id"], tweet_id, 1))
            db.commit()

            tweet_to_like = db.execute("SELECT * FROM tweets WHERE tweet_id = ?",(tweet_id,)).fetchone()
            tweet_total_likes = tweet_to_like["tweet_total_likes"]

            db.execute("UPDATE tweets SET tweet_total_likes = tweet_total_likes + 1 WHERE tweet_id = ?",(tweet_id,))
            db.commit()

            return {"info" : "ok", "tweet_id" : tweet_id, "liked" : 1, "tweet_total_likes" : int(tweet_total_likes) + 1}



        # user har set tweet, men ikke liket det - liker det nu
        if tweet_liked_by_user_record["liked_viewed"] == 0 :
            db.execute("UPDATE tweets_liked_by_users SET liked_viewed = 1 WHERE user_id = ? AND tweet_id = ?",(user_cookie["user_id"], tweet_id))
            db.commit()

            tweet_to_like = db.execute("SELECT * FROM tweets WHERE tweet_id = ?",(tweet_id,)).fetchone()
            tweet_total_likes = tweet_to_like["tweet_total_likes"]

            db.execute("UPDATE tweets SET tweet_total_likes = tweet_total_likes + 1 WHERE tweet_id = ?",(tweet_id,))
            db.commit()
            return {"info" : "ok", "tweet_id" : tweet_id, "liked" : 1, "tweet_total_likes" : int(tweet_total_likes) + 1}



        # Hvis bruger klikker på knap, der returneres resultat, hvor liked ikke er 0 (koden er ikke gået ind i foregående sætninger)
        db.execute("UPDATE tweets_liked_by_users SET liked_viewed = 0 WHERE user_id = ? AND tweet_id = ?",(user_cookie["user_id"], tweet_id))
        db.commit()

        tweet_to_like = db.execute("SELECT * FROM tweets WHERE tweet_id = ?",(tweet_id,)).fetchone()
        tweet_total_likes = tweet_to_like["tweet_total_likes"]

        db.execute("UPDATE tweets SET tweet_total_likes = tweet_total_likes - 1 WHERE tweet_id = ?",(tweet_id,))
        db.commit()


        return {"info" : "ok", "tweet_id" : tweet_id, "liked" : 0, "tweet_total_likes" : int(tweet_total_likes) - 1}


    except Exception as ex:
        try: # Controlled exception, usually comming from the x file
            response.status = ex.args[0]
            return {"info":ex.args[1]}
        except: # Something unknown went wrong
            response.status = 500
            print(ex)
            return {"info":str(ex)}

    finally:
        if "db" in locals(): db.close()

