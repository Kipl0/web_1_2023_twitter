from bottle import get, response

@get("/logout")
def _():
    # Det virker, men klikker man tilbage i browseren, kommer man tilbage til index siden bare uden en cookie- Derfor indsætter vi cache control ovenover i /index
    response.set_cookie("user_cookie", "", expires=0) 
    response.status = 303
    response.set_header("Location", "/login")
    return
