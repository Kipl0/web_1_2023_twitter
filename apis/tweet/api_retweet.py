from bottle import post, response, request
import sqlite3
import x
import time

@post("/retweet-tweet")
def _():
    try:
        db = x.db()

        # user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET) #vi vil gerne have fat i en cookie fra browseren der hedder "user_cookie" det har vi defineret i login.py
        user_cookie = request.get_cookie("user_cookie", secret="my-secret") #vi vil gerne have fat i en cookie fra browseren der hedder "user_cookie" det har vi defineret i login.py
        user_cookie = x.validate_jwt(user_cookie) #user_cookie bliver sat lig den decoded JWT - så de nedenstående linjer kan forsætte som de gjorde før JWT kom ind... - se x fil

        if user_cookie is None : 
            return {"info" : "no user logged in"}

        tweet_id = request.forms.get("tweet_to_retweet_id")
        
        # User likes tweet --- and therefor view
        tweet_retweeted_by_user_record = db.execute("SELECT * FROM tweets_retweeted_by_users WHERE user_fk = ? AND tweet_fk = ?",(user_cookie["user_id"], tweet_id)).fetchone()

        retweeted_at = int(time.time())

        # Hvis den ikke eksisterer, har user ikke retweeted tweet
        if tweet_retweeted_by_user_record == None :
            db.execute("INSERT INTO tweets_retweeted_by_users VALUES(?,?,?,?)",(user_cookie["user_id"], tweet_id, 1,retweeted_at))
            db.commit()

            tweet_to_retweet = db.execute("SELECT * FROM tweets WHERE tweet_id = ?",(tweet_id,)).fetchone()
            tweet_total_retweets = tweet_to_retweet["tweet_total_retweets"]

            return {"info" : "ok", "tweet_id" : tweet_id, "retweeted" : 1, "tweet_total_retweets" : int(tweet_total_retweets)}



        # Hvis bruger klikker på knap, der returneres resultat, hvor retweeted ikke er 0 (koden er ikke gået ind i foregående sætninger)
        db.execute("DELETE FROM tweets_retweeted_by_users WHERE user_fk = ? AND tweet_fk = ?",(user_cookie["user_id"], tweet_id))
        db.commit()


        tweet_to_retweet = db.execute("SELECT * FROM tweets WHERE tweet_id = ?",(tweet_id,)).fetchone()
        tweet_total_retweets = tweet_to_retweet["tweet_total_retweets"]


        return {"info" : "ok", "tweet_id" : tweet_id, "retweeted" : 0, "tweet_total_retweets" : int(tweet_total_retweets)}


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

