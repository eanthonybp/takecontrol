from flask_wtf import FlaskForm
from wtforms import validators, StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Required, Length, EqualTo

class TakeControlForm(FlaskForm):
    apikey = StringField('API Key', [validators.Required()])
    deviceid = StringField('Device ID', [validators.Required()])