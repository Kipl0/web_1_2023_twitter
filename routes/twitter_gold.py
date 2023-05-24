from bottle import get, response, request, template
import x

@get("/twitter-gold")
def _() :
    try :
        db = x.db()

        response.add_header("Cache-control", "no-store, no-cache, must-revalidate, max-age=0")
        response.add_header("Pragma", "no-cache")
        response.add_header("Expires",0)

        user_cookie = request.get_cookie("user_cookie", secret="my-secret") #vi vil gerne have fat i en cookie fra browseren der hedder "user_cookie" det har vi defineret i login.py

        who_to_follow = []
        if user_cookie != None:
            who_to_follow = db.execute("SELECT * FROM users WHERE user_username!=? AND user_username != ? LIMIT 3",(user_cookie["user_username"],"Admin"))

        trends = db.execute("SELECT * FROM trends")

        return template("twitter_gold", user_cookie=user_cookie, who_to_follow=who_to_follow, trends=trends, TWEET_MIN_LEN=x.TWEET_MIN_LEN, TWEET_MAX_LEN=x.TWEET_MAX_LEN)

    except Exception as ex :
        print(ex)
        response.status = 400
        return {"error": str(ex)}



    finally : 
        if "db" in locals() : db.close()