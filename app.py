
from bottle import default_app, get, template, run, static_file, view, response
import sqlite3
import os

##############################
def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}






# This data will come from the database
# For now, we just hard coded the data
# tweets = [
#   { "verified":1, "image_name":"1.jpg", "fullname":"Santiago Donoso", "username":"santiagodonoso","message":"My first tweet","total_messages":"1","total_retweets":"2","total_likes":"3","total_dislikes":"4",},
#   { "verified":0, "image_name":"2.jpg", "fullname":"Joe Biden", "username":"joebiden","message":"I am THE president","message_image":"1.png","total_messages":"1","total_retweets":"2","total_likes":"3","total_dislikes":"4",},
#   { "verified":1, "image_name":"1.jpg", "fullname":"Santiago Donoso", "username":"santiagodonoso","message":"My first tweet","total_messages":"1","total_retweets":"2","total_likes":"3","total_dislikes":"4",},
#   { "verified":0, "image_name":"1.jpg", "fullname":"Santiago Donoso", "username":"santiagodonoso","message":"My first tweet","message_image":"1.png","total_messages":"1","total_retweets":"2","total_likes":"3","total_dislikes":"4",},
#   { "verified":1, "image_name":"1.jpg", "fullname":"Santiago Donoso", "username":"santiagodonoso","message":"My first tweet","total_messages":"1","total_retweets":"2","total_likes":"3","total_dislikes":"4",},
#   { "verified":0, "image_name":"1.jpg", "fullname":"Santiago Donoso", "username":"santiagodonoso","message":"My first tweet","message_image":"1.png","total_messages":"1","total_retweets":"2","total_likes":"3","total_dislikes":"4",},
# ]


trends = [
  {"title":"LGBTQ", "total_hash":58.5},
  {"title":"#Bevarstorebededag", "total_hash":20},
  {"title":"Netto", "total_hash":16.4},
  {"title":"Politics", "total_hash":17.3},
  {"title":"Bilka", "total_hash":10.8}
]


profiles = [
  {"profile_pic":"twitter-profile.jpg", "fullname" : "Maja I. Larsen", "total_tweets" : 58, "username": "majs503", "membership" : "Member since Feb 2012", "follows" : 4, "followers" : 8 }
]




##############################
#         IMAGES
##############################
@get("/images/<filename:re:.*\.png>")
def _(filename):
  return static_file(filename, root="./images")

##############################
@get("/images/<filename:re:.*\.jpg>")
def _(filename):
  return static_file(filename, root="./images")

##############################
@get("/images/<filename:re:.*\.jpeg>")
def _(filename):
  return static_file(filename, root="./images")

##############################
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
#           Routes  
##############################
@get("/app.css")
def _():
  return static_file("app.css", root=".")

############################## you want to display the index page, you want to pass the title, tweets and trends
@get("/")
def render_index():
  try:
    db = sqlite3.connect("twitter.db")
    db.row_factory = dict_factory
    user_suggested_follows = db.execute("SELECT * FROM users WHERE username!=?",("majs503",)).fetchall()
    # tweets = db.execute("SELECT * FROM tweets")
    tweets = db.execute("SELECT * FROM tweets,users WHERE tweets.user_fk = users.id")
    return template("index", title="Twitter", tweets=tweets, trends=trends, user_suggested_follows=user_suggested_follows)
    
  except Exception as ex:
    print(ex)
    response.status = 400
    return {"error": str(ex)}

  finally:
    if "db" in locals(): db.close()





##############################
@get("/<username>")
# @view("profile")
def _(username):
  try:
    # db = sqlite3.connect("home/MajaIL/mysite/twitter.db")
    db = sqlite3.connect("twitter.db")
    db.row_factory = dict_factory

    user = db.execute("SELECT * FROM users WHERE username=? COLLATE NOCASE",(username,)).fetchall()[0]
    user_id = user["id"]    

    user_suggested_follows = db.execute("SELECT * FROM users WHERE username!=?",("majs503",)).fetchall()

    #with that id look up the respectives tweets
    #pass the tweets to the view. Template it
    tweets = db.execute("SELECT * FROM tweets WHERE user_fk=?",(user_id,)).fetchall()
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
    run(host="127.0.0.1", port=3002, debug=True, reloader=True) #If it cant run it will run locally



###################################
#Continously interation from Github to python anywhere
@post('/secret_url_for_git_hook')
def git_update():
  repo = git.Repo('./web_1_2023_twitter')
  origin = repo.remotes.origin
  repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
  origin.pull()
  return ""