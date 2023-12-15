from bottle import post, response, request, time, template
import x
import uuid
import time
import bcrypt
import os
from apis.messages_to_users.send_verification_email import send_verification_email

@post("/register")
def _():
    try:
        import production #If this production is found, the next line should run
        rootdir = "/home/Kipl0/mysite/"     
    except Exception as ex:    
        rootdir = "C:/Users/maalm/Documents/kea/web_1_2023_twitter/"

    try:
        db = x.db()

        #get data validated data from form.
        user_email = x.validate_user_email()
        user_username = x.validate_user_name()
        user_first_name = x.validate_user_first_name()
        user_last_name = x.validate_user_last_name()
        user_password = x.validate_user_password()
        x.validate_user_confirm_password()
        
        
        #password bcrypt - kryptering
        user_input_password = user_password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(user_input_password, salt)



        #Upload avatar
        uploaded_avatar = request.files.get("uploaded_avatar") #files i formen
        if uploaded_avatar != None :
            name, ext = os.path.splitext(uploaded_avatar.filename)
            if ext == "" : 
                #Because of enctype the uploaded picture is not "none", but the extension is - so if there's no upload ext will be an empty string or just none
                avatar_to_upload = "default_avatar.png"
            else:
                if ext not in(".jpg", ".jpeg", ".png"):
                    response.status = 400
                    print(ext)
                    return "Picture not allowed"
                avatar_to_upload = str(uuid.uuid4().hex)
                avatar_to_upload = avatar_to_upload + ext
                uploaded_avatar.save(f"{rootdir}avatar/{avatar_to_upload}")
                # return "Picture uploaded"
        else :
            avatar_to_upload = "default_avatar.png"

        #Upload banner
        uploaded_banner = request.files.get("uploaded_banner") #files i formen
        if uploaded_banner != None :
            name, ext = os.path.splitext(uploaded_banner.filename)
            if ext == "" : 
                #På grund af enctype i html er uploaded_picture ikke "", men ext er - så hvis der ikke uploades et billede er ext en empty string og dermed ikke none
                banner_to_upload = "default_banner.png"
            else:
                if ext not in(".jpg", ".jpeg", ".png"):
                    response.status = 400
                    raise Exception("Picture not allowed")
                banner_to_upload = str(uuid.uuid4().hex)
                banner_to_upload = banner_to_upload + ext
                uploaded_banner.save(f"{rootdir}banner/{banner_to_upload}")
                # return "Picture uploaded"
        else :
            banner_to_upload = "default_banner.png"

        user_id = str(uuid.uuid4()).replace("-","")
        user = {
            "user_id" : user_id,
            "user_username" : user_username,
            "user_email" : user_email,
            "user_password" : hashed_password,
            "user_first_name" : user_first_name,
            "user_last_name" : user_last_name,
            "user_avatar" : avatar_to_upload,
            "user_banner" : banner_to_upload,
            "user_link" : "",
            "user_caption" : "",
            "user_location" : "",
            "user_created_at" : int(time.time()),
            "user_total_tweets" : 0,
            "user_total_retweets" : 0,
            "user_total_comments" : 0,
            "user_total_likes" : 0,
            "user_total_followers" : 0,
            "user_total_following" : 0,
            "user_active" : 1,
            "user_twitter_gold" : 0
        }


        values = ""
        for key in user:
            values += f':{key},'
        values = values.rstrip(",")

        total_rows_inserted = db.execute(f"INSERT INTO users VALUES({values})", user).rowcount
        db.commit()

        if total_rows_inserted != 1 : 
            raise Exception("Please try again")




        # Kør funktionen create_verification_key - findes længere nede - verification_key bliver returned her og bruges i næste function lige under
        verification_key = create_verification_key(user_id=user_id)



        # Send email to user if registered, "reciever_email = " øger bare læsbarhed - kan undværes
        send_verification_email(reciever_email=user_email, verification_key=verification_key)



        return {"info": "ok"}

    except Exception as e:
        print(e)
        try: # Controlled exception, usually comming from the x file
            response.status = e.args[0]
            return {"info":e.args[1]}

        except: # Something unknown went wrong
            if "user_email" in str(e): 
                response.status = 400 
                return {"info":"user_email already exists"}

            if "user_username" in str(e): 
                response.status = 400 
                return {"info":"user_name already exists"}

            # unknown scenario
            response.status = 500
            return {"info":str(e)}

    finally:
        if "db" in locals(): db.close()



# str 3 gange for læsbarhed - så man tydeligt kan se, hvad der returneres her.
def create_verification_key(user_id : str) -> str : 
    db = x.db()

    verification_key = str(uuid.uuid4().hex)
    db.execute("INSERT INTO accounts_to_verify VALUES(?,?)",(verification_key, user_id))
    db.commit()

    return verification_key