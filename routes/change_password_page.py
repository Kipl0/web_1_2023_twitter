from bottle import get, request, response, template
import x

@get("/change-password/<user_key>")
def _(user_key):
    try :
        # Åben forbindelse til DB
        db = x.db()

        # Set default info tekst
        info_text = "Enter your new password"

        # Tjek om change_password_user_key ligger i tabellen
        user_in_reset_password_table = db.execute("SELECT * FROM accounts_to_reset_password WHERE change_password_user_key = ?",(user_key,)).fetchone()

        # Hvis ikke den findes i tabellen, opdater info tekst
        if user_in_reset_password_table is None:
            info_text = "This key is no longer valid"

        return template("change_password_page", INFO_TEXT=info_text)


    except Exception as ex :
        print(x)
        response.status = ex.args[0]
        return {"info":ex.args[1]}


    finally :
        if "db" in locals() : db.close()