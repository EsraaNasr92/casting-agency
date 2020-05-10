from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField
from wtforms.validators import DataRequired, AnyOf, URL



class MovieForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )



class ActorsForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
# TODO IMPLEMENT NEW Movie FORM AND NEW Actors
