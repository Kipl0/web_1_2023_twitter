from bottle import post, request, response
import x

@post("/follow-unfollow")
def _():
    try :
        db = x.db()

        # Simulerer user_cookie -- lig Maja user
        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)
        user_cookie_id = user_cookie["user_id"]

        user_to_follow_id = request.forms.get("user_id")
        user = db.execute("SELECT * FROM users WHERE user_id = ?",(user_to_follow_id,)).fetchone()

        user_total_followers = user["user_total_followers"]
        follower_following_record = db.execute("SELECT * FROM follower_following WHERE follower_id = ? AND following_id = ?",(user_cookie_id, user_to_follow_id)).fetchone()

        # Hvis pk IKKE findes i tabel - follow
        if follower_following_record == None : 
            db.execute("INSERT INTO follower_following VALUES(?,?)",(user_cookie_id, user_to_follow_id))
            db.commit()
            db.execute("UPDATE users SET user_total_followers = user_total_followers + 1 WHERE user_id = ?",(user_to_follow_id,))
            db.commit()
            return {"info":"ok", "user_id" : user_to_follow_id, "follows" : 1, "user_total_followers" : int(user_total_followers) + 1}
    
        # Hvis pk findes i tabel - stop med at follow
        db.execute("DELETE FROM follower_following WHERE follower_id = ? AND following_id = ?",(user_cookie_id,user_to_follow_id))
        db.commit()
        db.execute("UPDATE users SET user_total_followers = user_total_followers - 1 WHERE user_id = ?",(user_to_follow_id,))
        db.commit()
        return {"info":"ok", "user_id" : user_to_follow_id, "follows" : 0, "user_total_followers" : int(user_total_followers) - 1}

  


    except Exception as ex :
        try: # Controlled exception, usually comming from the x file
            response.status = ex.args[0]
            return {"info":ex.args[1]}
        except: # Something unknown went wrong
            response.status = 500
            print(ex)
            return {"info":str(ex)}

    finally :
        if "db" in locals() : db.close()