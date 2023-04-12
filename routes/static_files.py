
from bottle import get, static_file


##############################
#         IMAGES
@get("/images/<filename:re:.*\.png>")
def _(filename):
  return static_file(filename, root="./images")

@get("/images/<filename:re:.*\.jpg>")
def _(filename):
  return static_file(filename, root="./images")

@get("/images/<filename:re:.*\.jpeg>")
def _(filename):
  return static_file(filename, root="./images")

@get("/images/<filename:re:.*\.PNG>")
def _(filename):
  return static_file(filename, root="./images")

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
@get("/favicon.png")
def _():
  return static_file("favicon.png", root=".")


