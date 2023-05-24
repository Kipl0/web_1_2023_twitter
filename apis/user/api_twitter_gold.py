from bottle import request, post, response
import x
import math
import random

@post("/twitter-gold")
def _() :
    try : 
        db = x.db()

        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)

        twitter_gold_email = request.forms.get("twitter_gold_email")

        if twitter_gold_email != user_cookie['user_email'] :
            raise Exception(400, "Email does not match your account")

        if user_cookie != None:
            user_to_twitter_gold = db.execute("SELECT * FROM users WHERE user_email = ?",(user_cookie['user_email'],)).fetchone()
            if user_to_twitter_gold == None :
                raise Exception(400, "Please insert your account's email")
        else :
            raise Exception(400, "Please login")


        sms_confirm_digits = math.floor(1000+random.random()*9000)
        
        print("1")
        twitter_gold_user_and_key = db.execute("SELECT * FROM twitter_gold_keys WHERE user_fk = ?",(user_cookie['user_id'],)).fetchone()
        if twitter_gold_user_and_key == None :
            print("2")
            db.execute("INSERT INTO twitter_gold_keys VALUES(?, ?)",(sms_confirm_digits, user_cookie['user_id']))
            db.commit()
        else :
            print("3")
            db.execute("UPDATE twitter_gold_keys SET verification_key = ? WHERE user_fk = ?", (sms_confirm_digits, user_cookie['user_id']))
            db.commit()

        print("4")
        print(sms_confirm_digits)
        return{"info":"ok", "sms_confirm_digits":sms_confirm_digits}

    except Exception as ex :
        print(ex)
        response.status = 400
        return {"error": str(ex)}


    finally :
        if "db" in locals() : db.close()
