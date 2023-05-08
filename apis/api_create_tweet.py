from bottle import post, request, response
import x
import uuid
import time
import os

@post("/tweet")
def _():
  try: # SUCCESS
    user_cookie = request.get_cookie("user_cookie", secret="my-secret") #vi vil gerne have fat i en cookie fra browseren der hedder "user_cookie" det har vi defineret i user_cookie.py

    #Upload image to tweets
    uploaded_tweet_image = request.files.get("uploaded_tweet_image") #files i formen
    name, ext = os.path.splitext(uploaded_tweet_image.filename)
    if ext == "" : 
        #Because of enctype the uploaded picture is not "none", but the extension is - so if there's no upload ext will be an empty string or just none
        uploaded_tweet_image_name = ""
        print("no picture chosen")
    else:
        if ext not in(".jpg", ".jpeg", ".png"):
            response.status = 400
            print(ext)
            return "Picture not allowed"
        uploaded_tweet_image_name = str(uuid.uuid4().hex)
        uploaded_tweet_image_name = uploaded_tweet_image_name + ext
        uploaded_tweet_image.save(f"tweet_images/{uploaded_tweet_image_name}")
        # return "Picture uploaded"


    db = x.db() #a function that gives access to db
    
    tweet_id = str(uuid.uuid4().hex) #hex removes everything but numbers and letter - To get a UUID4 without dashess
    tweet_user_fk = user_cookie["user_id"] #meningen er at det skal være den logged in bruger - senere
    tweet_created_at = int(time.time())
    tweet_message = x.validate_tweet_message()
    tweet_image = uploaded_tweet_image_name
    tweet_updated_at = ""
    tweet_total_replies = 0
    tweet_total_retweets = 0
    tweet_total_likes = 0
    tweet_total_views = 0
    db.execute("INSERT INTO tweets VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
               (tweet_id, tweet_user_fk, tweet_created_at, tweet_message, tweet_image, tweet_updated_at, tweet_total_replies, tweet_total_retweets, tweet_total_likes, tweet_total_views))
    db.commit()
    return {"info" : "ok"}
  except Exception as ex: # SOMETHING IS WRONG
    response.status = 400
    return str(ex)
  finally: # This will always take place
    if "db" in locals(): db.close()