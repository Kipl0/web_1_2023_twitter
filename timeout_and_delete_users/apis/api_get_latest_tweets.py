from bottle import post, response, request
import random


@post("/api-get-latest-tweets")
def _():
    # return "x"
    # TODO: get latest tweets from the db
    # tweets = db.execute("SELECT * FROM tweets ????")
    return str(int(random.randint(0, 999))) #random number er lig id for id for hvert tweet (bare et vilkårligt tal, ligesom et vilkårligt uuid4 som er id for billede)