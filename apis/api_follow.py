from bottle import post, request, response
import sqlite3
import pathlib

@post("/api-follow")
def _():
    try:
        # TODO: get user from cookie
        # user = request.get_cookie("user", secret="xxxx")
        # TODO: get user id from the user from the cookie
        # TODO: validate the volloweer's id
        # TODO: connect to the database
        db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/twitter.db") 
        # TODO: insert into followers table (tjek om users ID eksisterer i databasen)
        user_followee_id = request.forms.get("user_followee_id", "") #a way to secure the code - worst case, hvis data er tom pass en tom string 
        return {"info": f"Following user with id: {user_followee_id}"}

    except Exception as e:
        print(e)
        pass

    finally:
        pass