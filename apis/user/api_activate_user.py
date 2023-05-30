from bottle import request, response, post
import x
from apis.messages_to_users.send_info_email import send_info_email

# @post("/activate-user/<username>") Tjekkes ikke i javascript?
@post("/activate-user")
def _(username=None):
    try:
        db = x.db()

        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)

        # Hvis Admin er logget ind
        if user_cookie["user_username"] == "Admin" : 

            user_id = None
            # Ved post sendes attributes som key-values pairs, som tjekkes gennem her indtil den finder en der starter med deactivate_user
            for key in request.forms:
                if key.startswith("activate_user_"):
                    activate_user_id = key.split("_", 2)[2]  # Extract the user_id from the field name
                    break
            

            if activate_user_id != None:
                user_to_activate = db.execute("SELECT * FROM deleted_users WHERE deleted_user_id = ?",(activate_user_id,)).fetchone()
                
                activated_user = {
                    "user_id" : user_to_activate["deleted_user_id"],
                    "user_username" : user_to_activate["deleted_user_username"],
                    "user_email" : user_to_activate["deleted_user_email"],
                    "user_password" : user_to_activate["deleted_user_password"],
                    "user_first_name" : user_to_activate["deleted_user_first_name"],
                    "user_last_name" : user_to_activate["deleted_user_last_name"],
                    "user_avatar" : user_to_activate["deleted_user_avatar"],
                    "user_banner" : user_to_activate["deleted_user_banner"],
                    "user_link" : user_to_activate["deleted_user_link"],
                    "user_caption" : user_to_activate["deleted_user_caption"],
                    "user_location" : user_to_activate["deleted_user_location"],
                    "user_created_at" : user_to_activate["deleted_user_created_at"],
                    "user_total_tweets" : user_to_activate["deleted_user_total_tweets"],
                    "user_total_retweets" : user_to_activate["deleted_user_total_retweets"],
                    "user_total_comments" : user_to_activate["deleted_user_total_comments"],
                    "user_total_likes" : user_to_activate["deleted_user_total_likes"],
                    "user_total_followers" : user_to_activate["deleted_user_total_followers"],
                    "user_total_following" : user_to_activate["deleted_user_total_following"],
                    "user_active" : user_to_activate["deleted_user_active"],
                    "user_twitter_gold" : user_to_activate["deleted_user_twitter_gold"]
                }

                values = ""
                for key in activated_user:
                    values += f':{key},'
                values = values.rstrip(",")


                total_rows_inserted = db.execute(f"INSERT INTO users VALUES({values})", activated_user).rowcount
                db.commit()

                # Hvis det ikke lykkedes at få rækken commited
                if total_rows_inserted != 1 : raise Exception("Please try again")

                # Slet rækken i users, nu hvor den ligger i deleted_users
                db.execute("DELETE FROM deleted_users WHERE deleted_user_id = ?",(user_to_activate["deleted_user_id"],))
                db.commit()

                create_and_send_info_email(reciever_email=user_to_activate["deleted_user_email"])
                
                return {
                    "info" : "ok",
                    "message" : "user activated"
                }
           
        else:
            # Unauthorized access
            response.status = 401  # Forbidden

    except Exception as ex:
        response.status = 401
        print(ex)
        return {"info": str(ex)}

    finally:
        if "db" in locals(): db.close()     


def create_and_send_info_email(reciever_email: str):
    text = f"""\
        Hi!
        You account has been activated again! 
    """
    html = f"""\
    <html>
        <body>
            <h2> Hi! </h2>
            <p>You account has been activated again!</p>
        </body>
    </html>
    """

    send_info_email(reciever_email=reciever_email, message_plain_text=text, message_html=html)
