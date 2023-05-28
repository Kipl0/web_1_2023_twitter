from bottle import request, response
import sqlite3
import pathlib 
import re #regular expression

COOKIE_SECRET = "my-secret"

images_not_to_be_deleted = ["51602a9f7d82472b90ed1091248f6cb1.jpeg","a22da1effb3d4f03a0f77f9aa8320203.jpg", "6268331d012247539998d7664bd05cc1.jpg", "07578f6c49d84b7c94ce80e96c64ccc0.jpg","admin.png","ad1bfe9ce6e44a009b57a1a183ccb202.jpg","e130fd8b81d049a1b2fafbca9c5a15e3.png", "494e6a7fdadb4b3cae58d37a4fad879c.jpg","dd5582fff3ca4f7f9f97a911f3e77b22.jpg","default_banner.png"]

##############################
def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}

##############################
def db():
  try:
    db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/twitter.db")
    # db = sqlite3.connect("twitter.db")  
    db.execute("PRAGMA foreign_keys=ON;")
    db.row_factory = dict_factory
    return db
  except Exception as ex:
    print(ex)
  finally:
    pass

# ##############################
TWEET_MIN_LEN = 0
TWEET_MAX_LEN = 280

def validate_tweet_message():
  error = f"message min {TWEET_MIN_LEN} max {TWEET_MAX_LEN} characters"
  request.forms.tweet_message = request.forms.tweet_message.strip()
  if len(request.forms.tweet_message) < TWEET_MIN_LEN: raise Exception(error)
  if len(request.forms.tweet_message) > TWEET_MAX_LEN: raise Exception(error)
  return request.forms.tweet_message



# ##############################
# #       Validate user
# ##############################
USER_EMAIL_MIN = 6
USER_EMAIL_MAX = 100
USER_EMAIL_REGEX = "^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$"

def validate_user_email():
  error = f"user_email invalid"
  request.forms.user_email = request.forms.user_email.strip()
  if len(request.forms.user_email) < USER_EMAIL_MIN : raise Exception(400, error)
  if len(request.forms.user_email) > USER_EMAIL_MAX : raise Exception(400, error)
  if not re.match(USER_EMAIL_REGEX, request.forms.user_email) : raise Exception(400, error)
  return request.forms.user_email



# #######################
# # the name user_name comes from the username variable for logging in. 
# # capitalize it to show this is a constant and should not be changed
USER_NAME_MIN = 2
USER_NAME_MAX = 20
# what the user is allowed to put in their username - english letters only and numbers from 0-9
USER_NAME_REGEX = "^[a-zA-Z0-9_]*$"


def validate_user_name():
  error = f"user_name {USER_NAME_MIN} to {USER_NAME_MAX} english letters or numbers from 0 to 9"
  request.forms.user_name = request.forms.user_name.strip() #no spaces in front or back - only want the text
  if len(request.forms.user_name) < USER_NAME_MIN: raise Exception(error)
  if len(request.forms.user_name) > USER_NAME_MAX: raise Exception(error)
  if not re.match(USER_NAME_REGEX, request.forms.user_name): raise Exception(error)
  return request.forms.user_name

PASSWORD_MIN = 3
PASSWORD_MAX = 15
PASSWORD_REGEX = ""

def validate_user_password():
  error = f"Password must be between {PASSWORD_MIN} and {PASSWORD_MAX} characters"
  request.forms.user_password = request.forms.user_password.strip()
  if len(request.forms.user_password) < PASSWORD_MIN : raise Exception(400, error)
  if len(request.forms.user_password) > PASSWORD_MAX : raise Exception(400, error)
  return request.forms.user_password


def validate_user_confirm_password():
  error = "Passwords do not match"
  request.forms.user_password = request.forms.user_password.strip()
  request.forms.user_confirm_password = request.forms.user_confirm_password.strip()
  if request.forms.user_password != request.forms.user_confirm_password : raise Exception(400, error)

USER_FIRST_NAME_MIN = 2
USER_FIRST_NAME_MAX = 20

USER_LAST_NAME_MIN = 2
USER_LAST_NAME_MAX = 20

def validate_user_first_name():
  error = "Please insert your first name"
  request.forms.user_first_name = request.forms.user_first_name.strip()
  if len(request.forms.user_first_name) < USER_FIRST_NAME_MIN : raise Exception(400, error)
  if len(request.forms.user_first_name) > USER_FIRST_NAME_MAX : raise Exception(400, error)
  return request.forms.user_first_name

def validate_user_last_name():
  error = "Please insert your last name"
  request.forms.user_last_name = request.forms.user_last_name.strip()
  if len(request.forms.user_last_name) < USER_LAST_NAME_MIN : raise Exception(400, error)
  if len(request.forms.user_last_name) > USER_LAST_NAME_MAX : raise Exception(400, error)
  return request.forms.user_last_name



# my-secret bruges til at decypte username - så siden ved, hvem brugeren er. 