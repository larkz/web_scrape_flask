from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

from sqlalchemy import create_engine

'''
class web_form(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
'''

class webscrape_form(FlaskForm):
    website_url = StringField('Web URL', validators=[DataRequired()])
    submit = SubmitField('Scrape')


