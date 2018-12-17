#Aaina Vannan
#Ch.1 "A Hello, World" Flask Application

from flask import Flask
from config import Config

app = Flask (__name__)
app.config.from_object(Config)

from app import routes
