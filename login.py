#!/usr/bin/env python3

import cgi
import cgitb
from pickle import NONE
from tokenize import cookie_re

cgitb.enable()

from templates import login_page, secret_page, after_login_incorrect
import secret
import os
from http.cookies import SimpleCookie

# creating simple login form

# set up cgi form
s = cgi.FieldStorage()
username = s.getfirst('username')
password = s.getfirst('password')

# everything else to html
# print("Content-Type: text/html")
# print()

# check if login info ok
form_ok = username == secret.username and password == secret.password

# setup cookie
cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
cookie_username = None
cookie_password = None
if cookie.get("username"):
    cookie_username = cookie.get("username").value
if cookie.get("password"):
    cookie_username = cookie.get("password").value

cookie_ok = cookie_username == secret.username and cookie_password == secret.password

# then set username pass to cookie username pass
if cookie_ok:
    username = cookie_username
    password = cookie_password

print("Content-Type: text/html")
if form_ok:
    print(f"Set-Cookie: username={username}")
    print(f"Set-Cookie: password={password}")
print()

# load relevant html pages
if not username and not password:
    print(login_page())
elif username == secret.username and password == secret.password:
    print(secret_page(username, password))
else:
    print(login_page())
    print("username & password: ", username, password)