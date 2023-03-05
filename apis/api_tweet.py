
from bottle import post, request, response
import x
import uuid
import time

@post("/tweet")
def _():
  try: # SUCCESS
    x.validate_tweet()
    db = x.db() #a function that gives access to db
    
    tweet_id = str(uuid.uuid4().hex) #hex removes everything but numbers and letter - To get a UUID4 without dashess
    tweet_user_fk = "07578f6c49d84b7c94ce80e96c64ccc0" #meningen er at det skal være den logged in bruger - senere
    tweet_created_at = int(time.time())
    tweet_message = request.forms.get("message")
    tweet_image = ""
    tweet_updated_at = ""
    tweet_total_replies = ""
    tweet_total_retweets = ""
    tweet_total_likes = ""
    tweet_total_views = ""
    db.execute("INSERT INTO tweets VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
               (tweet_id, tweet_user_fk, tweet_created_at, tweet_message, tweet_image, tweet_updated_at, tweet_total_replies, tweet_total_retweets, tweet_total_likes, tweet_total_views))
    db.commit()
    return {"info" : "ok"}
  except Exception as ex: # SOMETHING IS WRONG
    response.status = 400
    return str(ex)
  finally: # This will always take place
    if "db" in locals(): db.close()