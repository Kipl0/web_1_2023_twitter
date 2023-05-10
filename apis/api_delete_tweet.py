from bottle import delete, request, response
import sqlite3
import x


@delete("/delete-tweet")
def _():
  try: 
    db = x.db()

    tweet_to_delete_id = request.forms.get("tweet_id")
    tweet_to_delete = db.execute("SELECT * FROM tweets WHERE tweet_id = ?", (tweet_to_delete_id,)).fetchone()

    user_cookie = request.get_cookie("user_cookie", secret="my-secret")
    
    # dobbelt tjek at kun user kan slette sine egne tweets
    if tweet_to_delete["tweet_user_fk"] == user_cookie["user_id"] :
        db.execute("DELETE FROM tweets WHERE tweet_id = ?",(tweet_to_delete_id,))
        db.commit()    


    return{"info":"ok", "tweet_to_delete_id":tweet_to_delete_id}

  except Exception as ex: 
    response.status = 401
    return str(ex)

  finally: 
    if "db" in locals(): db.close()

