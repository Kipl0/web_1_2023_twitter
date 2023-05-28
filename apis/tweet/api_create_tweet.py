from bottle import post, request, response, HTTPResponse
import x
import uuid
import time
import os
import json

@post("/tweet")
def _():
  try:
    import production #If this production is found, the next line should run
    rootdir = "/home/Kipl0/mysite/"     
  except Exception as ex:    
    rootdir = "C:/Users/maalm/Documents/kea/web_1_2023_twitter/"

  try:  # SUCCESS
    db = x.db()  # a function that gives access to db

    user_cookie = request.get_cookie("user_cookie", secret="my-secret")

    uploaded_tweet_image = request.files.get("uploaded_create_tweet_img_input")

    if uploaded_tweet_image != None:
      name, ext = os.path.splitext(uploaded_tweet_image.filename)

      if ext == "":
        uploaded_tweet_image_name = ""
        # print("No picture chosen")
      else:
        if ext not in (".jpg", ".jpeg", ".png"):
          response.status = 400
          print(ext)
          return "Picture not allowed"
        uploaded_tweet_image_name = str(uuid.uuid4().hex)
        uploaded_tweet_image_name = uploaded_tweet_image_name + ext
        print("Saving image")
        uploaded_tweet_image.save(f"{rootdir}tweet_images/{uploaded_tweet_image_name}")
        print("Image saved")
        # return "Picture uploaded"
    else:
      uploaded_tweet_image_name = ""
    tweet_id = str(uuid.uuid4().hex)
    tweet_user_fk = user_cookie["user_id"]
    tweet_created_at = int(time.time())
    tweet_updated_at = ""
    tweet_total_comments = 0
    tweet_total_retweets = 0
    tweet_total_likes = 0
    tweet_total_views = 0

    # Check if tweet contains a message
    tweet_message = request.forms.get("tweet_message")
    if tweet_message:
      tweet_message = tweet_message.strip()

    tweet_image = uploaded_tweet_image_name if uploaded_tweet_image_name else ""

    if not tweet_message and not tweet_image:
      error_message = "Please provide a message or an image."
      # print(error_message)
      response.status = 400
      return {"error": error_message}

    db.execute("INSERT INTO tweets VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (tweet_id, tweet_user_fk, tweet_created_at, tweet_message, tweet_image, tweet_updated_at,
                tweet_total_comments, tweet_total_retweets, tweet_total_likes, tweet_total_views))
    db.commit()
    return {"info": "ok"}

  except Exception as ex:  # SOMETHING IS WRONG
    error_message = str(ex)
    return {"error": error_message}

  finally:  # This will always take place
    if "db" in locals():
      db.close()