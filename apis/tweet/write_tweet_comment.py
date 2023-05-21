from bottle import request, response, post
import x
import json

@post("/write-tweet-comment")
def _():
    try:
        db = x.db()
        tweet_to_comment_on = request.forms.get("tweet_id")

        tweets_and_user_data = db.execute("SELECT * FROM tweets, users WHERE tweets.tweet_user_fk = users.user_id AND tweet_id = ?", (tweet_to_comment_on,)).fetchone()


        # Man kan ikke returnere en dictionary i en dictionary som json (den hentes som json i js) - derfor bruges json.dumps i python og parse i js
        # fordi password er hashed er det et byte objekt og derfor ikke validt json, så det bliver decoded til string her.
        tweets_and_user_data['user_password'] = tweets_and_user_data['user_password'].decode('utf-8')
        
        return {"info": "ok", "tweets_and_user_data": json.dumps(tweets_and_user_data)}

    except Exception as ex:
        response.status = 401  # Internal Server Error
        return json.dumps({"error": str(ex)})

    finally:
        pass
