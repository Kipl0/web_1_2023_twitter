from bottle import post, response, request
import os
import uuid

@post("/upload-picture")
def _():
  try:
    the_picture = request.files.get("uploaded_picture") #files i formen
    name, ext = os.path.splitext(the_picture.filename)

    if ext not in(".jpg", ".jpeg", ".png"):
      response.status = 400
      return "Picture not allowed"

    print("#"*30)
    picture_name = str(uuid.uuid4().hex)
    picture_name = picture_name + ext
    the_picture.save(f"pictures/{picture_name}")
    return "Picture uploaded"
    #kan give en warning messsage "resourcewarning: unclosed file" så længe filen er refereret vil den blive vist, ved ny query vil den blive dereferenced og forsvinde

  except Exception as e:
    print(e)

  finally:
    pass

