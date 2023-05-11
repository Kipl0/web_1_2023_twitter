from bottle import post, response, request, time, template
import x
import uuid
import time
import bcrypt
import os

@post("/register")
def _():
    try:
        #get data validated data from form.
        user_email = x.validate_user_email()
        user_username = x.validate_user_name()
        user_password = x.validate_user_password()
        x.validate_user_confirm_password()
        
        user_first_name = request.forms.get("user_first_name")
        user_last_name = request.forms.get("user_last_name")
        
        #password bcrypt - hashing
        user_input_password = user_password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(user_input_password, salt)


        #Upload avatar
        uploaded_avatar = request.files.get("uploaded_avatar") #files i formen
        name, ext = os.path.splitext(uploaded_avatar.filename)
        if ext == "" : 
            #Because of enctype the uploaded picture is not "none", but the extension is - so if there's no upload ext will be an empty string or just none
            picture_name_avatar = "default_avatar.jpg"
        else:
            if ext not in(".jpg", ".jpeg", ".png"):
                response.status = 400
                print(ext)
                return "Picture not allowed"
            picture_name_avatar = str(uuid.uuid4().hex)
            picture_name_avatar = picture_name_avatar + ext
            uploaded_avatar.save(f"avatar/{picture_name_avatar}")
            # return "Picture uploaded"


        #Upload banner
        uploaded_banner = request.files.get("uploaded_banner") #files i formen
        name, ext = os.path.splitext(uploaded_banner.filename)
        if ext == "" : 
            #Because of enctype the uploaded picture is not "none", but the extension is - so if there's no upload ext will be an empty string or just none
            picture_name_banner = "default_banner.png"
        else:
            if ext not in(".jpg", ".jpeg", ".png"):
                response.status = 400
                return "Picture not allowed"
            picture_name_banner = str(uuid.uuid4().hex)
            picture_name_banner = picture_name_banner + ext
            uploaded_banner.save(f"banner/{picture_name_banner}")
            # return "Picture uploaded"


        user_id = str(uuid.uuid4()).replace("-","")
        user = {
            "user_id" : user_id,
            "user_username" : user_username,
            "user_email" : user_email,
            "user_password" : hashed_password,
            "user_verification_key" : str(uuid.uuid4()).replace("-", ""),
            "user_first_name" : user_first_name,
            "user_last_name" : user_last_name,
            "user_avatar" : picture_name_avatar,
            "user_banner" : picture_name_banner,
            "user_link" : "",
            "user_caption" : "",
            "user_location" : "",
            "user_created_at" : int(time.time()),
            "user_verified" : 0,
            "user_total_tweets" : 0,
            "user_total_retweets" : 0,
            "user_total_comments" : 0,
            "user_total_likes" : 0,
            "user_total_dislikes" : 0,
            "user_total_followers" : 0,
            "user_total_following" : 0,
            "user_active" : 0
        }




        values = ""
        for key in user:
            values += f':{key},'
        values = values.rstrip(",")

        db = x.db()
        total_rows_inserted = db.execute(f"INSERT INTO users VALUES({values})", user).rowcount
        print(user_password)
        db.commit()

        if total_rows_inserted != 1 : raise Exception("Please try again")
        return {
            "info" : "user created",
            "user_id" : user_id
        }

    except Exception as e:
        print(e)
        try: # Controlled exception, usually comming from the x file
            response.status = e.args[0]
            return {"info":e.args[1]}

        except: # Something unknown went wrong
            if "user_email" in str(e): 
                response.status = 400 
                return {"info":"user_email already exists"}

            if "user_name" in str(e): 
                response.status = 400 
                return {"info":"user_name already exists"}

            # unknown scenario
            response.status = 500
            return {"info":str(e)}

    finally:
        if "db" in locals(): db.close()
