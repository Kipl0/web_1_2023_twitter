from bottle import post, request, response
import x

@post("/confirm-self-deactivate-profile/<deactivate_key>")
def _(deactivate_key):
    try:
        db = x.db()
        # print(deactivate_key)

        user_and_key_to_deactivate = db.execute("SELECT * FROM accounts_to_self_deactivate WHERE deactivate_key = ?",(deactivate_key,)).fetchone()
        print(user_and_key_to_deactivate)

        if user_and_key_to_deactivate != None:
            user_to_deactivate = db.execute("SELECT * FROM users WHERE user_id = ?",(user_and_key_to_deactivate['user_fk'],)).fetchone()        
            print(user_to_deactivate)

        if user_to_deactivate != None :
            print(user_to_deactivate)
            print("1")
            user_to_deleted_users = {
                "deleted_user_id" : user_to_deactivate['user_id'],
                "deleted_user_username" : user_to_deactivate['user_username'],
                "deleted_user_email" : user_to_deactivate['user_email'],
                "deleted_user_password" : user_to_deactivate['user_password'],
                "deleted_user_first_name" : user_to_deactivate['user_first_name'],
                "deleted_user_last_name" : user_to_deactivate['user_last_name'],
                "deleted_user_avatar" : user_to_deactivate['user_avatar'],
                "deleted_user_banner" : user_to_deactivate['user_banner'],
                "deleted_user_link" : user_to_deactivate['user_link'],
                "deleted_user_caption" : user_to_deactivate['user_caption'],
                "deleted_user_location" : user_to_deactivate['user_location'],
                "deleted_user_created_at" : user_to_deactivate['user_created_at'],
                "deleted_user_total_tweets" : user_to_deactivate['user_total_tweets'],
                "deleted_user_total_retweets" : user_to_deactivate['user_total_retweets'],
                "deleted_user_total_comments" : user_to_deactivate['user_total_comments'],
                "deleted_user_total_likes" : user_to_deactivate['user_total_likes'],
                "deleted_user_total_followers" : user_to_deactivate['user_total_followers'],
                "deleted_user_total_following" : user_to_deactivate['user_total_following'],
                "deleted_user_active" : user_to_deactivate['user_active'],
                "deleted_user_twitter_gold" : user_to_deactivate['user_twitter_gold']
            }


            values = ""
            for key in user_to_deleted_users:
                values += f':{key},'
            values = values.rstrip(",")

            total_rows_inserted = db.execute(f"INSERT INTO deleted_users VALUES({values})", user_to_deleted_users).rowcount
            db.commit()

            if total_rows_inserted != 1 : raise Exception("Please try again")

            db.execute("DELETE FROM users WHERE user_id = ?",(user_and_key_to_deactivate['user_fk'],))
            db.commit()

            db.execute("DELETE FROM accounts_to_self_deactivate WHERE user_fk = ?",(user_and_key_to_deactivate['user_fk'],))
            db.commit()

            response.set_cookie("user_cookie", "", expires=0)

        else: #den eksisterer ikke i db
            print("Verification_key does not exist in the database")
            raise Exception(400, "Verification_key does not exist in the database")

        return{"info":"ok"}
        

    except Exception as ex:
        print(ex)
        response.status = 400
        return {"error": str(ex)}



    finally :
        if "db" in locals() : db.close()
