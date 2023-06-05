from bottle import post, request, response
import x

@post("/confirm-twitter-gold")
def _():
    try:
        db = x.db()

        twitter_gold_confirm_number = request.forms.get("twitter_gold_confirm_number")

        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)
        user_cookie = x.validate_jwt(user_cookie) #user_cookie bliver sat lig den decoded JWT - så de nedenstående linjer kan forsætte som de gjorde før JWT kom ind... - se x fil


        if user_cookie != None :
            twitter_gold_user_and_key = db.execute("SELECT * FROM twitter_gold_keys WHERE verification_key = ? AND user_fk = ?",(twitter_gold_confirm_number,user_cookie['user_id'])).fetchone()
            if twitter_gold_user_and_key != None :
                db.execute("UPDATE users SET user_twitter_gold = 1 WHERE user_id = ?",(user_cookie['user_id'],))
                db.commit()

                db.execute("DELETE FROM twitter_gold_keys WHERE user_fk = ?",(user_cookie['user_id'],))
                db.commit()

        else : 
            raise Exception(400, "You must be logged in")

        return {"info":"ok"}

    except Exception as ex :
        print(ex)
        response.status = 400
        return {"error": str(ex)}


    finally :
        if "db" in locals() : db.close()