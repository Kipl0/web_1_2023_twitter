from bottle import get, request, template
import x

@get("/full-tweet-and-comments")
def _():
    try :
        db = x.db()

        trends = db.execute("SELECT * FROM trends").fetchall()

        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)

        who_to_follow = []
        if user_cookie != None:
            who_to_follow = db.execute("SELECT * FROM users WHERE user_username!=? AND user_username != ? LIMIT 3",(user_cookie["user_username"],"Admin")).fetchall()
        
        return template("full_tweet_and_comments", user_cookie = user_cookie, trends = trends, who_to_follow = who_to_follow)

    except Exception as ex :
        pass

    finally : 
        pass


