from bottle import post, response, request, template
import random
import x

@post("/api-get-latest-tweets")
def _():
   
    try:
        db = x.db()
        tweets_and_user_data = db.execute("SELECT * FROM tweets,users WHERE tweets.tweet_user_fk = users.user_id ORDER BY tweet_created_at DESC").fetchall()
        print(tweets_and_user_data)        
        return {"info": "ok"}

    except Exception as ex:
        print(ex)
        response.status = 500
        return {"error": str(ex)}

    finally:
        if "db" in locals(): db.close()
    # return str(int(random.randint(0, 999)))
    # random number er lig id for id for hvert tweet (bare et vilkårligt tal, ligesom et vilkårligt uuid4 som er id for billede)