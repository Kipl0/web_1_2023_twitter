from bottle import post, response, request, time, template
import x
import uuid
import time
import bcrypt

passwd = b'mit-password'

salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(passwd, salt)

print(salt)
print(hashed)