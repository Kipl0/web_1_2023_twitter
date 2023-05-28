from bottle import post, request, response
import bcrypt
import x

@post("/confirm-new-password/<user_key>")
def _(user_key):
    try :
        # Open forbindelse DB
        db = x.db()

        # Tjek at password overholder validation kriterier
        new_password = x.validate_user_password()
        x.validate_user_confirm_password()

        # Find brugeren som ønsker nyt passwrod ud fra validation key
        user_in_reset_password_table = db.execute("SELECT * FROM accounts_to_reset_password WHERE change_password_user_key = ?",(user_key,)).fetchone()
        user_to_reset_password = db.execute("SELECT * FROM users WHERE user_id = ?",(user_in_reset_password_table['change_password_user_fk'],)).fetchone()
        
        # nyt og confirm password stemmer overns

        new_hashed_password = new_password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(new_hashed_password, salt)

        db.execute("UPDATE users SET user_password = ? WHERE user_id = ?",(hashed_password, user_to_reset_password['user_id']))
        db.commit()

        db.execute("DELETE FROM accounts_to_reset_password WHERE change_password_user_key = ?",(user_key,))
        db.commit()

        return {"info":"ok"}

    except Exception as ex :
        print(ex)
        #response.status = ex.args[0]
        #return {"info":ex.args[1]}
        return {"info": "Oops, something went wrong"}

    finally :
        if "db" in locals(): db.close()