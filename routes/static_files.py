from bottle import get, static_file

##############################
#         tweet IMAGES
@get("/tweet_images/<filename:re:.*\.png>")
def _(filename):
  return static_file(filename, root="./tweet_images")

@get("/tweet_images/<filename:re:.*\.jpg>")
def _(filename):
  return static_file(filename, root="./tweet_images")

@get("/tweet_images/<filename:re:.*\.jpeg>")
def _(filename):
  return static_file(filename, root="./tweet_images")

@get("/tweet_images/<filename:re:.*\.PNG>")
def _(filename):
  return static_file(filename, root="./tweet_images")

@get("/tweet_images/<filename:re:.*\.gif>")
def _(filename):
  return static_file(filename, root="./tweet_images")


##############################
#         Comment IMAGES
@get("/comment_images/<filename:re:.*\.png>")
def _(filename):
  return static_file(filename, root="./comment_images")

@get("/comment_images/<filename:re:.*\.jpg>")
def _(filename):
  return static_file(filename, root="./comment_images")

@get("/comment_images/<filename:re:.*\.jpeg>")
def _(filename):
  return static_file(filename, root="./comment_images")

@get("/comment_images/<filename:re:.*\.PNG>")
def _(filename):
  return static_file(filename, root="./comment_images")

@get("/comment_images/<filename:re:.*\.gif>")
def _(filename):
  return static_file(filename, root="./comment_images")



##############################
@get("/avatar/<filename:re:.*\.png>")
def _(filename):
  return static_file(filename, root="./avatar")

##############################
@get("/avatar/<filename:re:.*\.jpg>")
def _(filename):
  return static_file(filename, root="./avatar")

##############################
@get("/avatar/<filename:re:.*\.jpeg>")
def _(filename):
  return static_file(filename, root="./avatar")



##############################
@get("/banner/<filename:re:.*\.jpg>")
def _(filename):
  return static_file(filename, root="./banner")

##############################
@get("/banner/<filename:re:.*\.png>")
def _(filename):
  return static_file(filename, root="./banner")


##############################
@get("/icons/<filename:re:.*\.svg>")
def _(filename):
  return static_file(filename, root="./icons")



##############################
@get("/favicon.png")
def _():
  return static_file("favicon.png", root=".")


