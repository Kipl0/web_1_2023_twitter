from bottle import get, request, response, post
import x
import json
import uuid
import os
import time

@get("/write-tweet-comment-pop-up/<tweet_id>")
def _(tweet_id):
    try:
        db = x.db()

        tweets_and_user_data = db.execute("SELECT * FROM tweets, users WHERE tweets.tweet_user_fk = users.user_id AND tweet_id = ?", (tweet_id,)).fetchone()

        # Man kan ikke returnere en dictionary i en dictionary som json (den hentes som json i js) - derfor bruges json.dumps i python og parse i js
        # fordi password er hashed er det et byte objekt og derfor ikke validt json, så det bliver decoded til string her.
        tweets_and_user_data['user_password'] = tweets_and_user_data['user_password'].decode('utf-8')
        
        ## når bruger 

        return {"info": "ok", "tweets_and_user_data": json.dumps(tweets_and_user_data)}

    except Exception as ex:
        response.status = 401  # Internal Server Error
        return json.dumps({"error": str(ex)})

    finally:
        pass



@post("/write-tweet-comment")
def _():
    try:
        db = x.db()

        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)

        tweet_to_comment_on_id = request.forms.get("tweet_id")
        print(tweet_to_comment_on_id)

        tweet_comment_user_input = request.forms.get("tweet_comment_user_input")
        if tweet_comment_user_input:
            tweet_comment_user_input = tweet_comment_user_input.strip()
        else : tweet_comment_user_input = ""


         # Upload image to tweet comment
        uploaded_comment_img_input = request.files.get("uploaded_comment_img_input")
        name, ext = os.path.splitext(uploaded_comment_img_input.filename)
        if ext == "":
            # No file uploaded, man må gerne ikke uploade et billede
            uploaded_comment_img_to_save = ""
            print("no file chosen")
        else:
            if ext not in (".jpg", ".jpeg", ".png"):
                response.status = 400
                return "Picture not allowed"
            uploaded_comment_img_to_save = str(uuid.uuid4().hex) + ext
            uploaded_comment_img_input.save(f"comment_images/{uploaded_comment_img_to_save}")

        # Der skal enten være text eller billede eller begge

        comment_image = uploaded_comment_img_to_save if uploaded_comment_img_to_save else ""

        if not tweet_comment_user_input and not comment_image:
            raise Exception
            



        comment_id = str(uuid.uuid4().hex)
        # comment_tweet_fk = tweet_to_comment_on_id #tidligere defineret
        comment_user_fk = user_cookie["user_id"]
        comment_message = tweet_comment_user_input
        # comment_image #tidligere defineret linje 63
        comment_created_at = int(time.time())

        db.execute("INSERT INTO tweet_comments VALUES(?, ?, ?, ?, ?, ?)",(comment_id, tweet_to_comment_on_id, comment_user_fk, comment_message, comment_image, comment_created_at))
        db.commit()

        tweet_to_comment_on = db.execute("SELECT * FROM tweets WHERE tweet_id=?",(tweet_to_comment_on_id,)).fetchone()
        tweet_total_comments = tweet_to_comment_on["tweet_total_comments"]

        return {"info": "ok", "tweet_id": tweet_to_comment_on_id, "tweet_total_comments": int(tweet_total_comments)}

    except Exception as ex:
        response.status = 401  # Internal Server Error
        return json.dumps({"error": str(ex)})

    finally:
        pass
