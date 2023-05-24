from bottle import post, request, response
from apis.change_password_email import send_change_password_email
import uuid
import x

@post("/change-password-submit")
def _():
    try :
        db = x.db()
        # TODO

        # få fat på email input
        # Validate både om det er en email i validate() js
        change_password_email_input = request.forms.get("change_password_email_input")
        print(change_password_email_input)

        # tjek om email eksisterer i users
        is_user_in_users_table = db.execute("SELECT * FROM users WHERE user_email = ?",(change_password_email_input,)).fetchone()

        if not is_user_in_users_table :
            print("user eksisterer ikke i db")
            raise Exception("Email is not used for an account")

        # Tjek om email eskisterer i reset_password tabel -> så man kun kan være der 1 gang
        does_user_exist_reset_password = db.execute("SELECT * FROM accounts_to_reset_password WHERE change_password_user_fk = ?",(is_user_in_users_table['user_id'],)).fetchone()
        if does_user_exist_reset_password :
            print("bruger eksiterer allerede i reset_password tabel")
            raise Exception("Email sent already, please check your email")


        # Insert bruger til reset_password_table
        change_password_user_key = str(uuid.uuid4().hex)
        db.execute("INSERT INTO accounts_to_reset_password VALUES(?,?)",(change_password_user_key, is_user_in_users_table['user_id']))
        db.commit()
        send_change_password_email(reciever_email = change_password_email_input, change_key = change_password_user_key)
        return {"info":"ok"}

    except Exception as ex :
        pass


    finally : 
        pass