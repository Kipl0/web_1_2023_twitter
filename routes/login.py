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
	return template("login",  USER_NAME_MIN=x.USER_NAME_MIN, USER_NAME_MAX=x.USER_NAME_MAX, PASSWORD_MIN=x.PASSWORD_MIN, PASSWORD_MAX=x.PASSWORD_MAX)

# Hvis login er succesfuldt skal man redirectes til en ny side frem for return template. Man bliver redirected når brugeren har udført en handling succesfuldt såsom en form
