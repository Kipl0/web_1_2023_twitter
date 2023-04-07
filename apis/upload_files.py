from bottle import post, response, request

@post("/upload-picture")
def _():
  try:
    the_picture = request.files.get("picture")
    name, ext = os.path.splitext(the_picture.filename)

    if ext not in(".jpg", ".jpeg", ".png"):
      response.status = 400
      return "Picture not allowed"

    print("#"*30)
    picture_name = str(uuid.uuid4().hex)
    picture_name = picture_name + ext
    the_picture.save(f"pictures/{picture_name}")
    return "Picture uploaded"

  except Exception as e:
    print(e)

  finally:
    pass

