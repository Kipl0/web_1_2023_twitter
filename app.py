
from bottle import default_app, get, template, run, static_file, view, response
import sqlite3
import os
import pathlib
import uuid
import x

##############################
def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}





##############################
#         API's 
import views.tweet

##############################
#         API's 
import apis.api_tweet 






##############################
#         JS
@get("/js/<filename>") 
def _(filename):
  return static_file(filename, "js")








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
@get("/images/<filename:re:.*\.gif>")
def _(filename):
  return static_file(filename, root="./images")





##############################
#           Routes
##############################
@get("/app.css")
def _():
  return static_file("app.css", root=".")



############################## you want to display the index page, you want to pass the title, tweets and trends
@get("/")
def render_index():
  try:
    db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/twitter.db") 
    db.row_factory = dict_factory
    user_suggested_follows = db.execute("SELECT * FROM users WHERE user_username!=?",("majs503",)).fetchall()
    
    trends = db.execute("SELECT * FROM trends")

    tweets = db.execute("SELECT * FROM tweets,users WHERE tweets.tweet_user_fk = users.user_id")
    return template("index", title="Twitter", tweets=tweets, trends=trends, user_suggested_follows=user_suggested_follows, TWEET_MIN_LEN=x.TWEET_MIN_LEN, TWEET_MAX_LEN=x.TWEET_MAX_LEN)
    

  except Exception as ex:
    print(ex)
    response.status = 400
    return {"error": str(ex)}

  finally:
    if "db" in locals(): db.close()



##############################
@get("/<user_username>")
# @view("profile")
def _(user_username):
  try:
    db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/twitter.db") 
    db.row_factory = dict_factory

    user = db.execute("SELECT * FROM users WHERE user_username=? COLLATE NOCASE",(user_username,)).fetchall()[0]
    user_id = user["user_id"]    

    trends = db.execute("SELECT * FROM trends")

    user_suggested_follows = db.execute("SELECT * FROM users WHERE user_username!=?",("majs503",)).fetchall()

    #with that id look up the respectives tweets
    #pass the tweets to the view. Template it
    tweets = db.execute("SELECT * FROM tweets WHERE tweet_user_fk=?",(user_id,)).fetchall()
    return template("profile", user=user, tweets=tweets, trends=trends, user_suggested_follows=user_suggested_follows)

  except Exception as ex:
    print(ex)
    response.status = 400
    return {"error": str(ex)}

  finally:
    if "db" in locals(): db.close()



###################################
#Run in AWS
try:
    import production #If this production is found, the next line should run
    print("Server running on AWS") #You will never see this line in your own computer - only on amazon
    application = default_app()
# Run in local computer
except Exception as ex:    
    print("Server running locally")
    run(host="127.0.0.1", port=3306, debug=True, reloader=True) #If it cant run it will run locally



