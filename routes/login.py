from bottle import get, template, request, response
import x
##############################
@get("/login")
def _():
	# x.disable_cache()
	# if user is logged, go to the profile page of that user
	user_cookie = request.get_cookie("user_cookie", secret=x.COOKIE_SECRET)
	if user_cookie:
		response.status = 303
		response.set_header("Location", f"/{user_cookie['user_username']}")
		return
	return template("login")
