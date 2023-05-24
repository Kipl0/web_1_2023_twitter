from bottle import post, request, response
import bcrypt
import x

@post("/confirm-new-password/<user_key>")
def _(user_key):
    try :
        db = x.db()

        new_password = request.forms.get("new_password")
        new_password_confirm = request.forms.get("new_password_confirm")


        user_in_reset_password_table = db.execute("SELECT * FROM accounts_to_reset_password WHERE change_password_user_key = ?",(user_key,)).fetchone()
        user_to_reset_password = db.execute("SELECT * FROM users WHERE user_id = ?",(user_in_reset_password_table['change_password_user_fk'],)).fetchone()
        
        # nyt og confirm password stemmer overns
        if new_password == new_password_confirm :
            new_hashed_password = new_password.encode('utf-8')
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(new_hashed_password, salt)

            db.execute("UPDATE users SET user_password = ? WHERE user_id = ?",(hashed_password, user_to_reset_password['user_id']))
            db.commit()

            db.execute("DELETE FROM accounts_to_reset_password WHERE change_password_user_key = ?",(user_key,))
            db.commit()

            return {"info":"ok"}


        # Hvis ikke user_password_confirm stemmer overens med user_password_confirm
        raise Exception(400, "cannot update user password")

    except Exception as ex :
        print(ex)
        response.status = ex.args[0]
        return {"info":ex.args[1]}

    finally :
        if "db" in locals(): db.close()