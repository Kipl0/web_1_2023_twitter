from bottle import post, request, response
import x
import uuid
from apis.messages_to_users.self_deactivate_profile_email import deactivate_own_profile

@post("/self-deactivate-profile/<user_username>")
def _(user_username):
    try : 
        db = x.db()

        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)
        user_cookie = x.validate_jwt(user_cookie) #user_cookie bliver sat lig den decoded JWT - så de nedenstående linjer kan forsætte som de gjorde før JWT kom ind... - se x fil


        user_to_deactivate_own_profile = db.execute("SELECT * FROM accounts_to_self_deactivate WHERE user_fk = ?",(user_cookie['user_id'],)).fetchone()

        deactivate_key = str(uuid.uuid4().hex)

        if user_cookie['user_username'] == user_username :
            if user_to_deactivate_own_profile == None :
                db.execute("INSERT INTO accounts_to_self_deactivate VALUES(?,?)",(deactivate_key, user_cookie['user_id']))
                db.commit()
            else :
                db.execute("UPDATE accounts_to_self_deactivate SET deactivate_key = ? WHERE user_fk = ?",(deactivate_key,user_cookie['user_id']))

        reciever_email = user_cookie['user_email']

        deactivate_own_profile(deactivate_key=deactivate_key,reciever_email=reciever_email)
        
        return {"info":"ok"}

    except Exception as ex :
        print(ex)
        response.status = 400
        return {"error": str(ex)}

    finally :
        if "db" in locals() : db.close()