from bottle import get, template
import x

@get("/full-tweet-and-comments")
def _():
    try :
        return template("full_tweet_and_comments")

    except Exception as ex :
        pass

    finally : 
        pass