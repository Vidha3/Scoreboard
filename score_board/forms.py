from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange


class DataForm(FlaskForm):
    """Form used for data entry"""
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=30)])
    score = IntegerField('Score', validators=[DataRequired(), NumberRange(min=0, max=1000)])
    submit = SubmitField('Submit your score')

