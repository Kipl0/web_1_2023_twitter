from bottle import request, response, delete
import x


@delete("/delete-user")
def _():
    try:
        db = x.db()

        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)
        user_cookie = x.validate_jwt(user_cookie) #user_cookie bliver sat lig den decoded JWT - så de nedenstående linjer kan forsætte som de gjorde før JWT kom ind... - se x fil


        # Hvis Admin er logget ind
        if user_cookie["user_username"] == "Admin" :

            deleted_user = None
            # Ved post sendes attributes som key-values pairs, som tjekkes gennem her indtil den finder en der starter med deactivate_user
            for key in request.forms:
                if key.startswith("delete_user_"):
                    user_to_delete_id = key.split("_", 2)[2]  # Extract the user_id from the field name
                    break
            

            if user_to_delete_id != None:
                # user_to_deactivate = db.execute("SELECT * FROM users WHERE user_id = ?",(deactivate_user_id,)).fetchone()
                print(user_to_delete_id)
                db.execute("DELETE FROM deleted_users WHERE deleted_user_id = ?",(user_to_delete_id,))
                db.commit()

                return {
                    "info" : "ok",
                    "message" : "user deactivated"
                }
           
            else : 
                raise Exception

        else:
            # Unauthorized access
            response.status = 401  # Forbidden
            raise Exception

    except Exception as ex:
        response.status = 401
        print(ex)
        return {"info": str(ex)}

    finally:
        if "db" in locals(): db.close()     
