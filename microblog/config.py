#Aaina Vannan
#12/6/18

import os

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    #if variable called SECRET_KEY, we get that value or default if there is not
