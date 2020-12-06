from flask_wtf import FlaskForm
from wtforms import DecimalField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from datetime import date

class ConverterForm(FlaskForm):
    date = date.today().strftime("%d/%m/%Y")
    amount = DecimalField(label=" Amount ", validators=[DataRequired()])
