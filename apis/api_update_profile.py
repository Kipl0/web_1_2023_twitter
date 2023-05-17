from bottle import request, put, response
import x
import os
import uuid

@put("/profile")
def _():
    try:
        db = x.db()
        user_cookie = request.get_cookie("user_cookie", secret="my-secret")

        user_updated_first_name = request.forms.get("user_updated_first_name")
        user_updated_last_name = request.forms.get("user_updated_last_name")
        user_updated_caption = request.forms.get("user_updated_caption")
        user_updated_location = request.forms.get("user_updated_location")
        user_updated_link = request.forms.get("user_updated_link")

        # Upload avatar
        uploaded_avatar = request.files.get("uploaded_avatar_input")
        name, ext = os.path.splitext(uploaded_avatar.filename)
        if ext == "":
            # No file uploaded, set default avatar
            picture_name_avatar = user_cookie["user_avatar"]
        else:
            if ext not in (".jpg", ".jpeg", ".png"):
                response.status = 400
                return "Picture not allowed"
            picture_name_avatar = str(uuid.uuid4().hex) + ext
            uploaded_avatar.save(f"avatar/{picture_name_avatar}")

            if user_cookie["user_avatar"] not in x.images_not_to_be_deleted :
                user_cookie_avatar = user_cookie["user_avatar"]
                myfile = f"avatar/{user_cookie_avatar}"
                os.remove(myfile)

        # Upload banner
        uploaded_banner = request.files.get("uploaded_profile_banner")
        name, ext = os.path.splitext(uploaded_banner.filename)
        if ext == "":
            # No file uploaded, set default banner
            picture_name_banner = user_cookie["user_banner"]
        else:
            if ext not in (".jpg", ".jpeg", ".png"):
                response.status = 400
                return "Picture not allowed"
            picture_name_banner = str(uuid.uuid4().hex) + ext
            uploaded_banner.save(f"banner/{picture_name_banner}")

            if user_cookie["user_banner"] not in x.images_not_to_be_deleted :
                user_cookie_banner = user_cookie["user_banner"]
                myfile = f"banner/{user_cookie_banner}"
                os.remove(myfile)


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

        updated_user = db.execute("SELECT * FROM users WHERE user_id = ?",(user_cookie["user_id"],)).fetchone()

        response.set_cookie("user_cookie", updated_user, secret = x.COOKIE_SECRET, httponly=True)

        return {"info": "ok"}

    except Exception as ex:
        response.status = 400
        return {"info": str(ex)}

    finally:
        pass




    # uploaded_banner = request.files.get("uploaded_profile_banner")
    # banner_filename = uploaded_banner.filename if uploaded_banner else None
    # if banner_filename:
    #     name, ext = os.path.splitext(banner_filename)
    #     if ext not in (".jpg", ".jpeg", ".png"):
    #         response.status = 400
    #         return {"error": "Picture not allowed"}
    #     picture_name_banner = str(uuid.uuid4().hex) + ext
    #     uploaded_banner.save(f"banner/{picture_name_banner}")
    # else:
    #     picture_name_banner = None  # Keep the existing banner
