from bottle import get, template, request, response
import x
##############################
@get("/login")
def _():
	# x.disable_cache()
	# if user is logged, go to the profile page of that user
	login = request.get_cookie("login", secret=x.COOKIE_SECRET)
	if login:
		response.status = 303
		response.set_header("Location", f"/{login['user_username']}")
		return
	return template("login")
