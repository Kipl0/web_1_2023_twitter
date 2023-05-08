from bottle import post, request, response
# normalt ville man bruge "get" fordi man skal "get" noget fra db. Men fordi get har det med at cache, bruger vi post
import json #bruges for at kunne returnere en list i try

@post("/search")
def _() :
    try :
        #connect to the database
        #get the proper search results from the database and return the results at json.dumps
        response.set_header("Content-type","application/json")
        return json.dumps([{"name":"A"},{"name":"B"}])

    except Exception as e :
        pass

    finally :
        pass