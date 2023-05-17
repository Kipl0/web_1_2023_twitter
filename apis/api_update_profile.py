from bottle import request, put, response
import x

@put("/profile")
def _():
    try :
        db = x.db()
        user_cookie = request.get_cookie("user_cookie", secret="my-secret")

        user_updated_first_name = request.forms.get("user_updated_first_name")
        user_updated_last_name = request.forms.get("user_updated_last_name")
        user_updated_caption = request.forms.get("user_updated_caption")
        user_updated_location = request.forms.get("user_updated_location")
        user_updated_link = request.forms.get("user_updated_link")

        db.execute("UPDATE users SET user_first_name = ?, user_last_name = ?, user_caption = ?, user_location = ?, user_link = ? WHERE user_id = ?", (
            user_updated_first_name, user_updated_last_name, user_updated_caption, user_updated_location, user_updated_link, user_cookie["user_id"]
        ))
        db.commit()


        return{"info": "ok"}

    except Exception as ex :
        response.status = 400
        return {"info": str(ex)}

    finally :
        pass