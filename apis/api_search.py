from bottle import post, request, response
# normalt ville man bruge "get" fordi man skal "get" noget fra db. Men fordi get har det med at cache, bruger vi post
import json #bruges for at kunne returnere en list i try
import x

@post("/search")
def _() :
    try :
        db = x.db()

        search_input = request.forms.get("search_input")

        # Nedenstående kommentar er et eksemple på brug af LIKE og ikke FTS5 som vi har implementeret
        # search_results = db.execute(f"SELECT user_username, user_first_name, user_last_name, user_avatar FROM users WHERE user_username LIKE '%{search_input}%' OR user_first_name LIKE '%{search_input}%' OR user_last_name LIKE '%{search_input}%' OR user_first_name || ' ' || user_last_name  LIKE '%{search_input}%'").fetchall()
        search_results = db.execute(f"SELECT user_username, user_first_name, user_last_name, user_avatar FROM users_search WHERE users_search MATCH 'user_username:{search_input}* OR user_first_name:{search_input}* OR user_last_name:{search_input}*'").fetchall()

        response.set_header("Content-type","application/json")
        return json.dumps(search_results)

    except Exception as e :
        print(e)
        pass

    finally :
        pass