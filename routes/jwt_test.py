# from bottle import response, get, template
# import jwt
# import x

# @get("/jwt-test")
# def _():
#     the_jwt = jwt.encode({"name":"Maja","last_name":"Larsen"}, "the secret", algorithm="HS256")

#     try :
#         user_jwt = jwt.decode(the_jwt, "the secret", algorithms=["HS256"])
#         # response.set_cookie("jwt", user_jwt, secret=x.COOKIE_SECRET, httponly=True) #Udkommenteret fordi, jeg ikke skal have en cookie liggenede aktivt.
#         # print(user_jwt)

#         return template("jwt_test")
#     except Exception as e:
#             print("Sorry cannot verify jwt")

#     finally :
#         pass



