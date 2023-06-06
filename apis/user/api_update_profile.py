from bottle import request, put, response
import x
import os
import uuid
import time
import jwt

@put("/profile")
def _():
    try:
        import production #If this production is found, the next line should run
        rootdir = "/home/Kipl0/mysite/"     
    except Exception as ex:    
        rootdir = "C:/Users/maalm/Documents/kea/web_1_2023_twitter/"

    try:
        db = x.db()
        user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)
        user_cookie = x.validate_jwt(user_cookie) #user_cookie bliver sat lig den decoded JWT - så de nedenstående linjer kan forsætte som de gjorde før JWT kom ind... - se x fil


        user_updated_first_name = request.forms.get("user_updated_first_name")
        user_updated_last_name = request.forms.get("user_updated_last_name")
        user_updated_caption = request.forms.get("user_updated_caption")
        user_updated_location = request.forms.get("user_updated_location")
        user_updated_link = request.forms.get("user_updated_link")

        # Upload avatar
        uploaded_avatar = request.files.get("uploaded_avatar_input")
        if uploaded_avatar != None :
            name, ext = os.path.splitext(uploaded_avatar.filename)
            if ext == "":
                # No file uploaded, set default avatar
                picture_name_avatar = user_cookie["user_avatar"]
            else:
                if ext not in (".jpg", ".jpeg", ".png"):
                    response.status = 400
                    return "Picture not allowed"
                picture_name_avatar = str(uuid.uuid4().hex) + ext
                uploaded_avatar.save(f"{rootdir}avatar/{picture_name_avatar}")

                if user_cookie["user_avatar"] not in x.images_not_to_be_deleted :
                    user_cookie_avatar = user_cookie["user_avatar"]
                    myfile = f"{rootdir}avatar/{user_cookie_avatar}"
                    if user_cookie_avatar != "default_avatar.png" :


                        os.remove(myfile)
        else :
            picture_name_avatar = user_cookie["user_avatar"]

        # Upload banner
        uploaded_banner = request.files.get("uploaded_banner_input")
        if uploaded_banner != None :
            name, ext = os.path.splitext(uploaded_banner.filename)
            if ext == "":
                # No file uploaded, set default banner
                picture_name_banner = user_cookie["user_banner"]
            else:
                if ext not in (".jpg", ".jpeg", ".png"):
                    response.status = 400
                    return "Picture not allowed"
                picture_name_banner = str(uuid.uuid4().hex) + ext
                uploaded_banner.save(f"{rootdir}banner/{picture_name_banner}")

                if user_cookie["user_banner"] not in x.images_not_to_be_deleted :
                    user_cookie_banner = user_cookie["user_banner"]
                    myfile = f"{rootdir}banner/{user_cookie_banner}"
                    if user_cookie_banner != "default_banner.png" :
                        os.remove(myfile)
        else : 
            picture_name_banner = user_cookie["user_banner"]

        db.execute(
            "UPDATE users SET user_first_name = ?, user_last_name = ?, user_caption = ?, user_location = ?, user_link = ?, user_avatar = ?, user_banner = ? WHERE user_id = ?",
            (
                user_updated_first_name,
                user_updated_last_name,
                user_updated_caption,
                user_updated_location,
                user_updated_link,
                picture_name_avatar,
                picture_name_banner,
                user_cookie["user_id"],
            ),
        )
        db.commit()

        # ----------------------------
        #       cookie og jwt
        # ----------------------------
        # jwt
        updated_user = db.execute("SELECT * FROM users WHERE user_id = ?",(user_cookie["user_id"],)).fetchone()

        updated_user["user_password"] = ""
        user_jwt = jwt.encode(updated_user, x.JWT_SECRET, algorithm=x.JWT_ALGORITHM)

        # user cookie
        cookie_expiration_date = int(time.time()) + 7200
        response.set_cookie("user_cookie", user_jwt, secret = x.COOKIE_SECRET, httponly=True, expires=cookie_expiration_date)

        return {"info": "ok"}

    except Exception as ex:
        print(ex)
        response.status = 400
        return {"info": str(ex)}

    finally:
        pass


