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

    gender = SelectField(
        'gender', validators=[DataRequired()],
        choices=[
            ('Male'),
            ('Female'),
    ]
    )
# TODO IMPLEMENT NEW Movie FORM AND NEW Actors
