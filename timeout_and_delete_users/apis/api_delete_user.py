from bottle import post, request, response, delete
import sqlite3

# @post("/api-delete-user") # godt for indlæring at kalde det sådan, men man ville ikke se det her i et firma. Vi bruger delete i stedet for post
@delete("/user/<user_id>")
def _(user_id):
  try: 
    db = sqlite3.connect("company.db")
    # user_id = request.forms.get("user_id")
    print(user_id)

    user_delete = db.execute("DELETE FROM users WHERE user_id=?", (user_id,)).rowcount
    if not user_delete : raise Exception(401, "User not found")
    db.commit()

    return {
        "info" : "User deleted",
        "user_id" : user_id
    }

  except Exception as ex: 
    response.status = 401
    return str(ex)

  finally: 
    if "db" in locals(): db.close()


    