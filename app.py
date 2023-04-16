
from bottle import default_app, get, post, response, request, template, run, static_file, view
import sqlite3
import os
import pathlib
import uuid
import x
import git


##############################
def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}


##############################
#         Bridges 
import bridges.login


##############################
#         Routes 
import routes.send_message
import routes.login
import routes.logout
import routes.frontpage
import routes.profile
import routes.static_files
import routes.upload_picture
import routes.register
import routes.timeout


##############################
#         API's 
import apis.api_tweet 
import apis.api_register
import apis.api_follow
import apis.api_send_message
import apis.upload_files
import apis.api_get_latest_tweets


##############################
#         JS
@get("/js/<filename>") 
def _(filename):
  return static_file(filename, "js")






##############################
#           Routes
##############################
@get("/app.css")
def _():
  return static_file("app.css", root=".")


















###################################
#Run in AWS
try:
    import production #If this production is found, the next line should run
    print("Server running on AWS") #You will never see this line in your own computer - only on amazon
    application = default_app()
# Run in local computer
except Exception as ex:    
    print("Server running locally")
    run(host="127.0.0.1", port=1222, debug=True, reloader=True) #If it cant run it will run locally


###################################
#Continously interation from Github to python anywhere
@post('/secret_url_for_git_hook')
def git_update():
  repo = git.Repo('./mysite')
  origin = repo.remotes.origin
  repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
  origin.pull()
  return ""

