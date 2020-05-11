from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField
from wtforms.validators import DataRequired, AnyOf, URL



class MovieForm(Form):
    title = StringField(
        'title', validators=[DataRequired()]
    )
    release_date = StringField(
        'release_date', validators=[DataRequired()]
    )


class ActorsForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    age = StringField(
        'age', validators=[DataRequired()]
    )
    gender = SelectField(
        'gender', validators=[DataRequired()],
        choices=[
            ('Male'),
            ('Female'),
    ]
    )
# TODO IMPLEMENT NEW Movie FORM AND NEW Actors
