from bottle import get, template
import x

tweets = [
    {"tweet_id":"1", "tweet_message":"a"},
    {"tweet_id":"2", "tweet_message":"b"},
    {"tweet_id":"3", "tweet_message":"c"}
]

@get("/tweet")
def _(): 
    return template("tweet", tweets=tweets, TWEET_MIN_LEN=x.TWEET_MIN_LEN, TWEET_MAX_LEN=x.TWEET_MAX_LEN)