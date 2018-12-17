#Aaina Vannan
#12/10/18

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()]) #doesn't allow user to not enter in their username
    password = PasswordField('Password', validators = [DataRequired()]) #set to list b/c validator can take +1 arguments
                                                                        #validator = object --> needs parenthesis
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
