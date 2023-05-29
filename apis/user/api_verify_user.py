from bottle import post, response
import x

# post til at user bliver verified i db
@post("/verify-email/<verification_key>") #verification key kommer fra db
def _(verification_key):
    try :
        db = x.db()
        print("tester")
        # Få fat på user_fk OG tjek om den eksisterer - hvis den gør er der en række med data i tabel
        user_to_verify = db.execute("SELECT * FROM accounts_to_verify WHERE verify_user_key = ?", (verification_key,)).fetchone()


        if user_to_verify != "": # den eksisterer i db
            db.execute("DELETE FROM accounts_to_verify WHERE verify_user_key = ?", (verification_key,))
            db.commit()

        else: #den eksisterer ikke i db
            print("Verification_key does not exist in the database")
            raise Exception(400, "Verification_key does not exist in the database")

        return {"info": "ok"}

    except Exception as ex :
        print(ex)
        response.status = 400
        return {"error": str(ex)}

    finally :
        if "db" in locals(): db.close()