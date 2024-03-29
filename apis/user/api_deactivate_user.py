from bottle import request, response, post
import x
from apis.messages_to_users.send_info_email import send_info_email

@post("/deactivate-user/<username>")
@post("/deactivate-user")  # Route without a specific username for admin access
def _(username=None):
    try:
        db = x.db()

        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)
        user_cookie = x.validate_jwt(user_cookie) #user_cookie bliver sat lig den decoded JWT - så de nedenstående linjer kan forsætte som de gjorde før JWT kom ind... - se x fil


        # Hvis Admin er logget ind
        if user_cookie["user_username"] == "Admin" or username is not None and user_cookie["user_username"] == username : 

            deactivate_user_id = None
            # Ved post sendes attributes som key-values pairs, som tjekkes gennem her indtil den finder en der starter med deactivate_user
            for key in request.forms:
                if key.startswith("deactivate_user_"):
                    deactivate_user_id = key.split("_", 2)[2]  # Extract the user_id from the field name
                    break
            

            if deactivate_user_id != None:
                user_to_deactivate = db.execute("SELECT * FROM users WHERE user_id = ?",(deactivate_user_id,)).fetchone()
                
                deactivated_user = {
                    "deleted_user_id" : user_to_deactivate["user_id"],
                    "deleted_user_username" : user_to_deactivate["user_username"],
                    "deleted_user_email" : user_to_deactivate["user_email"],
                    "deleted_user_password" : user_to_deactivate["user_password"],
                    "deleted_user_first_name" : user_to_deactivate["user_first_name"],
                    "deleted_user_last_name" : user_to_deactivate["user_last_name"],
                    "deleted_user_avatar" : user_to_deactivate["user_avatar"],
                    "deleted_user_banner" : user_to_deactivate["user_banner"],
                    "deleted_user_link" : user_to_deactivate["user_link"],
                    "deleted_user_caption" : user_to_deactivate["user_caption"],
                    "deleted_user_location" : user_to_deactivate["user_location"],
                    "deleted_user_created_at" : user_to_deactivate["user_created_at"],
                    "deleted_user_total_tweets" : user_to_deactivate["user_total_tweets"],
                    "deleted_user_total_retweets" : user_to_deactivate["user_total_retweets"],
                    "deleted_user_total_comments" : user_to_deactivate["user_total_comments"],
                    "deleted_user_total_likes" : user_to_deactivate["user_total_likes"],
                    "deleted_user_total_followers" : user_to_deactivate["user_total_followers"],
                    "deleted_user_total_following" : user_to_deactivate["user_total_following"],
                    "deleted_user_active" : user_to_deactivate["user_active"],
                    "deleted_user_twitter_gold" : user_to_deactivate["user_twitter_gold"]
                }

                values = ""
                for key in deactivated_user:
                    values += f':{key},'
                values = values.rstrip(",")


                total_rows_inserted = db.execute(f"INSERT INTO deleted_users VALUES({values})", deactivated_user).rowcount
                db.commit()

                # Hvis det ikke lykkedes at få rækken commited
                if total_rows_inserted != 1 : raise Exception("Please try again")

                # Slet rækken i users, nu hvor den ligger i deleted_users
                db.execute("DELETE FROM users WHERE user_id = ?",(user_to_deactivate["user_id"],))
                db.commit()

                create_and_send_info_email(reciever_email=user_to_deactivate["user_email"])

                return {
                    "info" : "ok",
                    "message" : "user deactivated"
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
        We regret to inform you, that your account has been deactivated.
    """
    html = f"""\
    <html>
        <body>
            <h2> Hi! </h2>
            <p>We regret to inform you, that your account has been deactivated.</p>
        </body>
    </html>
    """

    send_info_email(reciever_email=reciever_email, message_plain_text=text, message_html=html)
